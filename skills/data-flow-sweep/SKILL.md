---
name: data-flow-sweep
description: Gemini-native end-to-end data flow verification — audits the entire pipeline from producer to dashboard with 2M+ token grounding
capability: skill.data_flow_sweep
node_name: node_skill_data_flow_sweep_orchestrator
dot_color: 208
---

# Data Flow Sweep Skill (Gemini Edition)

End-to-end data flow verification for all omnidash projections, leveraging Gemini's massive context window to trace data from its source emission through Redpanda and the consumer into the final dashboard display.

## Workflow
1. **Topic Discovery**: Gemini maps all `read_model_topics` from `topics.yaml` to their projection files, DB tables, and dashboard routes.
2. **Producer Verification**: Checks if upstream producers (omniclaude, omnibase_infra, etc.) are actively emitting messages to Redpanda.
3. **Consumer + DB Verification**: Audits consumer group lag and verifies that DB tables are receiving and persisting fresh data.
4. **Dashboard Page Verification**: Optionally uses Playwright to navigate to dashboard routes and ensure data renders correctly without JS errors.
5. **Remediation**: Auto-creates Linear tickets for broken flows, identifying the exact point of failure (Producer, Topic, Consumer, DB, or Page).

## Gemini Advantages
- **Full-Stack Traceability**: Gemini sees the entire pipeline from Python producers to TypeScript/Playwright consumers, identifying bottlenecks that local audits miss.
- **Intelligent Lag Analysis**: Better at distinguishing between transient lag and structural consumer stalls by analyzing the complexity of the projection logic.
- **Cross-Repo Correlation**: Correctly identifies when a broken dashboard page is caused by a contract change in a distant producer repository.

## Arguments
- `--dry-run`: Report findings without creating tickets.
- `--topic`: Check a single topic only.
- `--skip-playwright`: Skip dashboard page verification.
