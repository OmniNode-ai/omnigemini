# SPDX-FileCopyrightText: 2025 OmniNode.ai Inc.
# SPDX-License-Identifier: MIT
"""Skill result model for omnigemini."""

from __future__ import annotations

from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class SkillResultStatus(StrEnum):
    """Possible outcomes of a Gemini-native skill invocation."""

    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"
    ERROR = "error"


class ModelSkillResult(BaseModel):
    """Output from any Gemini-native skill dispatch node."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    skill_name: str = Field(..., min_length=1)
    status: SkillResultStatus = Field(...)
    output: str | None = Field(default=None)
    error: str | None = Field(default=None)
    correlation_id: UUID = Field(...)


#: Alias for ModelSkillResult
SkillResult: type[ModelSkillResult] = ModelSkillResult

__all__ = ["ModelSkillResult", "SkillResult", "SkillResultStatus"]
