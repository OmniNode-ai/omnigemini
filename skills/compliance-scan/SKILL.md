---
name: compliance-scan
description: Gemini-native handler contract compliance scan — cross-references source code against contracts with 2M+ token grounding
capability: skill.compliance_scan
node_name: node_skill_compliance_scan_orchestrator
dot_color: 208
---

# Compliance Scan Skill (Gemini Edition)

Scan all ONEX repositories for handler contract compliance violations, leveraging Gemini's massive context window to perform deep cross-referencing between Python source code and declarative `contract.yaml` files.

## Workflow
1. **Discovery**: Gemini identifies all repositories containing ONEX nodes and handlers.
2. **Contract Audit**: Cross-references every handler's implementation against its corresponding node contract to detect:
    - **Hardcoded topics**: Topic string literals in code that are missing from the contract.
    - **Undeclared transports**: Use of DB, HTTP, or Kafka transports not declared in `transports_used`.
    - **Unregistered handlers**: Handler files not listed in `handler_routing`.
    - **Logic in node.py**: Business logic that should be moved to specialized handlers.
3. **Aggregation**: Builds a comprehensive `ModelComplianceSweepReport` with per-repo breakdowns and violation histograms.
4. **Remediation**: Optionally creates Linear tickets for non-allowlisted violations, providing specific remediation instructions.

## Gemini Advantages
- **Whole-Project Pattern Recognition**: Gemini can identify "hybrid" compliance states by seeing the relationship between multiple nodes and shared utilities.
- **Superior Violation Diagnosis**: Better at extracted the *intent* of a transport usage to determine if it truly requires a contract declaration.
- **Automated Remediation Guidance**: Generates higher-fidelity `contract.yaml` snippets for Linear tickets by analyzing the actual usage patterns in the source code.

## Arguments
- `--repos`: Comma-separated repo names to scan.
- `--create-tickets`: Create Linear tickets for violations.
- `--dry-run`: Report findings without side effects.
