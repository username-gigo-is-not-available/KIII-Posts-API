from pymongo import MongoClient

from settings import environment_variables_dict


def get_db_client():
    return MongoClient(environment_variables_dict["CONNECTION_STRING"])


def get_db():
    return get_db_client()["DATABASE_NAME"]


def get_collection():
    return get_db()["COLLECTION"]
