import json
import httpx 

from typing import Union

class vanity_client: 
    def __init__(self) -> None:
        pass
    
    def vanity_taken(vanity: str) -> bool:
        result = httpx.get(f"https://discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return True
        else:
            return False
        
    def guild_id(vanity: str) -> Union[None, str]:
        result = httpx.get(f"https://discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["id"]
        else:
            return None
        
    def guild_boost_count(vanity: str) -> int:
        result = httpx.get(f"https://discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["premium_subscription_count"]
        else:
            return None
        
    def guild_name(vanity: str) -> str:
        result = httpx.get(f"https://discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["name"]
        else:
            return None
        
    def guild_description(vanity: str) -> str: 
        result = httpx.get(f"https://discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["description"]
        else:
            return None
        

    def change_vanity_code(guild_id: int, vanity: str, token: str) -> bool:
        try:
            payload = {'code': vanity}
            headers = {
                "Authorization": f"{token}",
                "Content-Type": "application/json",
            }
            
            response = httpx.patch(f"https://discord.com/api/v9/guilds/{guild_id}/vanity-url", data=json.dumps(payload), headers=headers)
            
            if response.status_code == 200: 
                return True
            else:
                return False
        except:
            return False