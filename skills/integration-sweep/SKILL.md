---
name: integration-sweep
description: Gemini-native post-merge integration verification — probes all integration surfaces across repos with 2M+ token grounding
capability: skill.integration_sweep
node_name: node_skill_integration_sweep_orchestrator
dot_color: 208
---

# Integration Sweep Skill (Gemini Edition)

Contract-driven post-merge verification that leverages Gemini's massive context window to probe multiple integration surfaces (Kafka, DB, CI, Plugin, Playwright) and ensure that recently completed tickets have correctly integrated into the system.

## Workflow
1. **Ticket Discovery**: Gemini identifies recently completed tickets and extracts their `ModelTicketContract`.
2. **Surface Probing**: Executes specialized probes for each integration surface:
    - **KAFKA**: Topic constant and model compatibility.
    - **DB**: Migration alignment and ORM schema verification.
    - **CI**: Workflow existence and status check registration.
    - **CROSS_REPO**: Live boundary parity across the entire organization.
    - **PLAYWRIGHT**: Data-flow E2E smoke tests.
3. **Artifact Generation**: Assembly of a `ModelIntegrationRecord` summarizing the results.
4. **Halt Policy**: Enforces a strict halt policy for failures or missing contracts.

## Gemini Advantages
- **Whole-Project Gating**: Gemini can verify that a change in one repository hasn't broken integration surfaces in another by seeing all repo states simultaneously.
- **Intelligent Probe Selection**: More accurately identifies which surfaces need probing based on the technical intent of the ticket.
- **Superior Artifact Assembly**: Generates high-fidelity evidence summaries by correlating probe logs with contract requirements.

## Arguments
- `--date`: ISO date to sweep (defaults to today).
- `--tickets`: Explicit ticket IDs to probe.
- `--mode`: omniclaude-only | full-infra.
