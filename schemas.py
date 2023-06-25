from pydantic import BaseModel


class PostBase(BaseModel):
    title = str
    description = str
    author_id = str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    class Config:
        orm_mode = True
