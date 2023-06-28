from typing import Any
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument
from service.database_models import *
from service.schemas import *


async def query(collection: AsyncIOMotorCollection, offset: int = 0, limit: int = 100,
                query_sort: list[tuple[str, int]] = None,
                query_filter: dict[str, Any] = None):
    cursor = collection.find(query_filter).skip(offset).limit(limit)
    cursor = cursor.sort(query_sort) if query_sort else cursor
    result = [doc async for doc in cursor]
    print(f"All Posts: {result}")
    return result


async def count(collection: AsyncIOMotorCollection):
    if (total := await collection.count_documents({})) != 0:
        print(f"Total Posts: {total}")
        return total
    raise HTTPException(status_code=404, detail="MongoDB collection is empty!")


async def create(post: PostCreate, collection: AsyncIOMotorCollection):
    data = post.dict()
    data['timestamp'] = datetime.now()
    result = await collection.insert_one(data)
    if (inserted_post := await get(post_id=result.inserted_id, collection=collection)) is not None:
        print(f"Inserted Post: {inserted_post}")
        return inserted_post
    else:
        raise HTTPException(status_code=404, detail="Post not found")


async def get(post_id: str, collection: AsyncIOMotorCollection):
    if (post := await collection.find_one({"_id": ObjectId(post_id)})) is not None:
        print(f"Get Post: {post}")
        return Post(**post)
    else:
        raise HTTPException(status_code=404, detail="Post not found")


async def update(post_id: str, post: PostUpdate, collection: AsyncIOMotorCollection):
    data = post.dict()
    data['timestamp'] = datetime.now()
    if (result := await collection.find_one_and_update({"_id": ObjectId(post_id)}, {"$set": data},
                                                       return_document=ReturnDocument.AFTER)) is not None:
        print(f"Updated Post: {result}")
        return result
    else:
        raise HTTPException(status_code=404, detail="Post not found")


async def delete(post_id: str, collection: AsyncIOMotorCollection):
    if (result := await collection.find_one_and_delete({"_id": ObjectId(post_id)})) is not None:
        print(f"Deleted Post: {result}")
        return Post(**result)
    else:
        raise HTTPException(status_code=404, detail="Post not found")
