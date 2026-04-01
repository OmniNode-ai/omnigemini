---
name: begin-day
description: Gemini-native morning investigation pipeline — syncs repos, checks infra, and dispatches parallel probes with 2M+ token grounding
capability: skill.begin_day
node_name: node_skill_begin_day_orchestrator
dot_color: 208
---

# Begin Day Skill (Gemini Edition)

Automated morning investigation pipeline that pairs with `/close-day` to form a daily OODA cycle, leveraging Gemini's massive context window to aggregate findings across the entire platform.

## Workflow
1. **Context Load**: Gemini loads yesterday's `close-day` corrections and computes the today/yesterday context.
2. **Sync & Preconditions**: Executes `pull-all.sh` to sync all repositories and checks organization-wide infrastructure health (Docker, Redpanda, Postgres).
3. **Parallel Investigation**: Dispatches 7 parallel Gemini-native probes to audit various system layers:
    - `list_prs`: Overnight PR and CI state across all repos.
    - `dashboard_sweep`: Holistic UI health check.
    - `aislop_sweep`: Organization-wide AI slop detection.
    - `standardization_sweep`: Python and architectural standards audit.
    - `gap_detect`: Cross-repo integration drift detection.
    - `env_parity`: Local vs cloud environment variable drift.
    - `system_status`: Platform service and node registry health.
4. **Aggregate & Model**: Gemini collects results from all probes, deduplicates findings, and builds a `ModelDayOpen` YAML artifact.
5. **Plan Generation**: Optionally feeds the findings into `design-to-plan` to generate a prioritized morning action plan.

## Gemini Advantages
- **Whole-Organization Health View**: Gemini can simultaneously analyze the results of all 7 probes to identify high-level architectural correlations that Claude-based aggregation might miss.
- **Superior Finding Deduplication**: More accurately identifies when a finding in one probe is actually a symptom of an issue found in another repo by seeing both states.
- **Context-Aware Prioritization**: Better at weighting findings by understanding their technical significance to the day's upcoming milestones.

## Arguments
- `--date`: ISO date to open (defaults to today).
- `--skip-plan`: Skip action plan generation.
- `--skip-sync`: Skip initial repository synchronization.
- `--probes`: Comma-separated list of probes to run.
