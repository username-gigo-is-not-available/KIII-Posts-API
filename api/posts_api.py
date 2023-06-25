from fastapi import APIRouter
from schemas import *
from crud import *

router = APIRouter(tags=["posts"])


@router.get("/items", response_model=list[Post])
async def list_all_posts(offset: int = 0, limit: int = 100):
    return await list_all(offset=offset, limit=limit)


@router.post("/items", response_model=Post)
async def create_post(post: PostCreate):
    return await create(post=post)


@router.get("/items/{id}", response_model=Post)
async def get_post_by_id(post_id: str):
    return await get(post_id)


@router.put("/items/{id}", response_model=Post)
async def update_post(post: PostUpdate):
    return await update(post)


@router.delete("/items/{id}", response_model=Post)
async def delete_post(post_id: str):
    return await delete(post_id)
