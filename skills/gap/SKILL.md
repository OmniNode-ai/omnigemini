---
name: gap
description: Gemini-native cross-repo integration health audit — detect, fix, and cycle modes with 2M+ token grounding
capability: skill.gap
node_name: node_skill_gap_orchestrator
dot_color: 208
---

# Gap Skill (Gemini Edition)

Unified cross-repo integration health audit that leverages Gemini's massive context window to identify and repair architectural drift between multiple repositories in a single pass.

## Subcommands
- **detect**: Audit closed epics for Kafka topic drift, model mismatches, FK drift, API contract drift, and DB boundary violations across the entire organization.
- **fix**: Auto-fix loop for gap findings with Gemini-native decision gates.
- **cycle**: Full detect -> fix -> verify loop with artifact chaining and post-merge verification.
- **reconcile**: Trigger manual artifact reconciliation via the ONEX event bus.

## Gemini Advantages
- **Whole-Organization Drift Detection**: Gemini can simultaneously verify that a change in repository A hasn't introduced a silent contract mismatch in repository B.
- **Intelligent Probe Analysis**: Better at extracting signal from complex cross-repo boundary probes (Kafka, DB, API) by understanding the technical intent of the integration.
- **Surgical Auto-Fixes**: Generates higher-fidelity resolution code for "class-action" drift patterns by seeing the entire organization's registry.

## Arguments
- `subcommand`: detect | fix | cycle | reconcile.
- `--epic`: Linear epic ID to audit.
- `--since-days`: Look-back window for closed Epics.
- `--dry-run`: Preview changes without taking action.
- `--repo`: Limit audit to a specific repository.
