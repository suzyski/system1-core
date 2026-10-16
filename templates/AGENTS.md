# AGENTS.md — System 1 Architecture Integration

Add the following section to your repository's root `AGENTS.md` or system prompt:

```markdown
## Dual-Engine System 1 Gating
Every autonomous agent operating in this codebase MUST execute through the reflexive System 1 layer:

1. **Before Coding / Architecting**:
   Run `jev route "<task topic>"` (or `system1 route "<topic>"`) to retrieve pre-existing battle-tested runbooks and avoid hallucinated patterns.
   
2. **Before Destructive Actions**:
   Run `jev gate "<proposed command>"`.
   - If output contains `"top_label": "high_risk_destructive"`, HALT immediately and ask the user for confirmation.
   - If `"safe_read_or_test"` or `"standard_edit"`, proceed autonomously.

3. **When Handling Verbose Outputs**:
   If test outputs, compiler errors, or terminal dumps exceed 40 lines, compress via:
   `jev compress "<verbose text>"`
   Use the compressed output to conserve 30–70% of prompt context without losing error details.

4. **Before Declaring Task Done**:
   Run `jev verify "<user goal>" "<outcome summary & test proof>"`.
   Only declare complete if the critic returns `"top_label": "fully_satisfied"`.
```
