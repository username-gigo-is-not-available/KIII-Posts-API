import asyncio
from service.settings import environment_variables_dict, environment_variables_list
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from typing import Optional


async def set_connection_string(connection_string: str) -> str:
    for env_variable in environment_variables_list:
        if env_variable in connection_string:
            connection_string = connection_string.replace(env_variable, environment_variables_dict[env_variable])
    return connection_string


# async def connect_to_mongodb(authenticate: bool = True) -> AsyncIOMotorClient:
#     if authenticate:
#         connection_string = await set_connection_string(environment_variables_dict["CONNECTION_STRING_AUTH"])
#     else:
#         connection_string = await set_connection_string(environment_variables_dict["CONNECTION_STRING_NO_AUTH"])
#     return AsyncIOMotorClient(connection_string)

async def connect_to_mongodb() -> AsyncIOMotorClient:
    connection_string = await set_connection_string(environment_variables_dict["CONNECTION_STRING"])
    return AsyncIOMotorClient(connection_string)

# async def check_if_mongodb_user_exists() -> bool:
#     print("Checking if MongoDB user exists...")
#     client = await connect_to_mongodb(authenticate=False)
#     user_collection = client['admin']['users']
#     user = await user_collection.find_one({'username': environment_variables_dict['MONGODB_USER']})
#     if user is not None:
#         print("MongoDB user already exists.")
#     else:
#         print("MongoDB user does not exist.")
#     return user is not None


# async def create_mongodb_user() -> bool:
#     for retry_attempt in range(int(environment_variables_dict['MAX_RETRY_ATTEMPTS'])):
#         try:
#             client = await connect_to_mongodb(authenticate=False)
#             await client.admin.command('createUser', environment_variables_dict["MONGODB_USER"],
#                                              pwd=environment_variables_dict["MONGODB_PASSWORD"], roles=['readWrite'])
#             print("Successfully created MongoDB user!")
#             return True
#         except ServerSelectionTimeoutError:
#             print(f"Failed to create MongoDB user. Retrying... {retry_attempt}")
#             await asyncio.sleep(int(environment_variables_dict['RETRY_DELAY']))
#
#     print("Failed to create MongoDB user.")
#     return False


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
