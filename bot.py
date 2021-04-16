import os
import librairies
from discord.ext import commands
from commands.request import *

librairies.dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = librairies.discord.Client()
bot = commands.Bot(command_prefix=';')


Request=Request()
@ bot.event
async def on_ready():
    print('bot online')
    await bot.change_presence(activity=discord.Game(name="Type ;help"))

@ bot.command()
async def stats(ctx, *arg):
    embed=await Request.getStats(arg)
    await ctx.send(embed = embed)

@ bot.command()
async def map(ctx):
    embed=await Request.getMap()
    await ctx.send(embed = embed)


bot.run(TOKEN)
