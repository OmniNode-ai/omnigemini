# Contributing to omnigemini

## Prerequisites

- Python 3.12+

This repo does not yet ship a `pyproject.toml` or `.pre-commit-config.yaml` — there is no `uv sync` / `pre-commit install` step to run here today. See "Development Status" in `README.md` for the current state.

---

## Development Workflow

### 1. Create a worktree

All work happens in a git worktree. Never commit directly to `omni_home/omnigemini/`.

```bash
TICKET="OMN-XXXX"
git -C "$OMNI_HOME/omnigemini" worktree add \
  "$OMNI_HOME/omni_worktrees/$TICKET/omnigemini" \
  -b "jonah/$TICKET-description"
```

### 2. Make changes

Follow the patterns in `CLAUDE.md`. For new skill nodes, copy an existing `node_skill_*_orchestrator/` directory and update the contract and node class name.

### 3. Verify before pushing

This repo has no `tests/`, `pyproject.toml`, or `.pre-commit-config.yaml`, so there is no lint/test/type-check command to run. Verify by reading the diff against existing node/contract patterns.

### 4. Open a PR

- Title must contain `OMN-XXXX`.
- Body must cite `OMN-XXXX` with a `## DoD evidence` section.
- No `[skip-*]` bypass tokens.

---

## Code Standards

All code must follow the standards in `~/.claude/CLAUDE.md` and `omni_home/CLAUDE.md`. Key rules (style conventions to follow now; `uv`/`ruff`/`mypy`/pytest enforcement is not yet wired in this repo — see "Prerequisites" above):

- Python 3.12+.
- PEP 604 unions (`X | Y`, not `Optional[X]`).
- Never hardcode Kafka topic strings — declare in `contract.yaml`.
