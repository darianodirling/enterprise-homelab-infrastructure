# Implementation and validation checklist

- [ ] Document CPU/RAM/storage inventory, BIOS virtualization and NIC support.
- [ ] Back up switch and firewall configs; establish emergency management access.
- [ ] Configure VLAN trunks, DHCP/DNS and firewall matrix.
- [ ] Confirm no WAN exposure of OPNsense, Proxmox, Nutanix or NAS management.
- [ ] Configure Proxmox bridge and test VM connectivity.
- [ ] Validate Nutanix CE hardware/software support for chosen build.
- [ ] Configure ZFS datasets, NFS exports, snapshots and separate backups.
- [ ] Validate Kubernetes node readiness, CNI, DNS and storage provisioning.
- [ ] Deploy Jellyfin with a nonprivileged security context where feasible.
- [ ] Test negative segmentation cases and permitted application flows.
- [ ] Test independent backup restores and document actual recovery times.
- [ ] Document monitoring, patching, certificate renewal and access review.
