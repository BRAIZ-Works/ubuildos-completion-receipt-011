# Security

## Shipped architecture
The release is static HTML, CSS, and JavaScript. It contains:
- no backend;
- no credentials or secrets;
- no authentication;
- no third-party runtime libraries;
- no external API calls;
- no remote code loading.

## Security consequence
The small static surface reduces runtime attack surface, but the demo also omits controls required by a real approval system.

## Production requirements
A production implementation would need authenticated identity, authorization/least privilege, server-side validation, protected persistence, tamper-evident decision history, dependency/secret governance, logging/monitoring, threat modeling, vulnerability management, and incident/recovery procedures.

## Integrity
`PUBLIC_MANIFEST.json` and `SHA256SUMS.txt` provide public-file integrity references. Integrity verification does not establish malware safety, legal compliance, or fitness for purpose.
