# coding=<utf-8>
import discord
import os
# http://whaleon.naver.com/on/1234567890
client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game("디즈니 덕질") # 상태 메시지
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content =="오" or message.content =="오..":
            await message.channel.send("오..")
        if message.content == "윤지는?" or message.content == "윤지는":
            await message.channel.send("디즈니 씹덕!")
        if message.content == "디즈니 씹덕은?" or message.content == "디즈니 씹덕은":
            await message.channel.send("윤지!")
        if message.content == "윤지 생일":
            await message.channel.send(message.author.mention+" 내 생일 2월 8일!")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
