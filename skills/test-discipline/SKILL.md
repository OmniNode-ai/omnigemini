---
name: test-discipline
description: Gemini-native unified testing methodology — TDD red-green-refactor cycle and anti-pattern detection with 2M+ token grounding
capability: skill.test_discipline
node_name: node_skill_test_discipline_orchestrator
dot_color: 208
---

# Test Discipline Skill (Gemini Edition)

Unified testing methodology that leverages Gemini's massive context window to enforce TDD discipline and detect sophisticated testing anti-patterns across the entire project.

## Workflow
1. **TDD Mode**: Gemini orchestrates the red-green-refactor cycle, ensuring no production code is written without a failing test first.
2. ** Anti-Pattern Audit**: Gemini scans existing and new tests for anti-patterns:
    - **A1**: Asserting on mock elements instead of real behavior.
    - **A2**: Test-only methods in production classes.
    - **A3**: Mocking without understanding the dependency chain.
    - **A4**: Incomplete or "partial" mocks that hide structural assumptions.
3. **Completion Gate**: Enforces a strict evidence-before-assertion policy, requiring full command output confirmation before work is marked complete.

## Gemini Advantages
- **Deep Anti-Pattern Recognition**: Gemini can identify subtle over-mocking or implementation-biased tests by seeing the relationship between source code and tests simultaneously.
- **Intelligent Gate Verification**: Better at parsing complex test outputs to confirm that a "PASS" truly addresses the requirement.
- **Whole-Project Coverage Audit**: Simultaneously analyzes the entire test suite to ensure that new tests adhere to organization-wide discipline standards.

## Arguments
- `--mode`: tdd | audit | full.
