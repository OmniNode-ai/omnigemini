---
name: refill-sprint
description: Gemini-native sprint capacity management — auto-pulls tech debt from Future into Active Sprint with 2M+ token grounding
capability: skill.refill_sprint
node_name: node_skill_refill_sprint_orchestrator
dot_color: 208
---

# Refill Sprint Skill (Gemini Edition)

Auto-pull high-value tech debt tickets from Future into Active Sprint when capacity allows, leveraging Gemini's massive context window to verify ticket scope and applicability against the current codebase.

## Workflow
1. **Capacity Check**: Gemini queries Linear for Active Sprint status and computes weighted capacity based on estimates.
2. **Candidate Selection**: Identifies tech debt candidates from the Future project using priority tiers (suppressions, friction, keywords).
3. **Scope Verification**: Gemini reads each candidate's description and cross-references it with the *entire* codebase to ensure the referenced files/APIs still exist and the DoD is applicable.
4. **Pull & Label**: Moves verified candidates to Active Sprint, adding the `auto-pulled` label and appropriate time-box constraints.
5. **Notification**: Emits `sprint.auto-pull.completed` events and sends summaries to organization-wide notification channels.

## Gemini Advantages
- **Whole-Project Scope Check**: Gemini can simultaneously verify hundreds of tech debt tickets against the latest repository states to prune stale items.
- **Intelligent Tiering**: More accurately identifies "high-impact" tech debt by understanding the architectural significance of the affected modules.
- **Accurate DoD Verification**: Better at determining if a tech debt fix is still relevant by analyzing recent changes in the referenced implementation.

## Arguments
- `--dry-run`: Preview candidates without moving tickets.
- `--threshold`: Weighted capacity threshold for triggering a pull.
- `--batch-size`: Max tickets to pull per run.
