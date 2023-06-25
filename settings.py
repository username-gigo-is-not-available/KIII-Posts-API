import os

from pymongo import MongoClient

environment_variables_list = ["CONNECTION_STRING", "DATABASE_NAME", "COLLECTION_NAME"]
environment_variables_dict = {
    env_var: os.getenv(env_var) for env_var in environment_variables_list
}

for variable_name, variable_value in environment_variables_dict.items():
    if not variable_value:
        raise RuntimeError(f"{variable_name} is not set!")

client = MongoClient(environment_variables_dict["CONNECTION_STRING"])
db = client["DATABASE_NAME"]
collection = db["COLLECTION_NAME"]
