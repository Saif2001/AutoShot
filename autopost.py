#import pyautogui

#myScreenshot = pyautogui.screenshot()

import pyautogui
import discord
import keyboard
from time import sleep


client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    i = 0
    async def send_on_key():
        if keyboard.is_pressed('ctrl+alt+f'):
            channel = client.get_channel()      #CHANNEL ID HERE
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save()                                 #|
            await channel.send(file=discord.File())             #|- DIRECTORIES HERE

            
    while True:
        sleep(0.2)
        await send_on_key()


client.run()        #BOT TOKEN HERE
