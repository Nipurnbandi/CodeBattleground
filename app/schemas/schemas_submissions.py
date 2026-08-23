from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.submissions import SubmissionStatus


class SubmissionRequest(BaseModel):
    language: str = Field(min_length=1, max_length=16)
    source_code: str = Field(min_length=1)


class SubmissionResponse(BaseModel):
    id: int
    user_id: int
    problem_id: int
    language: str
    status: SubmissionStatus
    tests_total: int
    tests_done: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)