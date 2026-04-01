---
name: close-day
description: Gemini-native end-of-day reconciliation — snapshot baselines and verify boundaries across all repos with 2M+ token grounding
capability: skill.close_day
node_name: node_skill_close_day_orchestrator
dot_color: 208
---

# Close Day Skill (Gemini Edition)

Automates the evening reconciliation loop across the entire organization, leveraging Gemini's massive context window to identify regressions and architectural drift since the morning.

## Workflow
1. **Baseline Snapshot**: Gemini triggers `check-omnidash-health` to save current dashboard metrics as a baseline.
2. **Boundary Parity**: Gemini verifies Kafka boundary parity across all repositories, identifying any unwired topics or contract mismatches.
3. **PR Collection**: Aggregates all merged PRs from today across the OmniNode-ai organization.
4. **Artifact Generation**: Gemini generates a comprehensive "Day Close" YAML artifact that summarizes the day's progress and current system health.
5. **Reconciliation**: Compares the closing state with the morning's `begin-day` baseline to flag any unexpected regressions.

## Gemini Advantages
- **Cross-Repo Health Check**: Simultaneously analyzes the state of all repositories to ensure organization-wide consistency.
- **Intelligent Drift Detection**: Better at identifying subtle architectural drift that isn't caught by simple parity checks.
- **Comprehensive Summary**: Generates a high-fidelity summary of the day's work by understanding the technical relationships between different PRs and tickets.

## Arguments
- `--date`: ISO date to close (defaults to today).
- `--skip-baseline`: Skip dashboard baseline snapshot.
- `--skip-boundary`: Skip boundary parity check.
- `--dry-run`: Report only, no artifact commitment.
