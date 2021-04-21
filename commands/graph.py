import discord
import os
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class Graph:
    async def legendGraph(self,arg):
        try:
            pseudo = arg[0]
            legende = arg[1]
            with open('accountLinks/save.txt') as json_file:
                data = json.load(json_file)
                for compte in data["comptes"]:
                    if compte["apexUser"] == pseudo:
                        kills = data["comptes"][0]["stats"][legende]["kills"]
                        dates = data["comptes"][0]["stats"][legende]["date"]

                        fig, ax = plt.subplots()
                        ax.xaxis.set_major_locator(MaxNLocator(5))
                        ax.yaxis.set_major_locator(MaxNLocator(5))
                        ax.yaxis.grid(True)
                        ax.plot(dates,kills, color="#851A2A")
                        ax.spines['top'].set_visible(False)
                        ax.spines['right'].set_visible(False)
                        ax.spines['bottom'].set_color("white")
                        ax.spines['left'].set_color("white")
                        ax.xaxis.label.set_color('white')
                        ax.yaxis.label.set_color('white')
                        ax.tick_params(axis='x', colors='white')
                        ax.tick_params(axis='y', colors='white')

                        plt.yscale('linear')
                        plt.ylabel("Kills")
                        plt.xlabel("Date (mm/dd/yy)")
                        plt.savefig("./img/img", transparent=True)
                        plt.close('all')
                        embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description=f"Graphique des kills sur la légende: **{legende}**")
                        embed.set_author(name=pseudo)
                        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                        embed.add_field(name="\u200b",value=f"Les stats sont enregistrées depuis le: `{dates[0]}`",inline=True)
                        embed.set_footer(text="By Nave#1960")
                        return embed,True
                
                embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Merci de vérifier la syntaxe de la légende demandée et vérifiez votre pseudo Apex Legends. \nVous devez également avoir lié votre compte avec la commande `;link`")
                embed.set_author(name="Erreur")
                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                embed.set_footer(text="By Nave#1960")
                return embed,False
        except:
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Mauvaise syntaxe de la commande.\n`;graph <pseudo> <légende>`\nExemple:\n`;graph PotagerDeNavets Pathfinder`")
            embed.set_author(name="Erreur")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
            embed.set_footer(text="By Nave#1960")
            return embed,False