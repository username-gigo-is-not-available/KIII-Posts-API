from fastapi import FastAPI
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorCollection
from service.database import *
from service.posts_api import router as posts_router

app = FastAPI(title="Posts Service")

app.include_router(posts_router)


@app.on_event("startup")
async def startup_event() -> Optional[AsyncIOMotorCollection]:
    user_exists = await check_if_mongodb_user_exists()
    if not user_exists:
        await create_mongodb_user()
    await get_collection()
