import os
from dotenv import *

load_dotenv()

environment_variables_list = ["CONNECTION_STRING_LOCAL", "CONNECTION_STRING_DOCKER",
                              "DATABASE_NAME", "COLLECTION_NAME", "MAX_RETRY_ATTEMPTS", "RETRY_DELAY"]
environment_variables_dict = {
    env_var: os.getenv(env_var) for env_var in environment_variables_list
}

for variable_name, variable_value in environment_variables_dict.items():
    if not variable_value:
        raise RuntimeError(f"{variable_name} is not set!")
