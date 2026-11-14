# Architecture decisions

## ADR-001: OPNsense as segmentation gateway
Use explicit inter-VLAN policy and a default-deny baseline. **Tradeoff:** A single firewall can become a failure domain; document backup/restore and consider HA only if hardware and topology justify it.

## ADR-002: Proxmox and Nutanix CE as separate evaluation platforms
Use Proxmox for flexible VM provisioning and Nutanix CE for HCI exploration. **Tradeoff:** CE support and features differ from commercial AOS/AHV; validate compatibility before claiming functionality.

## ADR-003: ZFS plus independent backup
Use checksummed ZFS datasets and periodic snapshots; copy backups to a separate system/location. **Tradeoff:** Snapshots on the same disks cannot protect against full-device loss.

## ADR-004: Kubernetes NFS storage
Use NFS for a small lab workload where the external provisioner/CSI driver is explicitly installed and tested. **Tradeoff:** Shared NFS availability and permissions become dependencies; the sample PVC assumes a matching StorageClass exists.

## ADR-005: Jellyfin optional GPU acceleration
Start with CPU transcoding and enable GPU passthrough only after validating host drivers, container device mapping, and supported codecs. **Tradeoff:** Device passthrough can reduce portability and increase operational complexity.
