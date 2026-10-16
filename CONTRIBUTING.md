# Contributing to System 1 Core

Thank you for your interest in contributing to the System 1 architecture!

## How to Contribute

1. **Agent Adapters**: Add support for new agent frameworks (e.g. LangChain, AutoGen, CrewAI, Roo Code).
2. **Classifier Rubrics**: Enhance safety categories in `system1/gate.py`.
3. **Runbook Skills**: Add curated skills and runbooks under `skills/`.

## Local Development

```bash
git clone https://github.com/suzyski/system1-core.git
cd system1-core
pip install -e .
python -m unittest discover tests
```

All pull requests must pass automated CI checks.
