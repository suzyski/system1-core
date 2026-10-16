---
name: git-hygiene
description: "Git hygiene protocol for agentic workflows: status verification, atomic commits, branch isolation, and safe pushes."
risk: low
---

# Git Hygiene Runbook

## Protocol
1. **Status Verification**: Always inspect `git status` and `git diff` before staging.
2. **Atomic Commits**: Group related changes logically with clear, imperative commit messages.
3. **No Force Pushes**: Never push `--force` to protected branches (`main`, `master`, `production`).
