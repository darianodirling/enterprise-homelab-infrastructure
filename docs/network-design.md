# Network design and firewall matrix

## Segmentation

OPNsense terminates VLAN interfaces and enforces routing policy between zones. A managed switch carries tagged VLANs to virtualization hosts; untagged access ports belong to exactly one intended VLAN.

| Source | Destination | Service | Action | Reason |
| --- | --- | --- | --- | --- |
| Admin VPN/jump | Management | HTTPS/SSH approved ports | Allow | Authorized administration |
| Kubernetes nodes | Storage NAS | TCP 2049 (NFSv4) | Allow | Persistent storage |
| Media clients | Jellyfin | TCP 8096 or HTTPS reverse proxy | Allow | Streaming |
| Guest/IoT | Management | Any | Deny | Containment |
| Guest/IoT | Storage | Any | Deny | Data protection |
| Media | Management | Any | Deny | Least privilege |
| All unapproved inter-VLAN | Any | Any | Deny and log | Default deny |

NFSv3 can require additional RPC ports; this design prefers NFSv4 where supported. Explicitly inventory DNS, NTP, identity, monitoring and backup flows before enforcement.

## Verification

- Validate VLAN tag/untag configuration on each switch port.
- Verify management access via an out-of-band path before firewall rule changes.
- Test allowed NFS, media and admin traffic from intended zones.
- Test blocked guest-to-management and media-to-management flows.
- Confirm no unintended NAT between internal VLANs and no open WAN management ports.
