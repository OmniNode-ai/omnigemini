---
name: systematic-debugging
description: Gemini-native five-phase debugging framework — backward tracing and root cause investigation with 2M+ token grounding
capability: skill.systematic_debugging
node_name: node_skill_systematic_debugging_orchestrator
dot_color: 208
---

# Systematic Debugging Skill (Gemini Edition)

Standardized five-phase framework for encountering bugs, test failures, or unexpected behavior, leveraging Gemini's massive context window to ensure full understanding before attempting fixes.

## Workflow
1. **Backward Tracing**: Gemini traces backward through the call chain to identify the original trigger, leveraging whole-project grounding to understand complex stack traces.
2. **Root Cause Investigation**: Reproduces the symptom consistently and gathers evidence across multi-component systems to identify the exact point of failure.
3. **Pattern Analysis**: Gemini identifies working examples and compares them against the broken code to find subtle differences in implementation or dependencies.
4. **Hypothesis & Testing**: Forms a single, specific hypothesis and tests it minimally to confirm understanding without adding redundant changes.
5. **Implementation**: Gemini creates a failing test case (via `test-discipline`) and implements a surgical fix addressed at the root cause.

## Gemini Advantages
- **Whole-Project Stack Analysis**: Gemini can simultaneously analyze source code, tests, and configuration files to trace a bug's origin across multiple repositories.
- **Superior Pattern Matching**: Better at finding "what works" elsewhere in the organization's registry to apply consistent fixes.
- **Implicit Knowledge Reuse**: Automatically extracts architectural invariants from the entire project to ensure the fix is idiomatically complete.

## Arguments
- `PROMPT`: Natural language description of the bug or failure.
- `--analyze-only`: Perform investigation without applying fixes.
