# SPDX-FileCopyrightText: 2025 OmniNode.ai Inc.
# SPDX-License-Identifier: MIT
"""NodeGeminiEmitEffect — Gemini-native event emission."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from omnibase_core.nodes.node_effect import NodeEffect
from omnibase_infra.event_bus.event_bus_kafka import EventBusKafka
from omnibase_infra.event_bus.models.config import ModelKafkaEventBusConfig

if TYPE_CHECKING:
    from omnibase_core.models.container.model_onex_container import ModelONEXContainer

logger = logging.getLogger(__name__)


class NodeGeminiEmitEffect(NodeEffect):
    """Effect node for Gemini-native event emission."""

    def __init__(self, container: ModelONEXContainer) -> None:
        super().__init__(container)
        self._event_bus: EventBusKafka | None = None

    async def start(self) -> None:
        """Initialize the Kafka event bus."""
        # In a real implementation, we'd get these from config
        kafka_config = ModelKafkaEventBusConfig(
            bootstrap_servers="localhost:19092",
            environment="local",
        )
        self._event_bus = EventBusKafka(config=kafka_config)
        await self._event_bus.start()

    async def emit_event(self, event_type: str, payload: dict[str, Any]) -> None:
        """Publish an event to the appropriate topic."""
        if not self._event_bus:
            logger.error("Event bus not started")
            return

        # Map event_type to canonical OmniGemini topics
        topic = f"onex.evt.omnigemini.{event_type}.v1"
        
        await self._event_bus.publish(
            topic=topic,
            payload=payload,
        )
        logger.debug(f"Emitted {event_type} to {topic}")

    async def stop(self) -> None:
        if self._event_bus:
            await self._event_bus.stop()


__all__ = ["NodeGeminiEmitEffect"]
