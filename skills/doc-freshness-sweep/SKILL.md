---
name: doc-freshness-sweep
description: Gemini-native documentation freshness sweep — scans for broken references and stale content with 2M+ token grounding
capability: skill.doc_freshness_sweep
node_name: node_skill_doc_freshness_sweep_orchestrator
dot_color: 208
---

# Doc Freshness Sweep Skill (Gemini Edition)

Scan all documentation across the ONEX platform for broken references, stale content, and CLAUDE.md inaccuracy, leveraging Gemini's massive context window to resolve cross-repo links and verify instruction validity.

## Workflow
1. **Discovery**: Gemini identifies all `.md` files and extracts code references (paths, functions, commands, URLs).
2. **Reference Resolution**: Gemini cross-references every link against the *entire* codebase to ensure the targets still exist.
3. **Staleness Detection**: Compares document modification dates against referenced code changes using `git log` grounding.
4. **CLAUDE.md Audit**: Specifically validates the accuracy of "Foundation Mandates" and project conventions.
5. **Remediation**: Generates freshness reports and optionally creates Linear tickets for broken or stale documentation.

## Gemini Advantages
- **Deep Reference Context**: Gemini can resolve complex, indirect code references that simple regex-based scanners miss.
- **Intelligent Staleness Scoring**: Better at determining if a document is *materially* stale vs just chronologically old by understanding the technical significance of the surrounding code changes.
- **System-Wide Convention Mapping**: Correctly identifies when a instruction in CLAUDE.md has been superseded by a new pattern elsewhere in the organization.

## Arguments
- `--repo`: Scan a single repo only.
- `--claude-md-only`: Fast mode for convention verification.
- `--create-tickets`: Create Linear tickets for broken/stale docs.
