# SPDX-FileCopyrightText: 2025 OmniNode.ai Inc.
# SPDX-License-Identifier: MIT
"""NodeSkillDesignToPlanOrchestrator — thin orchestrator shell for design-to-plan."""

from __future__ import annotations

from typing import TYPE_CHECKING

from omnibase_core.nodes.node_orchestrator import NodeOrchestrator

if TYPE_CHECKING:
    from omnibase_core.models.container.model_onex_container import ModelONEXContainer


class NodeSkillDesignToPlanOrchestrator(NodeOrchestrator):
    """Orchestrator node for the Gemini-native design-to-plan skill."""

    def __init__(self, container: ModelONEXContainer) -> None:
        super().__init__(container)


__all__ = ["NodeSkillDesignToPlanOrchestrator"]
