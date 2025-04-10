from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from typing import Optional, Literal

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: Literal["done", "in_progress", "pending"]
    owner_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("title", "description", mode="before")
    def validate_non_empty_and_length(cls, value, info):
        if isinstance(value, str):
            if not value.strip():
                raise ValueError(f"{info.field_name.capitalize()} cannot be empty or whitespace")
            if len(value.strip()) < 4:
                raise ValueError(f"{info.field_name.capitalize()} must be at least 4 characters long")
        return value