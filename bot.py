import os
import librairies
from discord.ext import commands
from commands.request import *
from commands.file import *

librairies.dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = librairies.discord.Client()
bot = commands.Bot(command_prefix=';')


Request=Request()
File=File()
@ bot.event
async def on_ready():
    print('bot online')
    await bot.change_presence(activity=discord.Game(name="Type ;help"))

@ bot.command()
async def stats(ctx, *arg):
    if len(arg) == 0:
        arg = await File.getUser(bot.user.id)
    embed=await Request.getStats(arg)
    await ctx.send(embed = embed)

@ bot.command()
async def map(ctx):
    embed=await Request.getMap()
    await ctx.send(embed = embed)

@ bot.command()
async def link(ctx, *arg):
    embed=await File.saveUser(arg,bot.user.id,bot.user.name)
    await ctx.send(embed = embed)

@ bot.command()
async def unlink(ctx):
    embed=await File.delUser(bot.user.id)
    await ctx.send(embed = embed)

bot.run(TOKEN)
