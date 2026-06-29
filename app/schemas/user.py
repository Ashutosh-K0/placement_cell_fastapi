from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Annotated
from datetime import datetime

class UserBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=200, title='Name of the user')]
    email: EmailStr
    phone_number: Annotated[str, Field(min_length=10, max_length=20, title='Phone number of the user', pattern=r"^\+?[0-9]{10,20}$")]

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=8, max_length=255, title='Password of the account')]

class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=200)
    phone_number: str | None = Field(default=None, min_length=10, max_length=20, pattern=r"^\+?[0-9]{10,20}$")


class UserResponse(UserBase):
    id: int
    company_id: int | None
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
