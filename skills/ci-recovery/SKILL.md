---
name: ci-recovery
description: Gemini-native organization-wide CI recovery — scans all open PRs, classifies failures, and applies remediation with 2M+ token grounding
capability: skill.ci_recovery
node_name: node_skill_ci_recovery_orchestrator
dot_color: 208
---

# CI Recovery Skill (Gemini Edition)

Organization-wide CI recovery pipeline that polls all open PRs across OmniNode-ai repositories, leveraging Gemini's massive context window to accurately classify failures and orchestrate automated remediation.

## Workflow
1. **Scan**: Gemini lists all open PRs and extracts CI failure logs for those with failing status checks.
2. **Classification**: Categorizes failures using Gemini's deep log analysis:
    - `flaky_test`: Identified through known-flaky history or recent re-run pass.
    - `infra_issue`: Runner timeouts, network glitches, or connection refusals.
    - `config_error`: Missing dependencies, lock file mismatches, or env var drift.
    - `real_failure`: Genuine regressions requiring code changes.
3. **Remediation**:
    - **Rerun**: Triggers `gh run rerun` for flaky or infra issues.
    - **Fix Dispatch**: Dispatches `ci-fix-pipeline` for configuration errors or real failures.
4. **Reporting**: Generates structured per-cycle reports and emits results to the ONEX event bus.

## Gemini Advantages
- **Whole-Organization Failure Analysis**: Gemini can simultaneously identify that a "real_failure" in repo A is actually a side effect of a "config_error" in repo B.
- **Superior Log Triage**: More accurately distinguishes between transient infra noise and structural configuration errors by understanding the technical intent of the logs.
- **Intelligent Fix Orchestration**: Better at batching remediation actions to avoid redundant CI runs across multiple PRs.

## Arguments
- `--repos`: Comma-separated repo names to scan.
- `--dry-run`: Classify failures without applying fixes.
- `--max-fixes`: Hard cap on fix attempts per cycle.
