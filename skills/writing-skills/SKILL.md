---
name: writing-skills
description: Gemini-native skill development — applies TDD to process documentation with whole-project grounding
capability: skill.writing_skills
node_name: node_skill_writing_skills_orchestrator
dot_color: 39
---

# Writing Skills Skill (Gemini Edition)

High-fidelity skill development using Gemini's massive context window to ensure documentation is accurate, searchable, and respects organization-wide standards.

## Workflow
1. **Red (Failing Test)**: Gemini creates pressure scenarios and identifies baseline failures without the skill.
2. **Green (Minimal Skill)**: Generates a thin Markdown shell (`SKILL.md`) that addresses the specific failures.
3. **Refactor (Loophole Closing)**: Gemini identifies potential rationalizations and adds explicit counters to the documentation.
4. **Validation**: Gemini verifies that subagents correctly follow the new skill under pressure.

## Gemini Advantages
- **Whole-Project Discovery**: Gemini's 2M+ token window ensures that new skills don't duplicate existing knowledge and are correctly cross-referenced.
- **Superior CSO (Claude Search Optimization)**: Generates highly effective description fields and keywords by understanding how the entire organization's skill registry is searched.
- **Bulletproof Logic**: Gemini is better at finding subtle "spirit vs letter" loopholes in process documentation.

## Guidelines
- **Thin Shell Architecture**: Skills in Gemini are thin wrappers over node-based logic.
- **Context Efficiency**: Keep documentation concise and focused on triggering symptoms.
- **Polly-Dispatch**: Always use polymorphic agents for the actual implementation work.
