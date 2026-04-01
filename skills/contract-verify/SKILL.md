---
name: contract-verify
description: Gemini-native runtime contract compliance verification — reads contract.yaml files and verifies the running system matches declarations
capability: skill.contract_verify
node_name: node_skill_contract_verify_orchestrator
dot_color: 208
---

# Contract Verify Skill (Gemini Edition)

Runtime contract compliance verification that leverages Gemini's long context to perform deep cross-contract reference checks and validation against the running system.

## Workflow
1. **Contract Discovery**: Gemini identifies all `contract.yaml` files in the repository and builds a comprehensive map of declared nodes, handlers, and topics.
2. **Runtime Probing**: Executes the `omnibase_infra.verification` engine to verify that the running system matches the declarations.
3. **Cross-Contract Audit**: Gemini analyzes cross-contract references (e.g., node A publishing to a topic node B subscribes to) to identify inconsistencies.
4. **Remediation**: Automatically routes failures to `auto_ticket_from_findings` for Linear ticket creation.

## Gemini Advantages
- **Whole-System Grounding**: Can analyze the entire set of contracts in a repository simultaneously, spotting naming collisions or topic mismatches that per-node validators miss.
- **Intelligent Failure Analysis**: Better at diagnosing *why* a runtime check failed by correlating implementation details with contract declarations.
- **Sustained PASS Logic**: More reliably identifies when a previously failing check has truly been resolved across multiple runs.

## Arguments
- `--all`: Run the full 52-contract verification suite.
- `--registration-only`: Default fast mode for handler registration checks.
