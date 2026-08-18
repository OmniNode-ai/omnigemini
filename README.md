# omnigemini

Gemini-native ONEX skill execution runtime — leverages Google Gemini's 2M+ token context window to run platform skills with whole-project grounding.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What This Repo Is

`omnigemini` (package: `omnigemini`) is the **Gemini-backed execution layer** for ONEX platform skills. It exposes every skill defined in `omniclaude` as a Kafka-driven Orchestrator node backed by the Gemini CLI, enabling whole-codebase grounding for reviews, sweeps, and code generation tasks that exceed the context window of standard LLMs.

Key responsibilities:

- Hosting 47 skill Orchestrator nodes (one per skill) that consume `onex.evt.omnigemini.skill-requested.v1` and delegate to Gemini CLI with the skill's `SKILL.md` prompt.
- Publishing lifecycle events (`skill-started`, `skill-completed`) for observability and downstream coordination.
- Providing `NodeGeminiEmitEffect` — the canonical Kafka publisher for all OmniGemini events.
- Providing `NodeRegistryApiEffect` — project-wide contract discovery and runtime topic registration using Gemini's context window for organization-scale grounding.

---

## Who Uses This Repo

| Consumer | Usage |
|----------|-------|
| `omniclaude` | Dispatches skills to Gemini backend via Kafka events |
| `omnimarket` | Invokes Gemini-native nodes as part of multi-model fan-out pipelines |
| ONEX runtime | Registers and routes topics discovered by `NodeRegistryApiEffect` |
| Platform operators | Runs Gemini-backed code review, sweep, and generation tasks |

---

## What This Repo Owns

- **Skill Orchestrator nodes**: 47 `node_skill_*_orchestrator/` directories, each with a `contract.yaml` and thin `node.py` that wraps the corresponding `SKILL.md`.
- **Core Effect nodes**: `NodeGeminiEmitEffect` (Kafka publish) and `NodeRegistryApiEffect` (dynamic contract discovery).
- **Shared models**: `ModelSkillRequest` and `ModelSkillResult` — the typed I/O envelope for all skill dispatches.
- **Skill definitions**: `skills/<name>/SKILL.md` — prompt and capability declarations consumed by the Gemini CLI backend.

## What This Repo Does Not Own

- **Skill business logic**: portable node handlers live in `omnimarket`.
- **Kafka infrastructure**: topic registration wiring is owned by `omnibase_infra`.
- **Claude Code plugin hooks**: skill slash-command definitions live in `omniclaude`.
- **UI rendering**: skill results are rendered in `omnidash`.

---

## Development Status

This repo currently ships skill prompt definitions (`skills/*/SKILL.md`) and node scaffolding (`src/omnigemini/nodes/*`) only. There is no `pyproject.toml`, `tests/` directory, `.pre-commit-config.yaml`, or CI workflow in this repo yet, so the `uv sync` / `pytest` / `mypy` / `ruff` workflow used in other OmniNode repos is not wired here — there is no local command to run against this repo today. Node handlers import from `omnibase_core` / `omnibase_infra`, whose own packaging and test suites cover that code; this repo's own packaging is not yet built.

---

## Common Workflows

### Invoke a skill via Kafka

Publish a `ModelSkillRequest` to `onex.evt.omnigemini.skill-requested.v1`. The appropriate `node_skill_*_orchestrator` node picks it up and delegates to Gemini CLI using the skill's `SKILL.md` as the grounding prompt.

```python
from omnigemini.shared.models import ModelSkillRequest
import uuid

request = ModelSkillRequest(
    skill_name="pr_review",
    skill_path="skills/pr-review/SKILL.md",
    args={"PR_NUMBER": "42"},
    correlation_id=uuid.uuid4(),
)
```

### Add a new skill

1. Create `skills/<name>/SKILL.md` with the skill's prompt and capability declaration.
2. Create `src/omnigemini/nodes/node_skill_<name>_orchestrator/` with `contract.yaml`, `node.py`, and `__init__.py` following existing patterns.
3. Wire `yaml_consumed_events` / `yaml_published_events` in the contract.

---

## Architecture

```text
omnigemini/
├── skills/                              # Gemini prompt definitions (SKILL.md per skill)
│   ├── pr-review/SKILL.md
│   ├── hostile-reviewer/SKILL.md
│   └── ...  (47 skills total)
├── src/omnigemini/
│   ├── nodes/
│   │   ├── node_gemini_emit_effect/     # Kafka publisher for OmniGemini events
│   │   ├── node_registry_api_effect/    # Dynamic contract discovery + topic registration
│   │   └── node_skill_*_orchestrator/  # One per skill — thin Gemini CLI delegates
│   └── shared/
│       └── models/                     # ModelSkillRequest, ModelSkillResult
```

### Node types in use

| Type | Count | Purpose |
|------|-------|---------|
| `ORCHESTRATOR_GENERIC` | 47 | Skill dispatch to Gemini CLI |
| `EFFECT` | 2 | Kafka publish, contract discovery |

### Kafka topics

All topics follow the ONEX convention `onex.{cmd|evt}.{service}.{event}.v{N}`.

| Topic | Direction | Description |
|-------|-----------|-------------|
| `onex.evt.omnigemini.skill-requested.v1` | consumed | Triggers skill execution |
| `onex.evt.omnigemini.skill-started.v1` | published | Skill execution started |
| `onex.evt.omnigemini.skill-completed.v1` | published | Skill execution completed |

### Execution backend

Skill orchestrator nodes use `execution.backend: gemini_cli` in their contracts. The effect nodes use the standard Python backend with `omnibase_infra.event_bus.event_bus_kafka`.

---

## Documentation Map

| Document | Location |
|----------|----------|
| Repo-local operating rules | `CLAUDE.md` |
| Skill prompt definitions | `skills/<name>/SKILL.md` |
| Node contracts | `src/omnigemini/nodes/*/contract.yaml` |
| Shared standards (Python, Git, Testing) | `~/.claude/CLAUDE.md` |
| ONEX platform standards | `omni_home/CLAUDE.md` |

---

## Security

See [SECURITY.md](SECURITY.md) for the vulnerability disclosure policy.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines, branching conventions, and the PR checklist.

## License

MIT — see [LICENSE](LICENSE).
