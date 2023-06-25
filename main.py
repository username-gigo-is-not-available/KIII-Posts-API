from fastapi import FastAPI
from api.posts_api import router as posts_router
from database import *

app = FastAPI(title="Posts Service")

app.include_router(posts_router)


@app.on_event("startup")
async def startup_event():
    collection =  get_collection()
