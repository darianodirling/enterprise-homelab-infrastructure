# ZFS and NFS design

## ZFS planning

- Prefer disks with known health and sufficient RAM; plan capacity for snapshots and rebuilds.
- Choose mirror or RAIDZ layout according to recovery objectives and disk count.
- Enable compression where appropriate; document dataset quotas and recordsize decisions.
- Scrub and monitor SMART health regularly.
- Use snapshots for quick rollback, but **replicate or back up to independent storage**.

## Illustrative commands (review before running)

```bash
# DANGEROUS if run against the wrong disks: examples only; do not execute unchanged.
# zpool create tank mirror /dev/disk/by-id/REPLACE_DISK_A /dev/disk/by-id/REPLACE_DISK_B
# zfs create tank/k8s
# zfs create tank/media
# zfs snapshot tank/media@before-maintenance
```

## NFS

Prefer NFSv4 with restricted export CIDRs and root squashing. Review UID/GID mappings, ACLs, export options and Kubernetes storage driver behavior. Never export storage broadly to guest or WAN networks.

Example export intent: `/tank/k8s 10.10.30.0/24(rw,sync,root_squash,no_subtree_check)`; verify actual filesystem mount path and NFS server syntax.

## Recovery

Test restore from both snapshots and an independent backup target. Record recovery duration, recovered file integrity and access-control verification.
