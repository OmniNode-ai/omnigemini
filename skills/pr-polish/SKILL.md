---
name: pr-polish
description: Gemini-native PR polish for Track BPRs
capability: skill.pr_polish
node_name: node_skill_pr_polish_orchestrator
dot_color: 208
---

# PR Polish Skill (Gemini Edition)

This skill specializes in taking a "Track BPR" (Blocked/Broken PR), ingesting the full CI context and codebase, and applying surgical fixes using Gemini's long context window.

## Workflow
1. **Context Loading**: Ingest the PR diff, CI failure logs, and relevant source files.
2. **Diagnosis**: Gemini analyzes the failure with whole-project grounding.
3. **Execution**: Apply fixes via `replace` or `write_file`.
4. **Validation**: Run the project's validation suite.
5. **Outcome**: Push changes and report result.
