---
name: dashboard-sweep
description: Gemini-native dashboard audit-debug-fix loop — Playwright recon and parallel systematic-debug with 2M+ token grounding
capability: skill.dashboard_sweep
node_name: node_skill_dashboard_sweep_orchestrator
dot_color: 208
---

# Dashboard Sweep Skill (Gemini Edition)

Full autonomous audit-debug-fix loop for all dashboard pages, leveraging Gemini's massive context window to diagnose and fix UI defects, data pipeline gaps, and schema mismatches in a single pass.

## Workflow
1. **Recon**: Gemini orchestrates a Playwright audit of all routes, capturing screenshots and browser console errors for classification (HEALTHY, EMPTY, MOCK, BROKEN, FLAG_GATED).
2. **Triage**: Groups findings into problem domains (CODE_BUG, DATA_PIPELINE, SCHEMA_MISMATCH) and assigns fix tiers.
3. **Parallel Debug**: Dispatches multiple Gemini-native debug agents simultaneously to investigate and fix issues in dedicated worktrees.
4. **Validation**: Gemini re-audits the dashboard after fixes are merged to verify the resolution and ensure no regressions.
5. **Redeploy**: Optionally triggers local container restarts or cloud redeployments after successful fixes.

## Gemini Advantages
- **Cross-Stack Triage**: Gemini can simultaneously analyze TypeScript UI code and Python backend services to identify exactly where a data pipeline is broken.
- **Whole-Project Root Cause Analysis**: Unlike local debuggers, Gemini sees the entire system state, allowing it to solve complex "missing data" issues that span multiple repositories.
- **Superior Parallel Orchestration**: More efficiently manages multiple concurrent fix streams by maintaining a holistic view of the sweep's progress.

## Arguments
- `--target`: Deployment target: local or cloud.
- `--url`: Explicit dashboard base URL override.
- `--max-iterations`: Hard cap on fix-reaudit cycles.
- `--deploy`: Auto-deploy after fixes merge.
