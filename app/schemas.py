from datetime import datetime
from typing import List, Optional
import uuid
from pydantic import BaseModel


class PostBaseSchema(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class CreatePostSchema(PostBaseSchema):
    pass


class PostResponse(PostBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class UpdatePostSchema(BaseModel):
    title: str
    content: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class ListPostResponse(BaseModel):
    status: str
    results: int
    posts: List[PostResponse]
