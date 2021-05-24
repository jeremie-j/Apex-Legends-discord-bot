import discord
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class Graph:
    async def legendGraph(self,arg):
        try:
            if len(arg) == 1:
                pseudo = arg[0]
                with open('accountLinks/save.txt') as json_file:
                    data = json.load(json_file)
                    for i,compte in enumerate(data["comptes"]):
                        if compte["apexUser"].lower() == pseudo.lower():
                            legends = ""
                            for legend in compte["stats"]:
                                date = compte["stats"][legend]["date"][0]
                                nbPoints = len(compte["stats"][legend]["date"])
                                legends += str(f"**{legend}**, depuis le `{date}`, nombres de points: `{nbPoints}`\n")
                            refreshTime = data["refresh"]
                            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description=f"Voici les graphiques disponibles pour : **{pseudo}**")
                            embed.add_field(name="\u200b",value=legends,inline=False)
                            embed.add_field(name="\u200b",value=f"Les données sont recupérées tous les jours à `{refreshTime}`",inline=False)
                            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                            embed.set_footer(text="By Nave#1960")
                            return embed,False
                    embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description=f"Aucun compte trouvé, verifiez que `{pseudo}` s'agit bien de votre identifiant Origin")
                    embed.set_author(name="Erreur")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                    embed.set_footer(text="By Nave#1960")
                    return embed,False
            else:
                pseudo = arg[0]

                legende = arg[1].lower()
                legende = list(legende)
                legende[0] = legende[0].upper()
                legende = ''.join(legende)

                with open('accountLinks/save.txt') as json_file:
                    data = json.load(json_file)
                    for i,compte in enumerate(data["comptes"]):
                        if compte["apexUser"].lower() == pseudo.lower():
                            try:
                                kills = data["comptes"][i]["stats"][legende]["kills"]
                                dates = data["comptes"][i]["stats"][legende]["date"]

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
                                # Compte trouvé, mais pas encore de données
                            except:
                                embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Votre compte a été trouvé, mais aucune donnée n'a encore été enregistrée, vous pouvez regarder le fonctionnement de la commande graph avec `;help`.")
                                embed.set_author(name="Erreur")
                                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                                embed.set_footer(text="By Nave#1960")
                    # Compte non trouvé
                    embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Merci de vérifier la syntaxe de la légende demandée et vérifiez votre pseudo Apex Legends. \nVous devez également avoir lié votre compte avec la commande `;link`")
                    embed.set_author(name="Erreur")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                    embed.set_footer(text="By Nave#1960")
                    return embed,False
        # Arguments non valides
        except:
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Mauvaise syntaxe de la commande.\n`;graph <pseudo> <légende>`\nExemple:\n`;graph PotagerDeNavets Pathfinder`")
            embed.set_author(name="Erreur")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
            embed.set_footer(text="By Nave#1960")
            return embed,False