---
name: decompose-epic
description: Gemini-native Linear epic decomposition — analyzes goals and creates atomic sub-tickets with 2M+ token grounding
capability: skill.decompose_epic
node_name: node_skill_decompose_epic_orchestrator
dot_color: 39
---

# Decompose Epic Skill (Gemini Edition)

Analyze a Linear epic and generate a set of actionable, repo-aligned sub-tickets using Gemini's massive context window to ensure perfect architectural alignment and dependency mapping.

## Workflow
1. **Epic Analysis**: Gemini fetches the epic description and goals from Linear and analyzes them against the organization's `repo_manifest.yaml`.
2. **Workstream Identification**: Identifies distinct workstreams, ensuring that each ticket is atomic (one repo, one PR, one deliverable).
3. **Ticket Generation**: Generates titles, descriptions, functional requirements, and Definition of Done (DoD) for each child ticket.
4. **Contract Generation**: Automatically generates and commits ONEX contract YAMLs for all created tickets, ensuring immediate contract coverage.
5. **Remediation**: Returns a `ModelSkillResult` with the list of created tickets for downstream orchestration by `epic-team`.

## Gemini Advantages
- **Cross-Repo Architectural Awareness**: Gemini can see the entire organization's structure to perfectly assign sub-tickets to their owning repositories.
- **Superior Decomposition Logic**: Generates higher-quality tickets with clearer boundaries, reducing the risk of integration conflicts later in the pipeline.
- **Automated Contract Alignment**: More accurately infers the necessary input/output models and topics for the new sub-tickets by seeing the whole organization's registry.

## Arguments
- `epic_id`: Linear epic ID (e.g., OMN-2000).
- `--dry-run`: Preview the decomposition plan without creating tickets.
- `--repos`: Explicit list of repos to target.
