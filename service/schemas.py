from datetime import datetime
from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str = Field()
    content: str = Field()


class PostCreate(PostBase):
    author_id: int = Field()


class PostUpdate(PostBase):
    pass


class Post(PostCreate):
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
