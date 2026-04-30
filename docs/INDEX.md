# omnigemini — Documentation Index

## Repository-level docs

| Document | Purpose |
|----------|---------|
| [README.md](../README.md) | What the repo is, quickstart, architecture overview |
| [CLAUDE.md](../CLAUDE.md) | Operating rules for Claude Code agents working in this repo |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Contribution workflow, branching conventions, PR checklist |
| [SECURITY.md](../SECURITY.md) | Vulnerability disclosure policy |
| [LICENSE](../LICENSE) | MIT license |

## Node contracts

Every node has a `contract.yaml` that is the source of truth for its topics, I/O models, and execution backend.

| Node | Contract |
|------|---------|
| `node_gemini_emit_effect` | `src/omnigemini/nodes/node_gemini_emit_effect/contract.yaml` |
| `node_registry_api_effect` | `src/omnigemini/nodes/node_registry_api_effect/contract.yaml` |
| `node_skill_*_orchestrator` (×47) | `src/omnigemini/nodes/node_skill_*/contract.yaml` |

## Skill definitions

Each skill prompt lives in `skills/<name>/SKILL.md`. The skill's `node_name` field maps it to the corresponding orchestrator node.

## Shared standards

- Python, Git, Testing: `~/.claude/CLAUDE.md`
- Platform operating rules: `$OMNI_HOME/omni_home/CLAUDE.md`
