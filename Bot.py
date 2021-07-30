import discord
#import nest_asyncio
from discord.ext import commands
import json

#讀取設定檔
with open('setting.json','r',encoding='utf8') as jfile: #(檔案，r讀取，編碼)
    jdata=json.load(jfile)



#intents設置
intents=discord.Intents.default() #all.none.default() ex.default except presences&members
intents.members=True

#建立bot
bot=commands.Bot(command_prefix='[',intents=intents)

#啟動顯示訊息
@bot.event
async def on_ready():
    print(">>阿干肝甘乾Bot is online<<")

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

#指令
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')#round:小數點後四捨五入/latency:回傳延遲

#執行bot
bot.run(jdata['TOKEN']) #bot.run(Bot_Token)
