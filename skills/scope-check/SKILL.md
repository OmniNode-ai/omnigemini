---
name: scope-check
description: Gemini-native scope boundary extraction — extraction and confirmation of task boundaries with 2M+ token grounding
capability: skill.scope_check
node_name: node_skill_scope_check_orchestrator
dot_color: 208
---

# Scope Check Skill (Gemini Edition)

Extract and confirm scope boundaries from a plan or task description, leveraging Gemini's massive context window to ensure safety and enforcement during execution.

## Workflow
1. **Extraction**: Gemini parses the plan content to identify files, directories, repositories, and subsystems in scope.
2. **Manifest Generation**: Gemini produces a scope manifest that the scope gate hook can reference for enforcement.
3. **Presentation**: Clearly displays the extracted scope, identifying IN SCOPE, OUT OF SCOPE, and adjacent support files.
4. **Confirmation**: Allows for interactive adjustment of the scope before execution begins.
5. **Validation**: Writes the final manifest to the organization's standard path for session-wide enforcement.

## Gemini Advantages
- **Intelligent Boundary Detection**: Gemini can correctly identify "spirit vs letter" scope violations by understanding the technical intent of the task.
- **Cross-Repo Scope Analysis**: Simultaneously extract scope from multiple repositories to ensure that parallel workstreams don't collide.
- **Deep System Context**: Better at identifying adjacent files that may need modification as support by analyzing the entire codebase's dependency graph.

## Arguments
- `plan-file`: Path to the plan markdown file or task description.
- `--confirm`: Skip confirmation prompt.
- `--output`: Explicit path to write the scope manifest.
