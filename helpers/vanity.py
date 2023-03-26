import httpx 

from typing import Union

class vanity: 
    def __init__(self) -> None:
        pass
    
    def vanity_taken(vanity: str) -> bool:
        result = httpx.get(f"https://canary.discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return True
        else:
            return False
        
    def guild_id(vanity: str) -> Union[None, str]:
        result = httpx.get(f"https://canary.discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["id"]
        else:
            return None
        
    def guild_boost_count(vanity: str) -> int:
        result = httpx.get(f"https://canary.discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["premium_subscription_count"]
        else:
            return None
        
    def guild_name(vanity: str) -> str:
        result = httpx.get(f"https://canary.discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["name"]
        else:
            return None
        
    def guild_description(vanity: str) -> str: 
        result = httpx.get(f"https://canary.discord.com/api/v9/invites/{vanity}")
        
        if result.status_code == 200: 
            return result.json()["guild"]["description"]
        else:
            return None