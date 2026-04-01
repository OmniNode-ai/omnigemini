---
name: duplication-sweep
description: Gemini-native structural collision detection — scans all repos for duplicate definitions with 2M+ token grounding
capability: skill.duplication_sweep
node_name: node_skill_duplication_sweep_orchestrator
dot_color: 208
---

# Duplication Sweep Skill (Gemini Edition)

Lightweight structural scan that leverages Gemini's massive context window to identify colliding definitions across the entire organization, including Drizzle tables, Kafka topics, and Python models.

## Workflow
1. **Multi-Repo Scan**: Gemini ingests code across all repositories to identify potential collision classes.
2. **Structural Checks**:
    - **D1 (Database)**: Detects duplicate Drizzle table definitions across schema files.
    - **D2 (Events)**: Identifies conflicting producer claims for the same Kafka topic.
    - **D3 (Migrations)**: Detects duplicate migration prefixes.
    - **D4 (Models)**: Gemini performs a "whole-project" analysis to find cross-repo model name collisions outside of `omnibase_core`.
3. **Verdict Generation**: Categorizes findings into PASS, WARN, or FAIL based on structural risk.
4. **Integration**: Findings are fed into the autopilot system for automated halt decisions.

## Gemini Advantages
- **Whole-Project Model Mapping**: Unlike simple grep-based checks, Gemini can understand the relationship between models in different repositories and distinguish between intentional sharing and accidental collisions.
- **Intelligent Deduplication**: Better at identifying when a "duplicate" is actually a re-implementation or a legitimate cross-repo reference.
- **Accurate Risk Assessment**: More reliably determines if a collision occurs in a production codepath vs a test or fixture.

## Arguments
- `--check D1,D2`: Comma-separated check IDs to run.
- `--json`: Output machine-readable results.
