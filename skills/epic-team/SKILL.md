---
name: epic-team
description: Gemini-native multi-repo epic orchestration — autonomously drive a Linear epic across multiple repositories with 2M+ token grounding
capability: skill.epic_team
node_name: node_skill_epic_team_orchestrator
dot_color: 39
---

# Epic Team Skill (Gemini Edition)

High-level orchestrator that drives an entire Linear epic to completion across multiple repositories, leveraging Gemini's massive context window for superior dependency management and progress tracking.

## Workflow
1. **Decompose**: Gemini analyzes the epic and existing codebases across all relevant repos to create or refine sub-tickets.
2. **Wave Planning**: Group tickets into dependency-aware waves. Gemini's long context ensures accurate cross-repo dependency mapping.
3. **Dispatch**: Dispatch workers (via `ticket-pipeline`) to implement each ticket.
4. **Monitor**: Gemini monitors the entire epic's progress, identifying stalls or integration issues across the whole project.
5. **Finalize**: Run DoD sweeps and mark the epic as complete.

## Gemini Advantages
- **Cross-Repo Context**: Gemini sees all repositories simultaneously, allowing it to spot integration conflicts that Claude-based orchestration might miss.
- **Superior Decomposition**: Higher quality sub-tickets with clearer boundaries and better-defined contracts.
- **Holistic Monitoring**: Gemini maintains a "God-eye view" of the entire epic run, accurately correlating events across multiple streams.

## Arguments
- `epic_id`: Linear epic ID (e.g., OMN-2000).
- `--mode build`: Required for epic execution.
- `--dry-run`: Preview waves and decomposition without starting work.
- `--resume`: Continue from a previous checkpoint.
