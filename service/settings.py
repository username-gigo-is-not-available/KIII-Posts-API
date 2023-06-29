import os
from dotenv import *

load_dotenv()

environment_variables_list = list(os.environ.keys())
environment_variables_dict = {
    env_var: os.getenv(env_var) for env_var in environment_variables_list
}

for variable_name, variable_value in environment_variables_dict.items():
    if not variable_value:
        raise RuntimeError(f"{variable_name} is not set!")
