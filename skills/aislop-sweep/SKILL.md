---
name: aislop-sweep
description: Gemini-native AI slop detection — scans all repos for AI-generated anti-patterns with 2M+ token grounding
capability: skill.aislop_sweep
node_name: node_skill_aislop_sweep_orchestrator
dot_color: 208
---

# AI Slop Sweep Skill (Gemini Edition)

Detects AI-generated quality anti-patterns across all repositories, leveraging Gemini's massive context window to identify structural inconsistencies and violations of ONEX platform invariants.

## Workflow
1. **Whole-Project Scan**: Gemini ingests code across all repositories to identify "slop" patterns: phantom callables, backwards compat shims, prohibited env vars, agent-left TODOs, and empty implementations.
2. **Triage**: Categorizes findings by severity (CRITICAL, ERROR, WARNING, INFO) and confidence.
3. **Remediation**: Optionally creates Linear tickets or attempts auto-fixes for trivial patterns.
4. **Summary**: Reports sweep results to Slack and the event bus.

## Gemini Advantages
- **Deep Pattern Matching**: Recognizes subtle AI anti-patterns that simple regex-based scanners miss.
- **Context-Aware Validation**: Confirms "phantom callables" by checking the entire workspace for the existence of the referenced functions.
- **Intelligent Triage**: More accurately determines the severity of a finding by understanding its impact on the broader system architecture.

## Arguments
- `--repos`: Comma-separated repo names to scan.
- `--checks`: Comma-separated pattern categories to scan for.
- `--ticket`: Create Linear tickets for findings.
- `--auto-fix`: Attempt auto-fix for trivial patterns.
