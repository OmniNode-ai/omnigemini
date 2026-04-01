---
name: handoff
description: Gemini-native session continuity — save and inject high-fidelity context across sessions with 2M+ token grounding
capability: skill.handoff
node_name: node_skill_handoff_orchestrator
dot_color: 39
---

# Handoff Skill (Gemini Edition)

Provides high-fidelity session continuity by capturing and injecting comprehensive context across sessions, leveraging Gemini's long context to ensure no technical detail is lost during transitions.

## Workflow
1. **Context Capture**: `/handoff` captures the active ticket, branch, recent commits, working files, and Gemini's current "mental model" of the task.
2. **Manifest Generation**: Writes a multi-repo context manifest to the `onex_state` directory.
3. **Session Injection**: On the next session start, Gemini automatically ingests the most recent manifest for the current workspace.
4. **Seamless Resumption**: Gemini uses the injected context to immediately resume work without needing a new research phase.

## Gemini Advantages
- **Whole-Task Memory**: Unlike simple message-based handoffs, Gemini can preserve its understanding of the entire project's architectural state.
- **Intelligent Context Merging**: Better at merging auto-checkpoints with explicit handoff messages to provide a more complete picture of the work-in-progress.
- **Zero-Research Resumption**: Drastically reduces the "warm-up" time for new sessions by providing a 100% accurate snapshot of the previous session's state.

## Arguments
- `--message`: Optional message for the next session (free text context).
