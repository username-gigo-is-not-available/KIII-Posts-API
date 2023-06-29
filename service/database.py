import asyncio
from service.settings import environment_variables_dict, environment_variables_list
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from typing import Optional


async def connect_to_mongodb() -> AsyncIOMotorClient:
    connection_string = environment_variables_dict["CONNECTION_STRING_DOCKER"]
    for env_variable in environment_variables_list:
        if env_variable in connection_string:
            connection_string = connection_string.replace(env_variable, environment_variables_dict[env_variable])

    return AsyncIOMotorClient(connection_string)


async def get_collection() -> Optional[AsyncIOMotorCollection]:
    for retry_attempt in range(int(environment_variables_dict['MAX_RETRY_ATTEMPTS'])):
        try:
            client = await connect_to_mongodb()
            await client.server_info()
            print("Connected to MongoDB")
            return client[environment_variables_dict["DATABASE_NAME"]][environment_variables_dict["COLLECTION_NAME"]]
        except ServerSelectionTimeoutError:
            print(f"Failed to connect to MongoDB. Retrying ... {retry_attempt}")
            await asyncio.sleep(int(environment_variables_dict['RETRY_DELAY']))

    print("Failed to connect to MongoDB.")
    return None
