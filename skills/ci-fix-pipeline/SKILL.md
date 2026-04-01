---
name: ci-fix-pipeline
description: Gemini-native self-healing CI pipeline — autonomous fix loop with whole-project grounding
capability: skill.ci_fix_pipeline
node_name: node_skill_ci_fix_pipeline_orchestrator
dot_color: 208
---

# CI Fix Pipeline Skill (Gemini Edition)

Autonomous pipeline that fetches GitHub Actions CI failures and fixes them, leveraging Gemini's massive context window to diagnose and resolve complex, cross-module failures.

## Workflow
1. **Analysis**: Gemini ingests the full CI failure logs and the entire repository context to understand the root cause.
2. **Strategy Rotation**: Iteratively applies different fix strategies (Targeted -> Broad -> Regenerate).
3. **Execution**: Gemini applies surgical fixes across multiple files simultaneously.
4. **Validation**: Pushes changes and uses inbox-wait to detect CI re-run results.
5. **Remediation**: Creates Linear sub-tickets for large-scope or unfixable failures.

## Gemini Advantages
- **Cross-Module Diagnosis**: Correctly identifies when a failure in repo A is caused by a breaking change in a dependency from repo B.
- **Superior Log Parsing**: Better at extracting signal from noisy, multi-thousand-line CI logs.
- **High-Fidelity Fixes**: Generates code that respects the entire project's architectural invariants, reducing the need for multiple fix cycles.

## Arguments
- `--pr <number>`: PR number to fix.
- `--self-heal`: Enable the multi-attempt repair loop.
- `--analyze-only`: Diagnose failures without applying fixes.
