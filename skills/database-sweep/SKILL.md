---
name: database-sweep
description: Gemini-native projection table health and migration tracking — audits all ONEX databases with 2M+ token grounding
capability: skill.database_sweep
node_name: node_skill_database_sweep_orchestrator
dot_color: 208
---

# Database Sweep Skill (Gemini Edition)

Projection table health check and migration tracking across all ONEX databases, leveraging Gemini's massive context window to correlate schema definitions with runtime state and identify drift.

## Workflow
1. **Table Discovery**: Gemini cross-references `pg_tables` with Drizzle schema definitions in `omnidash` to identify expected vs actual tables.
2. **Health Check**: Audits each table for row count, staleness, and timestamp column existence.
3. **Migration Tracking**: Verifies migration state (Alembic/Drizzle) across all ONEX databases, comparing on-disk files with applied head positions.
4. **Schema Fingerprinting**: Captures and hash-compares sorted column definitions to detect manual schema drift not captured by migrations.
5. **Remediation**: Auto-creates Linear tickets for stale tables, pending migrations, or failed states.

## Gemini Advantages
- **Whole-Project Schema View**: Gemini can simultaneously analyze Drizzle schemas in TypeScript and Alembic migrations in Python to ensure system-wide consistency.
- **Intelligent Staleness Triage**: Better at identifying *why* a table is stale by understanding the technical relationship between the upstream Kafka topic and the projection handler.
- **Accurate Fingerprinting**: More reliably identifies structural changes by understanding the semantic meaning of column types and nullability constraints.

## Arguments
- `--dry-run`: Report findings without creating tickets.
- `--table`: Check a single table only.
- `--staleness-threshold`: Hours before data is considered stale.
