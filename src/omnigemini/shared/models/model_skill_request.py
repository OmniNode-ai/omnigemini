# SPDX-FileCopyrightText: 2025 OmniNode.ai Inc.
# SPDX-License-Identifier: MIT
"""Skill request model for omnigemini."""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ModelSkillRequest(BaseModel):
    """Input to any Gemini-native skill dispatch node.

    Attributes:
        skill_name: Human-readable skill identifier (e.g. "pr_polish").
        skill_path: Absolute or relative path to the skill's SKILL.md file.
        args: Key/value argument pairs.
        correlation_id: Correlation ID for end-to-end request tracing.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    skill_name: str = Field(..., min_length=1)
    skill_path: str = Field(...)
    args: dict[str, str] = Field(default_factory=dict)
    correlation_id: UUID = Field(...)

    @field_validator("skill_path")
    @classmethod
    def _validate_skill_path(cls, value: str) -> str:
        if not value.endswith("SKILL.md"):
            raise ValueError(f"skill_path must end with 'SKILL.md', got: {value!r}")
        return value


__all__ = ["ModelSkillRequest"]
