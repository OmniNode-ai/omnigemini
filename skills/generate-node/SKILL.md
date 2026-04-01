---
name: generate-node
description: Gemini-native ONEX node generation — generates production-ready nodes with whole-project grounding
capability: skill.generate_node
node_name: node_skill_generate_node_orchestrator
dot_color: 39
---

# Generate Node Skill (Gemini Edition)

Fully automated ONEX node generation that leverages Gemini's massive context window to ensure new nodes are perfectly integrated with existing patterns, contracts, and models.

## Workflow
1. **Inference**: Gemini analyzes the generation prompt against the *entire* codebase to infer the optimal contract, input/output models, and node type.
2. **Template Expansion**: Generates the infrastructure boilerplate using existing Jinja2 templates.
3. **Logic Generation**: Gemini generates the complete business logic, automatically identifying and reusing existing internal APIs.
4. **Validation**: Runs generated tests and quality checks to ensure ONEX v2.0 compliance.

## Gemini Advantages
- **Perfect Pattern Matching**: New nodes automatically adopt the specific architectural style of the surrounding modules without manual guidance.
- **Superior Contract Accuracy**: Gemini correctly identifies the necessary Kafka topics and Pydantic models by seeing the whole organization's registry.
- **High-Fidelity Tests**: Generates comprehensive unit tests that cover realistic edge cases derived from the project's actual usage patterns.

## Arguments
- `PROMPT`: Natural language description of the node.
- `--output-dir`: Output directory for generated files.
- `--node-type`: Hint for the node type (effect, compute, reducer, orchestrator).
- `--enable-quorum`: Use multi-model validation for the generated code.
