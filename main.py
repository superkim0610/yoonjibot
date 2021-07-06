# coding=<utf-8>
import discord
import asyncio
import youtube_dl 
import time
import urllib.request
from urllib.parse import quote
import re
import random
import pickle
import json
import logging
# http://whaleon.naver.com/on/1234567890
client = discord.Client()
token = "TOKEN"

@client.event
async def on_ready():
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    t = str(str(time.localtime(time.time()).tm_year) + "/" + str(time.localtime(time.time()).tm_mon) + "/" + str(time.localtime(time.time()).tm_mday) + "/" + str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":" + str(time.localtime(time.time()).tm_sec))
    game = discord.Game("디즈니 덕질") # 상태 메시지
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    t = str(str(time.localtime(time.time()).tm_year) + "/" + str(time.localtime(time.time()).tm_mon) + "/" + str(time.localtime(time.time()).tm_mday) + "/" + str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":" + str(time.localtime(time.time()).tm_sec))
    if not message.author.bot:
        if message.content =="오" or message.content =="오..":
            await message.channel.send("오..")

        if message.content == "윤지는?" or message.content == "윤지는":
            await message.channel.send("디즈니 씹덕!")
        if message.content == "디즈니 씹덕은?" or message.content == "디즈니 씹덕은":
            await message.channel.send("윤지!")
            
        if message.content == "윤지 생일":
            await message.channel.send(message.author.mention+" 내 생일 2월 8일!")

client.run(token)
