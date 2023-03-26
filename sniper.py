from colorama import *
from helpers.config import config_exists, create_config, get_data

init(convert=True)

if config_exists() is False: 
    create_config(); exit(code=None)
else:
    token: str = get_data()["token"]
    debugging: str = get_data()["debugging"]
    vanities: list[str] = get_data()["vanities"]
    
    if token == "":
        print("empty token")
    