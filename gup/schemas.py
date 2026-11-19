"""Versioned, game-agnostic inference output schemas."""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


Visibility = Literal[
    "visible", "occluded", "unreadable", "absent", "not_applicable", "unknown"
]


class Detection(BaseModel):
    """One observation in normalized xyxy coordinates."""

    model_config = ConfigDict(extra="forbid")

    class_name: str = Field(min_length=1)
    bbox_xyxy: tuple[float, float, float, float] | None = None
    value: float | str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    visibility: Visibility = "visible"
    attributes: dict[str, Any] = Field(default_factory=dict)


class PerceptionResult(BaseModel):
    """Top-level result emitted by any GUP task model."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["1.0"] = "1.0"
    game_id: str = Field(min_length=1)
    frame_id: int | None = Field(default=None, ge=0)
    timestamp_seconds: float | None = Field(default=None, ge=0.0)
    model_id: str = Field(min_length=1)
    model_version: str = "0.1.0"
    detections: list[Detection] = Field(default_factory=list)
    status: Literal["ok", "partial", "unknown", "not_applicable"] = "ok"
    metadata: dict[str, Any] = Field(default_factory=dict)
