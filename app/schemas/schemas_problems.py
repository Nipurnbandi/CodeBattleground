from pydantic import BaseModel, ConfigDict


class DefaultCodeResponse(BaseModel):
    id: int
    language: str
    starter_code: str
    full_boilerplate: str

    model_config = ConfigDict(from_attributes=True)


class ProblemResponse(BaseModel):
    id: int
    slug: str
    title: str
    points: int

    model_config = ConfigDict(from_attributes=True)


class ProblemDetailResponse(ProblemResponse):
    statement_markdown: str
    time_limit_seconds: int
    memory_limit_mb: int
    default_codes: list[DefaultCodeResponse]
    