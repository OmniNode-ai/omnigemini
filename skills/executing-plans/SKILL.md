---
name: executing-plans
description: Gemini-native implementation plan execution — reviews plans, creates Linear tickets, and routes to execution with 2M+ token grounding
capability: skill.executing_plans
node_name: node_skill_executing_plans_orchestrator
dot_color: 39
---

# Executing Plans Skill (Gemini Edition)

High-fidelity execution of implementation plans that leverages Gemini's massive context window to critically review plans against the current repository state and route to the optimal execution strategy.

## Workflow
1. **Plan Review**: Gemini reads the provided plan file and identifies concerns such as missing acceptance criteria, ambiguous requirements, or unclear dependencies using whole-project grounding.
2. **PR State Verification**: Verifies the live state of any PRs referenced in the plan using `gh pr view` to ensure assumptions match reality.
3. **Linear Availability Check**: Determines whether to proceed with Linear ticket creation or fallback to local YAML ticket mode.
4. **Ticket Creation**: Calls `plan-to-tickets` to create an epic and child tickets, ensuring architecture dependency validation.
5. **Execution Routing**: Routes to `epic-team` (for multi-repo/complex tasks) or `ticket-pipeline` (for lightweight tasks) based on ticket count and technical complexity.

## Gemini Advantages
- **Whole-Project Plan Validation**: Gemini can simultaneously verify that a plan's assumptions about internal APIs and models are correct across all repositories.
- **Intelligent Routing**: More accurately determines the "blast radius" of a plan to choose between parallel team orchestration and sequential pipelines.
- **Deep Dependency Analysis**: Better at identifying hidden cross-repo dependencies that require synchronized infrastructure changes.

## Arguments
- `plan_path`: Absolute or relative path to the implementation plan.
- `--local`: Skip Linear and create local ticket YAMLs.
