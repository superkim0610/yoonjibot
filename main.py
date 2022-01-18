import discord
from random import randrange
import datetime

discord_token = 'dd'
client = discord.Client()

q = []
_i = 0
sid = 0
per = [0,0] # incorrect, correct

def logging(m):
    log_jiyou = open("log_jiyou.txt", "a", encoding="utf8")
    log_jiyou.write(str(datetime.datetime.now())+' '+m+'\n')
    log_jiyou.close()

@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):
    global sid, _i, q, per
    print(sid, _i, q)
    if not message.author == client.user:
        if message.author.id == sid:       
            if q[_i][2]:
                if int(message.content) == q[_i][0] + q[_i][1]:
                    await message.channel.send('이걸 맞추네;')
                    per[1]+=1
                    logging(str(sid)+', _i: '+str(_i)+', input: '+message.content+', correct')
                    _i+=1
                    if _i+1 <= len(q):
                        if q[_i][2]:
                            await message.channel.send(f'({_i+1}) {q[_i][0]}보다 {q[_i][1]}만큼 큰 수')
                        else:
                            await message.channel.send(f'({_i+1}) {q[_i][0]}보다 {q[_i][1]}만큼 작은 수')
                else:
                    await message.channel.send('틀렸어 바보 멍청아~!')
                    per[0]+=1
                    logging(str(sid)+', _i: '+str(_i)+', input: '+message.content+', incorrect')
                    print(q[_i][0] + q[_i][1])
            else:
                if int(message.content) == q[_i][0] - q[_i][1]:
                    await message.channel.send('이걸 맞추네;')
                    per[1]+=1
                    logging(str(sid)+', _i: '+str(_i)+', input: '+message.content+', correct')
                    _i+=1
                    if _i+1 <= len(q):
                        if q[_i][2]:
                            await message.channel.send(f'({_i+1}) {q[_i][0]}보다 {q[_i][1]}만큼 큰 수')
                        else:
                            await message.channel.send(f'({_i+1}) {q[_i][0]}보다 {q[_i][1]}만큼 작은 수')
                else:
                    await message.channel.send('틀렸어 바보 멍청아~!')
                    per[0]+=1
                    logging(str(sid)+', _i: '+str(_i)+', input: '+message.content+', incorrect')
                    print(q[_i][0] - q[_i][1])
            if _i == len(q):
                await message.channel.send(str(_i)+'문제를 모두 다 풀었어! 축하링딩동~ (정답률 :'+str(per[1]/sum(per)*100)+'%)')
                logging(str(sid)+', '+str(_i)+'q complete, 정답률 : ,'+str(per[1]/sum(per)*100)+'%, [incorrect, correct] = '+str(per))
                per = [0,0]
        mc = message.content
        if mc.startswith('공부시작 '):
            n = int(mc.strip().split()[1])
            q = []
            _i = 0
            sid = message.author.id
            for i in range(n):
                q.append([randrange(-11,12),randrange(-11,12),randrange(0,2)])
            logging(str(sid)+', '+str(n)+'q start ,'.join(list(map(str,[_i,q]))))
            if q[_i][2]:
                await message.channel.send(f'({_i+1}) {q[_i][0]}보다 {q[_i][1]}만큼 큰 수')
            else:
                await message.channel.send(f'({_i+1}) {q[_i][0]}보다 {q[_i][1]}만큼 작은 수')
client.run(discord_token)
