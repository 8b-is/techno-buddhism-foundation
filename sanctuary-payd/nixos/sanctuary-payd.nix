{ config, pkgs, lib, ... }:

let
  sanctuaryPayd = pkgs.rustPlatform.buildRustPackage {
    pname = "sanctuary-payd";
    version = "0.1.0";
    src = /srv/sanctuary-payd;
    cargoLock.lockFile = /srv/sanctuary-payd/Cargo.lock;
  };
in {
  # 1. Secrets managed via sops-nix (zero plaintext secrets in /nix/store)
  # Contains:
  #   STRIPE_WEBHOOK_SECRET=whsec_...
  #   REVOLUT_WEBHOOK_SECRET=wsk_...
  #   PAYPAL_WEBHOOK_TOKEN=...
  #   DOWNLOAD_SIGNING_KEY=<64-byte hex key>
  sops.secrets."sanctuary-payd.env" = {
    sopsFile = ./secrets/sanctuary-payd.yaml;
    format = "dotenv";
  };

  # 2. Hardened systemd service
  systemd.services.sanctuary-payd = {
    description = "Sovereign Sanctuary Zero-Disclosure Payment & Book Unlock Daemon";
    wantedBy = [ "multi-user.target" ];
    after = [ "network.target" ];

    environment = {
      BIND_ADDR = "127.0.0.1:8108";
      VAULT_DIR = "/var/lib/sanctuary-payd/vault";
      PUBLIC_BASE_URL = "https://technobuddhism.8b.is";
    };

    serviceConfig = {
      ExecStart = "${sanctuaryPayd}/bin/sanctuary-payd";
      EnvironmentFile = config.sops.secrets."sanctuary-payd.env".path;
      DynamicUser = true;
      StateDirectory = "sanctuary-payd";
      Restart = "always";
      RestartSec = "2s";

      # Hardening (Mahakala Trit -1 Boundary)
      NoNewPrivileges = true;
      ProtectSystem = "strict";
      ProtectHome = true;
      PrivateTmp = true;
      PrivateDevices = true;
      ProtectKernelTunables = true;
      ProtectControlGroups = true;
      RestrictSUIDSGID = true;
      LockPersonality = true;
      MemoryDenyWriteExecute = true;
    };
  };

  # 3. Self-Hosted Caddy on technobuddhism.8b.is
  services.caddy = {
    enable = true;
    virtualHosts."technobuddhism.8b.is" = {
      extraConfig = ''
        encode zstd gzip

        handle /api/* {
          reverse_proxy 127.0.0.1:8108
        }

        handle {
          root * /var/www/technobuddhism.8b.is
          file_server
        }
      '';
    };
  };
}
