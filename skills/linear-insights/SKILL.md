---
name: linear-insights
description: Gemini-native platform analytics and reporting — generates deep dives and velocity estimates with 2M+ token grounding
capability: skill.linear_insights
node_name: node_skill_linear_insights_orchestrator
dot_color: 39
---

# Linear Insights Skill (Gemini Edition)

Unified analytics and reporting for the ONEX platform, leveraging Gemini's long context to perform comprehensive daily work analysis, velocity-based completion estimates, and project health monitoring.

## Workflow
1. **Reporting Mode Selection**: Supports multiple sub-modes: `deep-dive`, `close-day`, `project`, `velocity`, `suggest`, `pipeline`, and `github`.
2. **Data Aggregation**: Gemini pulls data from Linear, GitHub, and local git history across the entire organization.
3. **Deep Dive Analysis**: Generates a high-fidelity summary of work completed, classifying PRs by impact and significance.
4. **Velocity Estimation**: Calculates project velocity using a weighted rolling average and estimates milestone ETAs with confidence intervals.
5. **Kafka Emission**: Optionally relays workstream snapshots to the ONEX event bus via `onex-linear-relay`.

## Gemini Advantages
- **Cross-Repo Productivity Analysis**: Gemini sees the entire organization's activity, allowing it to correlate a fix in one repository with a feature launch in another.
- **Superior Semantic Classification**: More accurately classifies work into "feature" vs "fix" by understanding the technical intent of the PRs and commits.
- **Context-Rich Project Health**: Provides a more nuanced assessment of project risks and blockers by analyzing the relationship between various technical challenges across the codebase.

## Arguments
- `--mode`: deep-dive | close-day | project | velocity | suggest | pipeline | github | all.
- `--project`: Targeted Linear project name.
- `--date`: Target date for reporting.
- `--emit`: Relay snapshot to Kafka.
