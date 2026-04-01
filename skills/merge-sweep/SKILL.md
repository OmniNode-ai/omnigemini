---
name: merge-sweep
description: Org-wide PR merge sweep — enables GitHub auto-merge on ready PRs and runs pr-polish on Track BPRs
capability: skill.merge_sweep
node_name: node_skill_merge_sweep_orchestrator
dot_color: 39
---

# Merge Sweep Skill (Gemini Edition)

Org-wide PR sweep that scans all repositories in `omni_home` for open PRs and handles them in three tracks using Gemini's long context window for classification and orchestration.

## Workflow
1. **Scan**: List all open PRs across all repositories using `gh pr list`.
2. **Classify**: Use Gemini to categorize PRs into:
    - **Track A (Auto-Merge)**: Green, approved, current branch.
    - **Track A-update**: Needs branch update or unknown mergeable state.
    - **Track B (Polish)**: Conflicting, failing CI, or changes requested.
3. **Execution**:
    - **Track A**: Enable `gh pr merge --auto`.
    - **Track A-update**: Trigger `gh api -X PUT .../update-branch`.
    - **Track B**: Dispatch to `pr-polish` skill in a dedicated worktree.
4. **Summary**: Report sweep results to Slack and the event bus.

## Arguments
- `--repos`: Comma-separated repo names to scan.
- `--dry-run`: Print candidates without taking action.
- `--skip-polish`: Only process Track A PRs.
