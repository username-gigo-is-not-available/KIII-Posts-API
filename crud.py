from bson import ObjectId
from fastapi import HTTPException

from schemas import PostCreate, PostUpdate
from settings import *


async def list_all(offset: int = 0, limit: int = 100):
    return collection.find().skip(offset).limit(limit)


async def create(post: PostCreate):
    result = collection.insert_one(post.dict())
    if get(result.inserted_id):
        return get(result.inserted_id)
    else:
        raise HTTPException(status_code=404, detail="Post not found")


async def get(post_id: str):
    post = collection.find_one({"_id": ObjectId(post_id)})
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")


async def update(post: PostUpdate):
    post_id = post.dict(exclude_unset=True).pop("id")
    result = collection.update_one({"_id": ObjectId(post_id)}, {"$set": post.dict(exclude_unset=True)})
    if result.modified_count == 1:
        updated_post = get(post_id)
        return updated_post
    else:
        raise HTTPException(status_code=404, detail="Post not found")


async def delete(post_id: str):
    deleted_post = get(post_id)
    result = collection.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 1:
        return deleted_post
    else:
        raise HTTPException(status_code=404, detail="Post not found")
