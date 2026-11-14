#!/usr/bin/env python3
"""Offline structural checks only; no live lab connectivity or syntax validation."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", "docs/network-design.md", "docs/architecture-decisions.md",
    "docs/storage-zfs-nfs.md", "docs/backup-recovery-runbook.md",
    "docs/implementation-runbook.md", "configs/opnsense/firewall-intent.yaml",
    "configs/proxmox/interfaces.example", "configs/cloud-init/user-data.yaml",
    "k8s/namespace.yaml", "k8s/nfs-pvc.yaml", "k8s/jellyfin.yaml",
]
missing = [p for p in required if not (root / p).is_file()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))
assert "mermaid" in (root / "README.md").read_text()
assert "default_interzone_action: deny" in (root / "configs/opnsense/firewall-intent.yaml").read_text()
print("PASS: reference structure and security intent present.")
print("NOTE: live deployment, syntax and compatibility are NOT validated.")
