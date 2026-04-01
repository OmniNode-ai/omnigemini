---
name: design-to-plan
description: Gemini-native design workflow — brainstorm ideas and generate structured implementation plans with 2M+ token grounding
capability: skill.design_to_plan
node_name: node_skill_design_to_plan_orchestrator
dot_color: 39
---

# Design to Plan Skill (Gemini Edition)

End-to-end design and planning workflow that leverages Gemini's massive context window for whole-project architectural grounding.

## Workflow
1. **Brainstorm**: Gemini ingests the entire codebase context to provide architectural advice, identify existing patterns, and propose trade-offs for a new feature.
2. **Plan**: Generate a structured implementation plan (`## Task N:` format) with "Known Types Inventory" automatically populated from the entire repository.
3. **Adversarial Review**: Run Gemini-native R1-R7 checks against the plan to ensure technical integrity and adherence to standards.
4. **Launch**: Route to execution via `executing-plans`.

## Gemini Advantages
- **Whole-Project Grounding**: Unlike Claude-based design which is limited by context fragments, Gemini sees the entire `src/`, `docs/`, and `tests/` simultaneously.
- **Deep Pattern Matching**: Automatically identifies and reuses existing Pydantic models and Enums across the entire workspace.
- **Complex Dependency Mapping**: Accurately maps cross-module dependencies for large-scale refactors.

## Arguments
- `--topic`: Topic or problem to brainstorm.
- `--plan-path`: Path to an existing plan file to review or launch.
- `--no-launch`: Stop after generating the plan.
