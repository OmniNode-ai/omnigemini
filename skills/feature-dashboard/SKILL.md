---
name: feature-dashboard
description: Gemini-native skill connectivity audit — scans across 8 layers and surfaces gaps with 2M+ token grounding
capability: skill.feature_dashboard
node_name: node_skill_feature_dashboard_orchestrator
dot_color: 208
---

# Feature Dashboard Skill (Gemini Edition)

Comprehensive audit of skill connectivity across the entire ONEX platform, leveraging Gemini's massive context window to identify gaps between documentation, node contracts, Kafka topics, and test coverage.

## Workflow
1. **Discovery**: Gemini identifies all skills in the `skills/` directory and their associated orchestrator nodes.
2. **Connectivity Audit**: Runs an 8-layer applicability matrix for each skill:
    - **SKILL.md**: Frontmatter and content validity.
    - **Node Existence**: Verification of the orchestrator directory.
    - **Contract Integrity**: `contract.yaml` parsing and `node_type` validation.
    - **Event Bus**: Verification of topic declarations and namespacing.
    - **Test Coverage**: Heuristic and canonical check of skill tests.
    - **Linear Integrity**: Validation of `metadata.ticket` references.
3. **Rollup**: Computes a status (wired, partial, broken, unknown) for each skill.
4. **Ticketize**: Optionally loads the audit report and auto-creates Linear tickets for gaps, using Gemini's intelligent batching to group identical issues across multiple skills.

## Gemini Advantages
- **Whole-Organization Connectivity View**: Gemini can simultaneously verify that a skill in one repo has the correctly namespaced topics declared in the organization's central registry.
- **Intelligent Gap Batching**: More accurately identifies "class-action" fixes by understanding the technical commonality between gaps in different skills.
- **Heuristic Coverage Mapping**: Better at finding existing tests for a skill by understanding the semantic relationship between skill names and test implementation details.

## Arguments
- `--mode`: audit | ticketize.
- `--format`: cli | markdown | web.
- `--filter-skill`: limit to one skill.
- `--fail-on`: broken | partial | any.
