# coding=<utf-8>
import discord
import os
from discord.message import Message
client = discord.Client()
birth = [["김태윤", "0610"], ["김주함", "1120"], ["안태흠", "0328"], ["한윤찬", "0201"], ["이여명", "1004"], ["주하윤", "0930"], ["박윤지", "0208"], ["김효인", "0211"]]

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
        if len(message.centent.split()) == 2:
            if message.content.split()[1] == "생일":
                # message.content.split()[0]
                for i in range(len(birth)-1):
                    if not message.content.split()[0].find(birth[i][0]) == -1 or message.content.split()[0].find(str(birth[i][0])[1:3]) == -1:
                        await message.channel.send(message.author.mention + str(birth[i][0])[1:3] + "이의 생일은 " + birth[i][1])
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
