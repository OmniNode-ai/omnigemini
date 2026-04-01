---
name: ticket-pipeline
description: Gemini-native autonomous per-ticket pipeline — implement, review, test, and merge with 2M+ token grounding
capability: skill.ticket_pipeline
node_name: node_skill_ticket_pipeline_orchestrator
dot_color: 39
---

# Ticket Pipeline Skill (Gemini Edition)

Autonomous per-ticket pipeline that chains implementation, review, testing, and merging into a single unattended workflow, leveraging Gemini's massive context window for superior technical execution.

## Workflow
1. **Pre-flight**: Gemini analyzes the ticket and repository context to generate a robust implementation contract.
2. **Implement**: Gemini generates high-quality initial code based on the contract and whole-project grounding.
3. **Local Review**: Iterative review and fix loop with Gemini's deep pattern matching.
4. **Test & Iterate**: Autonomous test-fix-rerun cycle. Gemini uses the full CI log and project context to solve complex failures.
5. **PR & Merge**: Create PR, watch CI, and auto-merge upon approval.

## Gemini Advantages
- **Superior Diagnosis**: Gemini's long context allows it to understand complex cross-module bug reports and generate more accurate contracts.
- **Context-Aware Implementation**: Avoids "hallucinated" APIs by seeing the entire available toolset.
- **Faster Test Iteration**: Correctly identifies the root cause of failures by analyzing the relationship between source code, tests, and configuration files simultaneously.

## Arguments
- `ticket_id`: Linear ticket ID (e.g., OMN-1804).
- `--skip-to`: Resume from a specific phase.
- `--dry-run`: Preview changes without commits or PRs.
