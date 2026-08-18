# CLAUDE.md

> **Shared standards** (Python, Git, Testing, Infrastructure) are in `~/.claude/CLAUDE.md`.
> **Platform operating rules** are in `omni_home/CLAUDE.md`.

This file provides repo-local context for Claude Code when working in `omnigemini`.

---

## Repository Overview

`omnigemini` is the **Gemini-native execution layer** for ONEX platform skills. It exposes 47 skill Orchestrator nodes backed by the Gemini CLI (`execution.backend: gemini_cli`) plus two Effect nodes for Kafka event emission and dynamic contract discovery.

Every skill in `omniclaude/skills/` has a corresponding `node_skill_*_orchestrator` node here. The node's contract references the skill's `SKILL.md` as the Gemini grounding prompt.

---

## Directory Structure

```text
omnigemini/
├── skills/                              # Gemini prompt files (one SKILL.md per skill)
├── src/omnigemini/
│   ├── nodes/
│   │   ├── node_gemini_emit_effect/     # Kafka publisher (NodeGeminiEmitEffect)
│   │   ├── node_registry_api_effect/    # Contract discovery (NodeRegistryApiEffect)
│   │   └── node_skill_*_orchestrator/  # Thin Gemini delegates (47 total)
│   └── shared/
│       └── models/                     # ModelSkillRequest, ModelSkillResult
```

---

## Architecture Rules

### Node conventions

- All node classes follow `Node<Name><Type>` naming (`NodeGeminiEmitEffect`, `NodeSkillPrReviewOrchestrator`).
- All models use `Model` prefix and are Pydantic `BaseModel` with `model_config = ConfigDict(frozen=True, extra="forbid")`.
- Contract YAML is the source of truth for topics and I/O model declarations. Never hardcode topic strings in Python.

### Execution backend

Skill orchestrator nodes declare `execution: {backend: gemini_cli}` in their `contract.yaml`. Effect nodes use `execution: {backend: python}`. Do not change the backend without updating the contract.

### Topic naming

All OmniGemini Kafka topics follow `onex.evt.omnigemini.<event-name>.v<N>`. New event types must be declared in the relevant `contract.yaml` under `yaml_published_events` or `yaml_consumed_events` before being referenced in Python code.

### Adding a new skill

1. Create `skills/<name>/SKILL.md` with frontmatter fields: `name`, `description`, `capability`, `node_name`, `dot_color`.
2. Create `src/omnigemini/nodes/node_skill_<name>_orchestrator/` with:
   - `contract.yaml` — node contract with `node_type: ORCHESTRATOR_GENERIC`, `execution: {backend: gemini_cli}`, and topic declarations.
   - `node.py` — subclass of `NodeOrchestrator` with only `__init__` needed (logic lives in Gemini CLI layer).
   - `__init__.py` — re-export the node class.

Follow existing nodes (e.g. `node_skill_pr_review_orchestrator`) exactly — no divergence.

### What does NOT belong here

- Business logic or prompt engineering belongs in `skills/<name>/SKILL.md` or `omnimarket` nodes.
- Kafka infrastructure wiring belongs in `omnibase_infra`.
- Claude Code plugin hooks belong in `omniclaude`.

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `KAFKA_BOOTSTRAP_SERVERS` | Yes | Kafka bootstrap address (e.g. `<kafka-bootstrap-servers>:19092`) |
| `ONEX_ENVIRONMENT` | No | Runtime environment label (default: `local`) |

Never hardcode connection strings. Read all config from `KAFKA_BOOTSTRAP_SERVERS` or Infisical.

---

## Development Commands

This repo has no `pyproject.toml`, `tests/` directory, or `.pre-commit-config.yaml` — the standard `uv sync` / `pytest` / `mypy --strict` / `ruff` / `pre-commit` workflow described in `~/.claude/CLAUDE.md` is not wired here yet. Do not run those commands against this repo; there is currently nothing for them to target. Verify changes here by reading the diff against the node/contract patterns in `omnibase_core` and `omnibase_infra`.

---

## Pre-push Checklist

```
[ ] PR title contains OMN-XXXX
[ ] PR body cites OMN-XXXX with ## DoD evidence section
[ ] No [skip-*] bypass tokens
```
