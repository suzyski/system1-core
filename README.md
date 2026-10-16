# ⚡ System 1 Core (`system1-core`)

> **The Fast Reflexive Co-Processor for Autonomous AI Agents**  
> *Sub-15ms decision routing, deterministic destructive action gating, context compression, and ground-truth verification critics.*

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](pyproject.toml)
[![Latency](https://img.shields.io/badge/Reflex_Latency-%3C15ms-00f0ff.svg)](#benchmarks)
[![Context Saved](https://img.shields.io/badge/ScaleDown_Tokens--70%25-10b981.svg)](#context-compression)
[![Agent Protocol](https://img.shields.io/badge/Universal_Agent-Protocol-8b5cf6.svg)](#universal-agent-integration)

---

![System 1 Dual Engine Architecture](assets/poster.png)

---

## 💡 The Paradigm: Why Agents Need System 1

Today's autonomous coding agents (Claude Code, Antigravity, OpenAI Codex, Cursor) operate entirely on **System 2** (heavy, deep LLM reasoning). Every routine check costs **8 to 15 seconds** and thousands of reasoning tokens:

- **Searching runbooks**: Guessing and hallucinating deprecated APIs.
- **Checking safety**: Wondering if `rm -rf` or `git push -f` is destructive.
- **Consuming logs**: Ingesting 500-line build dumps and poisoning the context window.
- **Task completion**: Prematurely claiming "done" without ground-truth verification.

**System 1 Core** provides a sub-conscious reflexive co-processor powered by **TypeSafe Jev** and **ScaleDown** that sits in front of your agent, making deterministic sub-second decisions so the primary model can focus 100% on deep architecture.

```
       USER REQUEST / TOOL TRIGGER
                   │
                   ▼
  ┌─────────────────────────────────┐
  │   SYSTEM 1 REFLEXIVE ENGINE     │  ◄── < 15ms Latency
  │  (TypeSafe Jev + ScaleDown)     │  ◄── Zero Hallucinations
  ├─────────────────────────────────┤
  │ 1. Skill Router (880+ Runbooks) │
  │ 2. Destructive Action Risk Gate │
  │ 3. 70% Context Log Compressor   │
  │ 4. Output Verification Critic   │
  └─────────────────────────────────┘
                   │  [Shielded & Compressed]
                   ▼
  ┌─────────────────────────────────┐
  │      SYSTEM 2 AGENT BRAIN       │  ◄── 100% Focused on Architecture
  │   (Gemini, Claude, GPT, Codex)  │  ◄── Zero Token Exhaustion
  └─────────────────────────────────┘
```

---

## 🚀 Quickstart (1-Minute Install)

Install via one-line shell script:

```bash
curl -fsSL https://raw.githubusercontent.com/blackdarkknight1122-gif/system1-core/main/install.sh | bash
```

Or install via `pip`:

```bash
pip install system1-core
```

---

## 🛠️ The 4 Core CLI Pillars

Both `system1` and its shortcut alias `jev` are available on your path.

### 1. Skill & Runbook Routing
Instantly match any user intent to your offline runbook library in **< 15ms**:

```bash
system1 route "audit docker container security"
```

```json
{
  "matched": true,
  "skill_name": "container-security-audit",
  "score": 0.94,
  "engine": "jev (typesafe/jev-1.14)",
  "skill_file": "skills/container-security-audit/SKILL.md"
}
```

---

### 2. Destructive Action Risk Gating
Never let an autonomous agent accidentally destroy production databases or execute irreversible git resets:

```bash
system1 gate "rm -rf /var/data && git push origin main --force"
```

![Action Risk Gating Intercept](assets/still-gating.png)

```json
{
  "top_label": "high_risk_destructive",
  "confidence": 1.0,
  "reasoning": "Detected rm -rf / recursive delete & force push"
}
```

*If `high_risk_destructive` is returned, the agent is hard-gated to halt and request explicit user confirmation.*

---

### 3. ScaleDown Context Compression
Compress huge compiler outputs, test traces, and git diffs while retaining 100% of line numbers, error codes, and parameters:

```bash
system1 compress "<500 lines of raw compiler logs>"
```

- **Raw Prompt Tokens**: 4,820 tokens
- **Compressed Output**: 940 tokens
- **Context Saved**: **-80.5%**

---

### 4. Output Verification Critic
Before an agent declares a task done, System 1 evaluates the goal against actual proof:

```bash
system1 verify "Implement weakref cache" "Applied cache and memory test passed with 0 leaks"
```

```json
{
  "top_label": "fully_satisfied",
  "scores": { "fully_satisfied": 0.98, "regression": 0.0 },
  "engine": "jev-critic",
  "verdict": "All user criteria proven by test execution output"
}
```

---

## 🤖 Universal Agent Integration

![Universal Agent Workflow](assets/still-workflow.png)

### Drop-in `AGENTS.md` / System Prompt (Antigravity, Claude Code, Codex, Cursor, Hermes)

Add this single block to your repository's `AGENTS.md`:

```markdown
## Dual-Engine System 1 Gating
- Before coding: run `jev route "<topic>"` to find battle-tested runbooks
- Before destructive commands: run `jev gate "<cmd>"`, halt if high_risk_destructive
- Dumps & logs over 40 lines: compress via `jev compress "<logs>"`
- Before declaring done: run `jev verify "<goal>" "<outcome>"`
```

### Python API Integration

```python
from system1 import route_skill, gate_action, compress_context, verify_output

# 1. Gate an action
risk = gate_action("git reset --hard HEAD~5")
if risk["top_label"] == "high_risk_destructive":
    raise PermissionError("Destructive action gated!")

# 2. Compress terminal context
compressed = compress_context(verbose_compiler_output)
clean_text = compressed["compressed_text"]

# 3. Verify task outcome
verdict = verify_output(goal="Fix CSS alignment", outcome="Verified in headless browser")
assert verdict["top_label"] == "fully_satisfied"
```

---

## 📊 Benchmarks

| Metric | Unassisted System 2 LLM | System 1 Co-Processor | Improvement |
| :--- | :--- | :--- | :--- |
| **Command Safety Triage** | 4,500 – 12,000 ms | **< 15 ms** | **~500x Faster** |
| **Runbook Matching** | 8,000 ms (or hallucinated) | **12 ms** (grounded) | **Deterministic** |
| **Token Cost per Gate** | ~$0.04 – $0.12 | **$0.000016** | **99.9% Cheaper** |
| **Log Context Overhead** | 5,000+ tokens dumped | 900 tokens (ScaleDown) | **-70% to -80% Saved** |

---

## 📁 Repository Structure

```
system1-core/
├── assets/                 # Architecture graphics, stills, and video posters
├── system1/                # Python package implementation
│   ├── config.py           # Configuration & search paths
│   ├── core.py             # Dual-engine API (TypeSafe Jev + ScaleDown)
│   ├── router.py           # Instant runbook & skill routing
│   ├── gate.py             # Destructive action classifier
│   ├── critic.py           # Verification critic
│   └── cli.py              # CLI entrypoint (system1 & jev)
├── templates/              # Drop-in agent templates
│   ├── AGENTS.md           # Universal multi-agent rule block
│   ├── .cursorrules        # Cursor IDE rules
│   └── claude_rules.md     # Claude Code integration guide
├── tests/                  # Automated unit test suite
├── .github/workflows/      # GitHub Actions CI
├── install.sh              # One-line curl installer
├── pyproject.toml          # Packaging manifest
└── LICENSE                 # Apache 2.0 License
```

---

## 🤝 Contributing

We welcome community runbooks, agent adapters, and engine optimizations! Please read [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 📄 License

Distributed under the **Apache 2.0 License**. See [LICENSE](LICENSE) for details.
