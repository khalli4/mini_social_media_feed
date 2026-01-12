from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8, max_length=72)  # enforce 8–72 chars


class UserLogin(BaseModel):
    username: str
    password: constr(min_length=8, max_length=72)


class PostCreate(BaseModel):
    username: str
    title: str
    content: str
    image_filename: Optional[str] = None


class LikeCreate(BaseModel):
    username: str
