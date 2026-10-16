# Claude Code Integration Guide

To equip **Claude Code** with System 1 reflexes:

1. Install `system1-core`:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/blackdarkknight1122-gif/system1-core/main/install.sh | bash
   ```

2. Add custom tool or command permissions to `~/.claude.json` or project `CLAUDE.md`:
   ```markdown
   ## System 1 Engine
   - Always run `system1 gate "<bash command>"` before running rm, git push -f, or migration scripts.
   - Run `system1 compress "<output>"` on outputs over 40 lines.
   - Run `system1 verify "<task>" "<result>"` before declaring completion.
   ```
