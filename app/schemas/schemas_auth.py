from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime


class UsersRequest(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)


class UsersResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
