from service.settings import environment_variables_dict
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from tenacity import retry, wait_fixed, stop_after_attempt
from typing import Optional


async def connect_to_mongodb() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(environment_variables_dict["CONNECTION_STRING_DOCKER"])


@retry(
    stop=stop_after_attempt(environment_variables_dict["MAX_RETRY_ATTEMPTS"]),
    wait=wait_fixed(environment_variables_dict["RETRY_DELAY"])
)
async def get_collection() -> Optional[AsyncIOMotorCollection]:
    try:
        client = await connect_to_mongodb()
        await client.server_info()
        print("Connected to MongoDB")
        return client[environment_variables_dict["DATABASE_NAME"]][environment_variables_dict["COLLECTION_NAME"]]
    except ServerSelectionTimeoutError:
        print("Failed to connect to MongoDB")

    return None
