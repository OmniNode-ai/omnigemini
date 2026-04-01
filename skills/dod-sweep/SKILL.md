---
name: dod-sweep
description: Gemini-native Definition of Done compliance sweep — retroactive batch audit or targeted pre-close gate
capability: skill.dod_sweep
node_name: node_skill_dod_sweep_orchestrator
dot_color: 208
---

# DoD Compliance Sweep Skill (Gemini Edition)

Validate Definition of Done (DoD) compliance across closed epics and tickets, leveraging Gemini's long context to verify evidence across multiple repositories and event streams.

## Workflow
1. **Discovery**: Identify recently completed tickets (Batch mode) or expand a specific epic (Targeted mode).
2. **Evidence Verification**: Gemini cross-references:
    - **Primary Checks**: Contract existence, evidence receipts, and receipt cleanliness.
    - **Supporting Checks**: Merged PRs, green CI status, and integration sweep evidence.
3. **Verdict Matrix**: Categorizes results into ALLOW (CLEAN/WARNING/FOLLOW-UP) or BLOCK.
4. **Remediation**: Updates or creates Linear follow-up tickets for identified gaps.

## Gemini Advantages
- **Cross-Repo Traceability**: Gemini can trace a ticket ID through PRs, CI logs, and integration artifacts across multiple repositories in a single pass.
- **Intelligent Linkage**: Better at resolving "UNKNOWN" states where naming mismatches or branch drift might confuse standard regex-based tools.
- **Holistic Gating**: Provides a more nuanced "Gate Decision" by understanding the intent behind the ticket and the completeness of the evidence.

## Arguments
- `target`: Optional OMN-XXXX epic/ticket ID for targeted mode.
- `--since-days`: Look-back window for batch mode.
- `--dry-run`: Report only, no follow-up tickets.
