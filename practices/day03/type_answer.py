from pydantic import BaseModel, Field, computed_field, ConfigDict
from enum import Enum
from typing import Literal


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class Category(str, Enum):
    STYLE = "style"
    NAMING = "naming"
    LOGIC = "logic"
    SECURITY = "security"


class ReviewComment(BaseModel):
    file_path: str
    line_number: int = Field(ge=1)
    severity: Severity
    category: Category
    message: str = Field(min_length=1, max_length=200)
    suggestion: str | None = Field(default=None)

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True
    )


class ReviewRequest(BaseModel):
    file_path: str
    file_content: str
    language: str = Field(default="python")
    review_level: Literal["low", "medium", "high"] = Field(default="medium")

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True
    )


class ReviewResponse(BaseModel):
    request_id: str
    comments: list[ReviewComment]
    summary: str

    @computed_field
    @property
    def total_issues(self) -> int:
        return len(self.comments)

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True
    )
