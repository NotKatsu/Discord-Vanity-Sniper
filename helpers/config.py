import json
import os.path 

def config_exists() -> bool: 
    result = os.path.isfile("./config.json")
    return result 

def create_config() -> bool:
    try:
        file = open("./config.json", "a")
        
        file.write("""{
    "token": "", 
    "debugging": true,

    "vanities": ["discord", "vanity", "sniper"]
}""")
        file.close()
        
        return True
    except:
        return False