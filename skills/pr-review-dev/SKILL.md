---
name: pr-review-dev
description: Gemini-native PR issue resolution — auto-fixes review comments and CI failures with whole-project grounding
capability: skill.pr_review_dev
node_name: node_skill_pr_review_dev_orchestrator
dot_color: 39
---

# PR Review Dev Skill (Gemini Edition)

Autonomous PR issue resolution loop that leverages Gemini's massive context window to fix both PR review comments and CI failures in a single coordinated pass.

## Workflow
1. **Gather & Collate**: Gemini fetches all PR feedback and CI failure logs, merging them into a unified, severity-classified list.
2. **Fix Phase**: Gemini orchestrates surgical fixes for all CRITICAL, MAJOR, and MINOR issues across multiple files simultaneously.
3. **CI Triage**: Gemini analyzes CI logs to distinguish between introduced failures (fixed on the PR branch) and pre-existing technical debt (fixed in background PRs).
4. **Parallel Execution**: Dispatches multiple fix agents to address independent issue clusters in dedicated worktrees.
5. **Verification**: Gemini verifies that all blocking issues are resolved and that the codebase adheres to organization-wide standards before marking the work complete.

## Gemini Advantages
- **Context-Aware Fixing**: Gemini correctly identifies the root cause of CI failures by analyzing the relationship between the PR diff, tests, and global configuration.
- **Intelligent Comment Resolution**: Better at interpreting technical feedback and generating high-fidelity fixes that respect the reviewer's intent.
- **Multi-Repo CI Triage**: Simultaneously analyzes CI failures across all organization repositories to identify cross-repo regression sources.

## Arguments
- `pr_url`: PR URL or number.
- `--no-ci`: Skip CI failure analysis.
- `--include-nits`: Auto-fix optional nits during the main loop.
