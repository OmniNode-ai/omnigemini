---
name: coverage-sweep
description: Gemini-native test coverage sweep — scans all repos for coverage gaps and auto-creates Linear tickets
capability: skill.coverage_sweep
node_name: node_skill_coverage_sweep_orchestrator
dot_color: 208
---

# Coverage Sweep Skill (Gemini Edition)

Measure test coverage across all repositories and identify modules below the target threshold, leveraging Gemini's long context to correlate coverage gaps with recent changes and system importance.

## Workflow
1. **Scan**: Executes `pytest-cov` across all Python repositories to generate structured coverage reports.
2. **Prioritization**: Gemini analyzes the reports and prioritizes gaps based on:
    - **Zero coverage**: Complete blind spots.
    - **Recent Changes**: Modules changed in the last 14 days without tests.
    - **Architectural Importance**: Core modules vs peripheral tools.
3. **Remediation**: Auto-creates Linear tickets for prioritized gaps, ensuring no duplicate tickets for the same module.
4. **Integration**: Feeds into the `refill-sprint` workflow to generate fresh tech debt items.

## Gemini Advantages
- **Intelligent Prioritization**: Goes beyond raw percentages to identify *which* gaps are most risky based on whole-project grounding.
- **Superior Ticket Content**: Generates highly relevant testing instructions by understanding the module's role in the system.
- **Cross-Repo Comparison**: Provides a unified view of testing health across the entire organization.

## Arguments
- `--target`: Coverage target percentage (default: 50).
- `--repos`: Comma-separated repo names to scan.
- `--max-tickets`: Maximum tickets to create per run.
