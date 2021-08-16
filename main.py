# coding=<utf-8>
import discord
import os
import math
from discord.message import Message
client = discord.Client()
auto_delete = False
auto_delete_id = 857906844022603787
birth = [["한윤찬", "0201"],["박채진", "0206"],["박윤지", "0208"],["김효인", "0211"],["안태흠", "0328"],["신수빈", "0411"],["이서형", "0427"],["김태윤", "0610"],["전승흔", "0830"],["주하윤", "0930"],["이여명", "1004"],["윤성훈", "1019"],["공지민", "1108"],["김주함", "1120"]]
def quadratic_equation(a,b,c):
    if a.startswith("-"):
        a=-int(a.strip("-"))
    else:
        a=int(a)
    if b.startswith("-"):
        b=-int(b.strip("-"))
    else:
        b=int(b)
    if c.startswith("-"):
        c=-int(c.strip("-"))
    else:
        c=int(c)
    d = b**2-4*a*c
    if d == 0:
        return (-b)/(2*a)
    elif d > 0:
        return (-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)
    elif d < 0:
        return [(-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)]

@client.event
async def on_ready():
    game = discord.Game("디즈니 덕질!") # 상태 메시지
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content =="오" or message.content =="오..":
            await message.channel.send("오..")
            await message.channel.send(type(message.author.id))
        if message.content == "윤지는?" or message.content == "윤지는":
            await message.channel.send("디즈니 씹덕!")
        if message.content == "디즈니 씹덕은?" or message.content == "디즈니 씹덕은":
            await message.channel.send("윤지!")
        if len(message.content.split()) == 2:
            if message.content.split()[1] == "생일":
                # message.content.split()[0]
                for i in range(len(birth)):
                    # if not message.content.split()[0].find(birth[i][0]) == -1 or message.content.split()[0].find(str(birth[i][0])[1:3]) == -1:
                    if message.content.split()[0] == birth[i][0] or message.content.split()[0] == str(birth[i][0])[1:3]:
                        await message.channel.send(message.author.mention + str(birth[i][0])[1:3] + " 생일 " + getBirthString(birth[i][1]) + "!")
        if message.content == "윤지야 드가자":
            auto_delete = True
            await message.channel.send("ㄱ")
        if message.content == "윤지야 나가자":
            auto_delete = False
            await message.channel.send("ㅠ")
        if message.content.startswith("윤지야 다음은 "):
            auto_delete_id = int(message.content.split()[2])
        if auto_delete:
            await message.channel.send("on "+str(auto_message_id))
            if message.author.id == auto_message_id:
                await message.channel.send("ㅋㅋ")
                await message.delete()
            else:
                await message.channel.send("ㄴㄴ")
        if message.content.startswith("윤지야 이차방정식 "):
            if len(message.content.split()) == 5:
                await message.channel.send("𝓍 = "+str(quadratic_equation(message.content.split()[2],message.content.split()[3],message.content.split()[4])).strip("(").strip(")").strip("0").strip("."))
        if message.content.startswith("exec "):
            r = message.content[5:]
            await message.channel.send(exec(r))
            print("exec : "+r)
        if message.content.startswith("윤지야 계산해 "):
            r = message.content[7:]
            await message.channel.send(eval(r))
            print("exec : "+r)
def getBirthString(_birth):
    m = _birth[0:2]
    d = _birth[2:4]
    return m.lstrip("0") + "월 " + d.lstrip("0") + "일"

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
