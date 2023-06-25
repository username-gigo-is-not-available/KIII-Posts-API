from bson import ObjectId
from pydantic import BaseModel, Field


class Post(BaseModel):

    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    title: str
    content: str
    author_id: str
