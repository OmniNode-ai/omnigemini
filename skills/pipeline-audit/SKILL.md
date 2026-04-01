---
name: pipeline-audit
description: Gemini-native end-to-end multi-repo pipeline audit — system-wide integration verification with 2M+ token grounding
capability: skill.pipeline_audit
node_name: node_skill_pipeline_audit_orchestrator
dot_color: 208
---

# Pipeline Audit Skill (Gemini Edition)

Systematically audit an end-to-end multi-repo pipeline for integration correctness, leveraging Gemini's massive context window to prove every join between services with file-level evidence.

## Workflow
1. **Repository Discovery**: Gemini identifies every repository participating in the pipeline and analyzes its purpose.
2. **Capability Inventory**: Dispatches parallel Gemini-native agents to build structured maps of integration surfaces (Kafka, DB, API, Config) per repo.
3. **Pipeline Trace**: Gemini constructs an end-to-end pipeline trace, mapping narrative flows to exact wire formats.
4. **Hard Assertions**: Proves integration correctness across six categories:
    - **Runtime Entrypoint**: Verification that services actually start and reach integration code.
    - **DSN Proof**: Confirmation that all repos connect to the same database/schema.
    - **Wire Topics**: Byte-for-byte matching of producer and consumer topic strings.
    - **Schema Handshake**: Agreement on table schemas across writers, readers, and dashboards.
    - **Wire Format Compatibility**: Compatibility verification of message serialization/deserialization.
    - **Correlation ID Threading**: Tracing of identifier propagation through every stage.
5. **Gap Register**: Compiles all findings into a severity-ordered list of integration issues.
6. **Ticket Creation**: Auto-creates Linear tickets for identified gaps with exact code references and remediation guidance.

## Gemini Advantages
- **Whole-Pipeline Grounding**: Gemini can simultaneously verify that a producer in repo A matches a consumer in repo B across Kafka, DB, and API boundaries.
- **Superior Pattern Context**: Better at identifying "broken links" in the correlation chain by understanding the technical intent of the tracing identifiers.
- **Context-Aware Schema Audit**: More accurately identifies breaking changes in message models by seeing the entire organization's Pydantic config.

## Arguments
- `PIPELINE_NAME`: Name of the pipeline to audit.
- `--all`: Run all 6 proof categories.
- `--dry-run`: Preview findings without creating tickets.
