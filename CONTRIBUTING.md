# Contributing to omnigemini

## Prerequisites

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) for dependency management
- `pre-commit` for local enforcement hooks

```bash
uv sync --all-groups
pre-commit install
```

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

```bash
uv run ruff format src/ tests/ && uv run ruff check --fix src/ tests/
uv run pytest tests/ -v
uv run mypy src/ --strict
pre-commit run --all-files
```

### 4. Open a PR

- Title must contain `OMN-XXXX`.
- Body must cite `OMN-XXXX` with a `## DoD evidence` section.
- No `[skip-*]` bypass tokens.

---

## Code Standards

All code must follow the standards in `~/.claude/CLAUDE.md` and `omni_home/CLAUDE.md`. Key rules:

- Python 3.12+, `uv` for all commands.
- PEP 604 unions (`X | Y`, not `Optional[X]`).
- `ruff` for formatting and linting.
- `mypy --strict` target.
- Every change ships with a unit test.
- Never hardcode Kafka topic strings — declare in `contract.yaml`.
