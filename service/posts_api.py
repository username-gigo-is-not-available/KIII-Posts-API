from fastapi import APIRouter, Depends
from service.crud import *
from service.database import get_collection
from service.schemas import *
from service.database_models import *

router = APIRouter(tags=["posts"], prefix="/posts")


@router.get("", response_model=list[Post])
async def list_all_posts(offset: int = 0, limit: int = 100,
                         collection: AsyncIOMotorCollection = Depends(get_collection)):
    result = await query(offset=offset, limit=limit, collection=collection)
    return result


@router.post("/query", response_model=list[Post])
async def query_posts(offset: int = 0, limit: int = 100, query_sort: list[tuple[str, int]] = None,
                      query_filter: dict[str, Any] = None,
                      collection: AsyncIOMotorCollection = Depends(get_collection)):
    result = await query(offset=offset, limit=limit, query_sort=query_sort, query_filter=query_filter,
                         collection=collection)
    return result


@router.get("/count", response_model=int)
async def count_number_of_documents(collection: AsyncIOMotorCollection = Depends(get_collection)):
    return await count(collection)


@router.post("", response_model=Post)
async def create_post(post: PostCreate, collection: AsyncIOMotorCollection = Depends(get_collection)):
    return await create(post=post, collection=collection)


@router.get("/{id}", response_model=Post)
async def get_post_by_id(post_id: str, collection: AsyncIOMotorCollection = Depends(get_collection)):
    return await get(post_id, collection)


@router.put("/{id}", response_model=Post)
async def update_post(post_id: str, post: PostUpdate, collection: AsyncIOMotorCollection = Depends(get_collection)):
    return await update(post_id, post, collection)


@router.delete("/{id}", response_model=Post)
async def delete_post(post_id: str, collection: AsyncIOMotorCollection = Depends(get_collection)):
    return await delete(post_id, collection)
