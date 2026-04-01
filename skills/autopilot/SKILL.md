---
name: autopilot
description: Gemini-native autonomous close-out orchestrator — 20-step pipeline with whole-project grounding and hard gates
capability: skill.autopilot
node_name: node_skill_autopilot_orchestrator
dot_color: 208
---

# Autopilot Skill (Gemini Edition)

Top-level autonomous orchestrator that drives the entire ONEX platform through a comprehensive 4-phase pipeline (Prepare, Quality Gate, Ship, Verify), leveraging Gemini's massive context window for superior multi-repo coordination and safety enforcement.

## Workflow
1. **Phase A (Prepare)**: Gemini orchestrates worktree health sweeps, organization-wide merge sweeps (via `merge-sweep`), and infrastructure startup with auto-fix.
2. **Phase B (Quality Gate)**: Dispatches parallel Gemini-native quality sweeps (DoD, AI slop, Kafka, Gap) and enforces a **HARD GATE** on integration and Playwright behavioral verification.
3. **Phase C (Ship)**: Manages version bumping, releases (via `release`), and runtime refreshes (via `redeploy`) in dependency-tier order.
4. **Phase D (Verify)**: Gemini performs post-release verification across all services, ensuring container health, plugin deployment, and dashboard functionality.
5. **Circuit Breaker**: Enforces a strict halt policy for consecutive failures or integration brokenness.

## Gemini Advantages
- **Whole-Pipeline Grounding**: Gemini can simultaneously monitor all 20 steps of the pipeline, identifying cross-phase regressions that sequential Claude-based runs miss.
- **Superior Gate Logic**: Better at extracts the technical significance of a quality sweep finding to determine if it truly warrants a pipeline halt.
- **Intelligent Recovery**: More effective at auto-fixing infrastructure startup failures by understanding the relationship between multiple system components.

## Arguments
- `--mode`: build | close-out.
- `--autonomous`: Skip human gates (default: true).
- `--require-gate`: Opt into a Slack HIGH_RISK gate before release.
