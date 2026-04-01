---
name: runtime-sweep
description: Gemini-native runtime wiring verification — audits node descriptions, handler wiring, and topic symmetry with 2M+ token grounding
capability: skill.runtime_sweep
node_name: node_skill_runtime_sweep_orchestrator
dot_color: 208
---

# Runtime Sweep Skill (Gemini Edition)

Comprehensive runtime registration and wiring verification that leverages Gemini's long context to ensure that all ONEX nodes and topics are correctly declared and connected across the entire ecosystem.

## Workflow
1. **Description Audit**: Gemini scans all `contract.yaml` files to identify placeholder or missing node descriptions.
2. **Wiring Audit**: Verifies that every declared handler is actually wired in the dispatch engine (e.g., `read-model-consumer.ts` in `omnidash`).
3. **Topic Symmetry**: Identifies `PRODUCER_ONLY` or `CONSUMER_ONLY` topics by analyzing the entire organization's contract registry.
4. **Log Analysis**: Scans Docker container logs for repeated error patterns and correlates them with service health.
5. **Remediation**: Auto-creates Linear tickets for unwired handlers, asymmetric topics, or error-heavy containers.

## Gemini Advantages
- **Holistic Wiring View**: Gemini sees the entire graph of producers and consumers across all repositories, identifying "broken links" that local audits miss.
- **Intelligent Log Correlation**: Better at distinguishing between transient noise and repeated architectural errors in container logs.
- **System-Wide Symmetry**: Correctly identifies when a topic is "unwired" globally by seeing both the producer and consumer repositories simultaneously.

## Arguments
- `--dry-run`: Report findings without creating tickets.
- `--scope`: omnidash-only | all-repos.
