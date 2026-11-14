# Backup and recovery runbook

## Preflight

- [ ] Inventory Proxmox VM backups, Nutanix CE workloads, Kubernetes manifests, OPNsense configuration and ZFS datasets.
- [ ] Confirm backup encryption, retention, independent/offsite copy and restore credentials.
- [ ] Document application-consistent backup requirements.
- [ ] Confirm target hardware capacity and network isolation for restore tests.

## Exercise

1. Export OPNsense configuration securely and verify it is restorable.
2. Restore a disposable Proxmox VM to an isolated VLAN; verify boot, network and application checks.
3. Restore a representative ZFS dataset from an independent backup copy.
4. Recreate Kubernetes namespace and manifests; restore persistent application data.
5. Validate Jellyfin library mounts and media metadata without exposing the test instance publicly.
6. Record actual RPO/RTO, restore timestamps, integrity checks and any failures.
7. Remove isolated test resources and retain redacted evidence.

## Incident recovery priorities

1. Network access and secure management plane.
2. Storage integrity and backup availability.
3. Hypervisor and Kubernetes control planes.
4. Stateful applications and user-facing services.
5. Monitoring, alerting and post-incident review.

Do not assume snapshots alone are a disaster recovery strategy.
