---
name: pr-review
description: Gemini-native comprehensive PR review — strict priority-based organization and merge readiness assessment with 2M+ token grounding
capability: skill.pr_review
node_name: node_skill_pr_review_orchestrator
dot_color: 208
---

# PR Review Skill (Gemini Edition)

Comprehensive PR review that leverages Gemini's massive context window to perform "whole-project" analysis, identifying architectural regressions and structural flaws that local diff-based reviews miss.

## Workflow
1. **Seam Contract Check**: Gemini extracts the ticket ID and verifies PR compliance against the corresponding `ModelTicketContract` before starting the main review.
2. **Multi-Endpoint Data Fetch**: Gemini pulls PR data from all 4 GitHub endpoints (comments, review comments, reviews, CI status) to ensure no feedback is missed.
3. **Claude Bot Detection**: Specifically identifies and triages feedback from other automated agents using Gemini's superior pattern recognition.
4. **Priority Classification**: Categorizes all findings into a strict priority system:
    - **CRITICAL**: Security vulnerabilities, data loss, or system crashes (BLOCKING).
    - **MAJOR**: Performance problems, incorrect behavior, or missing tests (BLOCKING).
    - **MINOR**: Code quality improvements or missing documentation (BLOCKING).
    - **NIT**: Stylistic preferences or optional refactoring (NON-BLOCKING).
5. **Merge Readiness**: Gemini provides a definitive "Ready to Merge" verdict based on the resolution of all blocking issues.

## Gemini Advantages
- **Deep Architectural Grounding**: Gemini sees the entire PR in the context of the *entire* codebase, identifying breaking changes across repository boundaries.
- **Superior Intent Matching**: More accurately determines the severity of a comment by understanding the technical intent of the reviewer and the impact on the system.
- **Whole-Project Pattern Reuse**: Automatically identifies and suggests internal APIs or models that would improve the PR's implementation.

## Arguments
- `PR_NUMBER`: GitHub PR number to review.
- `--strict`: Fail if any Critical/Major/Minor issues are found.
- `--claude-only`: Focus only on feedback from Claude-based bots.
