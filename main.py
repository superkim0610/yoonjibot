# coding=<utf-8>
import discord
import os
from discord.message import Message
client = discord.Client()
birth = [["한윤찬", "0201"],["박채진", "0206"],["박윤지", "0208"],["김효인", "0211"],["안태흠", "0328"],["신수빈", "0411"],["이서형", "0427"],["김태윤", "0610"],["전승흔", "0830"],["주하윤", "0930"],["윤성훈", "1019"],["공지민", "1108"],["김주함", "1120"]]

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
        if message.content == "칼답은?" or message.content == "칼답은":
            await message.channel.send("김태윤!")
        if message.content == "디즈니 씹덕은?" or message.content == "디즈니 씹덕은":
            await message.channel.send("윤지!")
        if len(message.content.split()) == 2:
            if message.content.split()[1] == "생일":
                # message.content.split()[0]
                for i in range(len(birth)):
                    # if not message.content.split()[0].find(birth[i][0]) == -1 or message.content.split()[0].find(str(birth[i][0])[1:3]) == -1:
                    if message.content.split()[0] == birth[i][0] or message.content.split()[0] == str(birth[i][0])[1:3]:
                        await message.channel.send(message.author.mention + " " + str(birth[i][0])[1:3] + " 생일 " + getBirthString(birth[i][1]) + "!")

def getBirthString(_birth):
    m = _birth[0:2]
    d = _birth[2:4]
    return m.lstrip("0") + "월 " + d.lstrip("0") + "일"

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
