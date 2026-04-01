---
name: ultimate-validate
description: Gemini-native comprehensive codebase validation — generates high-fidelity validation commands with whole-project grounding
capability: skill.ultimate_validate
node_name: node_skill_ultimate_validate_orchestrator
dot_color: 39
---

# Ultimate Validate Skill (Gemini Edition)

Analyze the entire codebase deeply and generate a comprehensive validation command that leaves no stone unturned, leveraging Gemini's massive context window to understand real user workflows and external integrations.

## Workflow
1. **Workflow Discovery**: Gemini reads documentation (README, CLAUDE.md, docs/) to understand actual user journeys and external integrations (CLIs, APIs).
2. **Deep Codebase Analysis**: Explores the entire project to identify linting, type-checking, style, and testing configurations.
3. **End-to-End Mapping**: Gemini maps complete user workflows to E2E test scenarios, ensuring that validation mirrors actual production usage.
4. **Command Generation**: Creates or updates `.gemini/commands/validate.md` with multi-phase validation (Lint, Type, Style, Unit, E2E).
5. **Creativity & Comprehensiveness**: Gemini identifies subtle error cases and database integrity checks that standard test generators miss.

## Gemini Advantages
- **Deep Workflow Grounding**: Gemini can resolve complex user journeys that span multiple repositories and external platforms.
- **Superior Test Heuristics**: Better at identifying "material" validation gaps by understanding the architectural significance of various modules.
- **Whole-Project Integration Check**: Simultaneously analyze internal APIs and external platform dependencies to ensure 100% confidence in production readiness.

## Arguments
- `--force`: Regenerate the validation command even if it exists.
- `--dry-run`: Preview the generated command without writing to disk.
