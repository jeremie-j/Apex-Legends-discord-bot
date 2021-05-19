import os
import discord
from discord import message
import dotenv
from discord.ext import commands
from discord.ext import tasks
from commands.request import *
from commands.file import *
from commands.graph import *
from commands.help import *

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
bot = commands.Bot(command_prefix=';')
bot.remove_command("help")

Request=Request()
File=File()
Graph=Graph()
Help=Help()

@ bot.event
async def on_ready():
    print('Bot online')
    await bot.change_presence(activity=discord.Game(name="Type ;help"))

@ bot.command()
async def stats(ctx, *arg):
    if len(arg) == 0:
        arg = await File.getUser(ctx.message.author.id)
    embed=await Request.getStats(arg)
    await ctx.send(embed = embed)

@ bot.command()
async def map(ctx):
    embed=await Request.getMap()
    await ctx.send(embed = embed)

@ bot.command()
async def link(ctx, *arg):
    embed=await File.saveUser(arg,ctx.message.author.id,ctx.message.author.name)
    await ctx.send(embed = embed)

@ bot.command()
async def unlink(ctx):
    embed=await File.delUser(ctx.message.author.id)
    await ctx.send(embed = embed)

@ bot.command()
async def graph(ctx, *arg):
    embed,image = await Graph.legendGraph(arg)
    if image == True:
        embed.set_image(url='attachment://img.png')
        img = discord.File("./img/img.png", filename="img.png")
        await ctx.send(file = img, embed = embed)
    else:
        await ctx.send(embed = embed)

@ bot.command()
async def help(ctx):
    embed = await Help.displayHelp()
    await ctx.send(embed = embed)

@tasks.loop(hours=24)
async def refresh():
    print("Stats Update")
    await Request.updateStats()

refresh.start()

bot.run(TOKEN)
