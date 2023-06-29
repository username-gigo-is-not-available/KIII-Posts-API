from typing import Optional
from motor.motor_asyncio import AsyncIOMotorCollection
from fastapi import FastAPI
from service.database import get_collection
from service.posts_api import router as posts_router

app = FastAPI(title="Posts Service")

app.include_router(posts_router)


@app.on_event("startup")
async def startup_event() -> Optional[AsyncIOMotorCollection]:
    await get_collection()
