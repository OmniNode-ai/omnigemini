---
name: ci-watch
description: Gemini-native per-PR CI monitoring — polls GitHub Actions, auto-fixes introduced failures, and reports state with 2M+ token grounding
capability: skill.ci_watch
node_name: node_skill_ci_watch_orchestrator
dot_color: 208
---

# CI Watch Skill (Gemini Edition)

Monitor CI status for a specific pull request, leveraging Gemini's long context to distinguish between introduced and pre-existing failures and providing autonomous repair loops.

## Workflow
1. **Polling**: Uses `gh` CLI or the ONEX event bus to monitor CI status checks for a target PR.
2. **Triage**: Gemini compares current failures against the base branch (`main`) to classify each failing check as `PRE-EXISTING` or `INTRODUCED`.
3. **Remediation (Introduced)**: Gemini dispatches a `ci-fix-pipeline` fix agent on the current branch to resolve new failures.
4. **Remediation (Pre-existing)**: Dispatches a background fix agent targeting `main` to address existing technical debt without blocking the current PR.
5. **Iteration**: Automatically waits for new CI runs and iterates until a terminal state is reached (`passed`, `capped`, `timeout`).

## Gemini Advantages
- **Deep Triage Logic**: Better at identifying when a failure is "pre-existing" by analyzing the relationship between the PR diff and the failing test context.
- **Autonomous Repair Loops**: More effective at fixing introduced failures by seeing the entire repository state simultaneously.
- **Push-Based Integration**: Natively integrates with the Gemini-native emit daemon for real-time CI status updates.

## Arguments
- `pr_number`: GitHub PR number to watch.
- `repo`: GitHub repository slug (org/repo).
- `--timeout-minutes`: Max wait time for CI.
- `--no-auto-fix`: Poll only, don't attempt repairs.
