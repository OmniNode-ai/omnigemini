---
name: plan-to-tickets
description: Gemini-native batch ticket creation — parses plan markdown and manages Linear epics/tickets with 2M+ token grounding
capability: skill.plan_to_tickets
node_name: node_skill_plan_to_tickets_orchestrator
dot_color: 39
---

# Plan to Tickets Skill (Gemini Edition)

Batch create Linear tickets from a plan markdown file, leveraging Gemini's massive context window to ensure perfect structure detection, dependency mapping, and architectural validation.

## Workflow
1. **Structure Detection**: Gemini identifies the plan structure (Task sections, Phase sections, numbered headings) and parses it into a `ModelPlanDocument`.
2. **Anti-Pattern Enforcement**: Gemini enforces strict rules: no cross-repo tickets (without override), no duplicate IDs, no circular dependencies, and no empty content.
3. **Epic Management**: Gemini resolves or creates a parent Linear epic by analyzing the plan's title and goals.
4. **Architecture Validation**: Validates all external OMN-XXXX dependencies against organization-wide architecture rules before creation.
5. **Ticket Creation**: Creates tickets in Linear with standardized descriptions and auto-inferred `ModelTicketContract` blocks.
6. **Dependency Linking**: Automatically links tickets based on internal (`P1`, `P2`) and external (`OMN-####`) references.
7. **Post-Creation**: Triggers `generate-ticket-contract` for every ticket to ensure immediate contract coverage.

## Gemini Advantages
- **Intelligent Dependency Graphing**: Gemini can build and analyze complex dependency graphs across hundreds of tasks in a single pass.
- **Superior Contract Inference**: Better at identifying which tickets are "seams" and which interfaces are touched by analyzing the technical intent of the task description.
- **Accurate Architecture Validation**: Simultaneously verify plan dependencies against the *entire* organization's repo manifest and foundation rules.

## Arguments
- `plan-file`: Path to the plan markdown file.
- `--project`: Targeted Linear project name.
- `--repo`: Repository label for architecture validation.
- `--dry-run`: Preview tickets without taking action.
