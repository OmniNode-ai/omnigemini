---
name: tech-debt-sweep
description: Gemini-native tech debt audit — scans all Python repos for debt patterns and manages Linear tickets/epics
capability: skill.tech_debt_sweep
node_name: node_skill_tech_debt_sweep_orchestrator
dot_color: 208
---

# Tech Debt Sweep Skill (Gemini Edition)

Comprehensive tech debt audit that leverages Gemini's long context to identify and prioritize maintenance work across the entire Python codebase.

## Workflow
1. **Pattern Detection**: Gemini scans all Python repositories for six categories of debt: `type-ignore`, `noqa`, `todo-fixme`, `any-types`, `skipped-tests`, and `stale-ignores`.
2. **Deduplication**: Gemini intelligently deduplicates findings against existing open Linear tickets by analyzing the technical intent of the debt.
3. **Grouping**: Automatically groups findings into epics by category, with closeable tickets grouped by repo and top-level directory.
4. **Remediation**: Generates tickets with category-specific remediation guidance derived from whole-project grounding.

## Gemini Advantages
- **Deep Pattern Context**: Gemini can differentiate between a "safe" type ignore and a "high-risk" ignore that masks a protocol mismatch.
- **Intelligent Grouping**: Better at batching findings into logical, closeable work items by understanding the architectural boundaries of the directories being scanned.
- **Stale Ignore Identification**: Leverages long context to identify `type: ignore` comments that are no longer necessary, providing "free" cleanup opportunities.

## Arguments
- `--repo`: Scan a single repo only.
- `--categories`: Comma-separated category filter.
- `--dry_run`: Report findings without creating tickets.
