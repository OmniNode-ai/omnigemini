---
name: linear-triage
description: Gemini-native ticket health and PR verification — syncs Linear status with GitHub state across repos with 2M+ token grounding
capability: skill.linear_triage
node_name: node_skill_linear_triage_orchestrator
dot_color: 39
---

# Linear Triage Skill (Gemini Edition)

Comprehensive ticket health assessment that leverages Gemini's massive context window to verify Linear ticket status against live GitHub PR state across the entire organization.

## Workflow
1. **Fetch**: Gemini retrieves all non-completed tickets from Linear across all projects.
2. **Age Classification**: Categorizes tickets into RECENT and STALE based on update history.
3. **PR Verification**: For recent tickets, Gemini extracts the repository slug and searches all organization repos for matching PRs (open or merged).
4. **Action Determination**: Automatically marks tickets as DONE (if PR merged), DONE_SUPERSEDED (if sibling PR found), or flags them as STALE.
5. **Orphan & Epic Detection**: Identifies orphans needing epic assignment and auto-closes epics when all child tickets are completed.
6. **Reporting**: Generates a comprehensive `TriageReport` YAML artifact and human-readable summary.

## Gemini Advantages
- **Cross-Repo PR Search**: Gemini can simultaneously search all organization repositories to find superseded or sibling PRs that simple single-repo lookups miss.
- **Intelligent Repo Extraction**: Better at identifying the target repository from ambiguous branch names or title prefixes by analyzing common naming patterns.
- **Holistic Epic Completion**: More accurately determines if an epic is truly "Done" by understanding the technical relationship between its child tickets and their integration artifacts.

## Arguments
- `--threshold-days`: Definition of "recent" for PR verification.
- `--dry-run`: Assess and report without modifying Linear.
