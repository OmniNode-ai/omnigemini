# SPDX-FileCopyrightText: 2025 OmniNode.ai Inc.
# SPDX-License-Identifier: MIT
"""NodeSkillEpicTeamOrchestrator — thin orchestrator shell for epic-team."""

from __future__ import annotations

from typing import TYPE_CHECKING

from omnibase_core.nodes.node_orchestrator import NodeOrchestrator

if TYPE_CHECKING:
    from omnibase_core.models.container.model_onex_container import ModelONEXContainer


class NodeSkillEpicTeamOrchestrator(NodeOrchestrator):
    """Orchestrator node for the Gemini-native epic-team skill."""

    def __init__(self, container: ModelONEXContainer) -> None:
        super().__init__(container)


__all__ = ["NodeSkillEpicTeamOrchestrator"]
