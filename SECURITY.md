# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| `0.x.x` (current) | Yes |

---

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report security issues privately to: **contact@omninode.ai**

Include:

- A description of the vulnerability and its potential impact.
- Steps to reproduce or a proof-of-concept (if available).
- The affected version(s).

You will receive an acknowledgment within 48 hours and a resolution timeline within 7 days.

---

## Security Model

`omnigemini` is a **Kafka-driven skill execution layer** backed by the Gemini CLI. Its threat model:

- **No secrets in source**: Kafka bootstrap address and all connection strings are read from environment variables or Infisical. Never hardcoded.
- **Effect nodes are stateless callers**: `NodeGeminiEmitEffect` and `NodeRegistryApiEffect` hold no persistent credentials — they read configuration at startup from env vars.
- **Skill prompts are read-only**: `SKILL.md` files are static prompt definitions. They do not execute arbitrary code; the Gemini CLI backend interprets them.
- **Contract YAML is the API surface**: topic declarations in `contract.yaml` are the only wiring between Python code and the Kafka bus. Undeclared topics cannot be produced or consumed by ONEX routing.
