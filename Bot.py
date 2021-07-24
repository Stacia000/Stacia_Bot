import discord
#import nest_asyncio
from discord.ext import commands

#intents設置
intents=discord.Intents.default() #all.none.default() ex.default except presences&members
intents.members=True

#建立bot
bot=commands.Bot(command_prefix='[',intents=intents)

#啟動顯示訊息
@bot.event
async def on_ready():
    print(">>Bot is online<<")

#成員加入訊息
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(868438995498074142) #指定頻道
    await channel.send(f'{member}join!')
    #print(f'{member}join!')

#成員離開訊息
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(868438995498074142) #指定頻道
    await channel.send(f'{member}leave!')
    #print(f'{member}leave!')

#執行bot
bot.run('NzEzMDMwMzM1ODMwNjg3ODU0.XsaLPw.nY9uTZC5_qym7k8ROcuvVbmCE4I')
