from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class PostCreate(BaseModel):
    username: str
    title: str
    content: str
    image_filename: Optional[str] = None


class LikeCreate(BaseModel):
    username: str
