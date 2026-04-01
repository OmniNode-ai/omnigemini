---
name: ticket-work
description: Gemini-native contract-driven ticket execution — drive a ticket from intake to merge with whole-project grounding
capability: skill.ticket_work
node_name: node_skill_ticket_work_orchestrator
dot_color: 208
---

# Ticket Work Skill (Gemini Edition)

Orchestrate ticket execution through structured phases (Intake, Research, Questions, Spec, Implement, Review), leveraging Gemini's 2M+ token window for superior research and implementation.

## Workflow
1. **Research & Questions**: Gemini analyzes the ticket against the *entire* codebase to identify requirements and ask clarifying questions.
2. **Spec Generation**: Creates a detailed implementation spec with whole-project architectural awareness.
3. **Implementation**: Gemini generates high-quality code, automatically identifying and reusing existing models, enums, and patterns.
4. **Verification**: Gemini runs tests and analyzes failures with deep context to ensure the fix is correct.
5. **Done**: Manages the PR creation and Linear ticket update.

## Gemini Advantages
- **Whole-Project Research**: Ingests all `docs/`, `src/`, and `tests/` to provide a research phase that is far more comprehensive than Claude-based search.
- **Implicit Knowledge Reuse**: Automatically finds and leverages internal APIs and patterns without needing explicit search tool calls.
- **Superior Spec Quality**: Generates implementation plans that are architecturally sound and respect system-wide invariants.

## Arguments
- `ticket_id`: Linear ticket ID (e.g., OMN-1807).
- `--autonomous`: Skip human gates and proceed through all phases unattended.
