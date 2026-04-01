---
name: compliance-sweep
description: Gemini-native handler contract compliance sweep — scans all repos for contract violations with 2M+ token grounding
capability: skill.compliance_sweep
node_name: node_skill_compliance_sweep_orchestrator
dot_color: 208
---

# Compliance Sweep Skill (Gemini Edition)

Org-wide compliance audit that scans repositories for "imperative" handlers that bypass the ONEX contract system, leveraging Gemini's massive context window for deep architectural analysis.

## Workflow
1. **Whole-Project Scan**: Gemini ingests the entire repository (contracts and handler implementations) to identify undeclared topics, hardcoded transports, or logic-in-node anti-patterns.
2. **AST-Based Analysis**: Uses Gemini's understanding of Python code structures to differentiate between real violations and false positives (e.g., in comments).
3. **Verdict Generation**: Classifies handlers as COMPLIANT, IMPERATIVE, HYBRID, or ALLOWLISTED.
4. **Remediation**: Optionally creates Linear tickets for nodes with significant compliance gaps.

## Gemini Advantages
- **Deep Contextual Audit**: Can cross-reference `contract.yaml` files against multiple handler files simultaneously to spot missing declarations.
- **Pattern Recognition**: Identifies "logic-in-node" violations by seeing the relationship between `node.py` and its handlers across the entire repo.
- **Superior Ticket Context**: Generates highly specific remediation instructions in Linear tickets by seeing the full implementation detail.

## Arguments
- `--repos`: Comma-separated repo names to scan.
- `--create-tickets`: Create Linear tickets for violations.
- `--dry-run`: Report only, no ticket creation.
