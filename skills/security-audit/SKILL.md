---
name: security-audit
description: "Audit repository code and containers for hardcoded secrets, misconfigured permissions, and dependency vulnerabilities."
risk: low
---

# Security Audit Runbook

## Protocol
1. **Secrets Scan**: Search working tree for high-entropy tokens, private keys (`BEGIN RSA PRIVATE KEY`), or uncommitted `.env` files.
2. **Permission Check**: Ensure no world-writable files (`chmod 777`) exist in the repository.
3. **Dependency Vulnerabilities**: Run security audit on package manifests (`npm audit` or `pip-audit`).
