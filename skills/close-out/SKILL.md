---
name: close-out
description: Gemini-native end-of-day close-out pipeline — ordered PR merging, release, and redeploy with whole-project grounding
capability: skill.close_out
node_name: node_skill_close_out_orchestrator
dot_color: 208
---

# Close Out Skill (Gemini Edition)

End-of-day close-out pipeline that leverages Gemini's long context to orchestrate ordered PR merging, dependency-aware releases, and runtime refreshes across the entire organization.

## Workflow
1. **Merge Sweep**: Gemini invokes `merge-sweep` across all active repositories in parallel to drain open PRs with passing CI.
2. **Integration Sweep**: Executes `integration-sweep` as a **HARD GATE**; any FAIL or contract UNKNOWN halts the pipeline.
3. **Release**: Gemini orchestrates releases in dependency-tier order (core -> spi -> infra -> others), verifying each publish before proceeding.
4. **Redeploy**: Refreshes the runtime with new versions, syncing bare clones and rebuilding Docker services.
5. **Verification**: Confirms PR status, release tags, and runtime health, generating a comprehensive daily close-out summary.

## Gemini Advantages
- **Cross-Repo Release Ordering**: Gemini perfectly maps the organization's dependency graph to ensure releases happen in the correct sequence without manual guidance.
- **Superior Diagnosis**: If halted at the integration gate, Gemini generates a high-fidelity diagnosis document by analyzing the entire day's technical history.
- **Holistic Verification**: Better at correlating PR merges with release tags and container health to provide 100% confidence in the system's terminal state.

## Arguments
- `--dry-run`: Preview close-out steps without taking action.
- `--skip-release`: Skip the release and redeploy phases.
