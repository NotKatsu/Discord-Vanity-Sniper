from colorama import *
from helpers.vanity import vanity_client
from helpers.config import config_exists, create_config, get_data

init(convert=True)

if config_exists() is False: 
    create_config(); exit(code=None)
else:
    token: str = get_data()["token"]
    debugging: str = get_data()["debugging"]
    vanities: list[str] = get_data()["vanities"]
    guild_id: int = get_data()["guild_id"]
    
    for vanity in vanities: 
        if vanity_client.vanity_taken(vanity) is True:
            print(f"""{Fore.RED}[VANITY] {vanity.upper()}\n{Fore.RED}[GUILD NAME] {vanity_client.guild_name(vanity)}{Fore.RESET}\n{Fore.RED}[GUILD ID] {vanity_client.guild_id(vanity)}{Fore.RESET}\n{Fore.RED}[BOOST COUNT] {vanity_client.guild_boost_count(vanity)}{Fore.RESET}\n""")
        else:
            if vanity_client.change_vanity_code(int(guild_id), vanity, token) == True:
                exit()

