import discord
import requests
import os
import dotenv
import json
from commands.file import *
from discord.ext import tasks


File=File()

class Request:
    def __init__(self):
        dotenv.load_dotenv()
        self.trackerToken = os.getenv('TRACKER_TOKEN')
    
    async def getStats(self,arg):
        try:
            if len(arg) == 1:
                 plateforme = "PC"
            elif len(arg) == 2:
                if (arg[1] == "PC"):
                    plateforme = "PC"
                elif (arg[1] == "PS4"):
                    plateforme = "PS4"
                elif (arg[1] == "XBOX"):
                    plateforme = "X1"
                else:
                    embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="La plateforme specifiée est invalide, les plateformes valides sont `[PC | PS4 | XBOX]`.\nVous pouvez verifier la syntaxe de la commande avec `;help`")
                    embed.set_author(name="Erreur")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                    embed.set_footer(text="By Nave#1960")
                    return embed
            pseudo = arg[0]
            response = requests.get("https://api.mozambiquehe.re/bridge?version=5&platform={0}&player={1}&auth={2}".format(plateforme,pseudo,self.trackerToken)).json()
            pseudo = str(response["global"]["name"])
            level = str(response["global"]["level"])
            rank = str(response["global"]["rank"]["rankName"])+" "+str(response["global"]["rank"]["rankDiv"])
            selected = response["legends"]["selected"]["LegendName"]
            banner = response["legends"]["selected"]["ImgAssets"]["banner"]
            trackers = []
            for i,stats in enumerate(response["legends"]["selected"]["data"]):
                tracker = response["legends"]["selected"]["data"][i]["name"]
                if tracker == "Special event kills":
                    tracker = "Kills"
                elif tracker == "Special event wins":
                    tracker = "Wins"
                elif tracker == "Special event damage":
                    tracker = "Damages"

                trackers.append([tracker,response["legends"]["selected"]["data"][i]["value"]])
            while len(trackers) < 3:
                trackers.append(["No Data","-"])

            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description=f"Légende sélectionnée: **{selected}**")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
            embed.set_footer(text="By Nave#1960")
            embed.set_image(url=banner)
            embed.set_author(name=pseudo)
            embed.add_field(name="Niveau: ",value=level,inline=True)
            embed.add_field(name="Classement ",value=rank,inline=True)
            embed.add_field(name="\u200b",value=f"Statistique de **{selected}**",inline=False)
            embed.add_field(name=trackers[0][0]+":",value=trackers[0][1],inline=True)
            embed.add_field(name=trackers[1][0]+":",value=trackers[1][1],inline=True)
            embed.add_field(name=trackers[2][0]+":",value=trackers[2][1],inline=True)
            return embed
        except:
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Une erreur s'est produite, verifiez votre pseudo et votre plateforme. Vous pouvez aussi verifier la syntaxe de la commande avec `;help`. \nIl est possible que l'API de ne soit pas disponible pour le moment.")
            embed.set_author(name="Erreur")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
            embed.set_footer(text="By Nave#1960")
            return embed

    async def getMap(self):
        try:
            response = requests.get("https://api.mozambiquehe.re/maprotation?version=2&auth={0}".format(self.trackerToken)).json()
            #Carte du Battle royale
            currentMap = str(response["battle_royale"]["current"]["map"])
            changeIn = str(response["battle_royale"]["current"]["remainingTimer"])
            nextMap = str(response["battle_royale"]["next"]["map"])
            nextDuration = str(response["battle_royale"]["next"]["DurationInMinutes"])

            if (currentMap == "Kings Canyon"):
                banner = "https://media.contentapi.ea.com/content/dam/apex-legends/common/maps-page/apex-embed-image-maps-hub-kings-canyon.jpg"
            elif (currentMap == "World's Edge"):
                banner = "https://media.contentapi.ea.com/content/dam/apex-legends/common/maps-page/apex-embed-image-maps-hub-worlds-edge.jpg"
            elif (currentMap == "Olympus"):
                banner = "https://media.contentapi.ea.com/content/dam/apex-legends/common/maps-page/apex-embed-image-maps-hub-olympus.jpg"

            embed = discord.Embed(colour=discord.Colour(8722986), url="https://www.ea.com/fr-fr/games/apex-legends/maps", description=f"Carte actuelle: **{currentMap}**")
            embed.set_thumbnail(url="https://media.contentapi.ea.com/content/dam/apex-legends/common/legacy/modes/battle-royale/battle-royale-section-logo-light.png")
            embed.set_author(name="Rotation des cartes: Battle Royale")
            embed.set_image(url=banner)
            embed.add_field(name="\u200b",value=f"Temps restant: `{changeIn}`",inline=False)
            embed.add_field(name="\u200b",value=f"Prochaine carte: **{nextMap}** \nPendant : {nextDuration} minutes",inline=False)
            mapBR = embed

            #Carte arènes
            currentMap = str(response["arenas"]["current"]["map"])
            changeIn = str(response["arenas"]["current"]["remainingTimer"])
            nextMap = str(response["arenas"]["next"]["map"])
            nextDuration = str(response["arenas"]["next"]["DurationInMinutes"])

            if (currentMap == "Party crasher"):
                banner = "https://media.contentapi.ea.com/content/dam/apex-legends/images/2021/05/arenas/apex-grid-tile-arenas-maps-party-crasher.jpg"
            elif (currentMap == "Phase runner"):
                banner = "https://media.contentapi.ea.com/content/dam/apex-legends/images/2021/05/arenas/apex-grid-tile-arenas-maps-phase-runner.jpg"
            else:
                banner = "https://media.contentapi.ea.com/content/dam/apex-legends/images/2021/05/arenas/apex-grid-tile-arenas-maps-rotating.jpg"
            
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://www.ea.com/fr-fr/games/apex-legends/maps", description=f"Carte actuelle: **{currentMap}**")
            embed.set_thumbnail(url="https://media.contentapi.ea.com/content/dam/apex-legends/common/legacy/modes/arenas/arenas-section-logo-light.png")
            embed.set_footer(text="By Nave#1960")
            embed.set_author(name="Rotation des cartes: Arènes")
            embed.set_image(url=banner)
            embed.add_field(name="\u200b",value=f"Temps restant: `{changeIn}`",inline=False)
            embed.add_field(name="\u200b",value=f"Prochaine carte: **{nextMap}** \nPendant : {nextDuration} minutes",inline=False)
            mapARENA = embed
            
            return mapBR,mapARENA
        
        except Exception as e:
            print(e)
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Une erreur s'est produite")
            embed.set_author(name="Erreur")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
            embed.set_footer(text="By Nave#1960")
            return embed,None

    async def updateStats(self):
        from datetime import date
        from datetime import datetime
        now = datetime.now()
        time = f"{now.hour}H{now.minute}"
        today = date.today()
        date = today.strftime("%m/%d/%y")
        with open('accountLinks/save.txt') as json_file:
            data = json.load(json_file)
            data["refresh"] = time
            for i,compte in enumerate(data["comptes"]):
                try:
                    pseudo = data["comptes"][i]["apexUser"]
                    print(pseudo)
                    plateforme = data["comptes"][i]["plateforme"]
                    response = requests.get("https://api.mozambiquehe.re/bridge?version=5&platform={0}&player={1}&auth={2}".format(plateforme,pseudo,self.trackerToken)).json()
                    for legend in response["legends"]["all"]:
                            try:
                                Kills = 0
                                EventKills = 0
                                for tracker in response["legends"]["all"][legend]["data"]:
                                    if tracker["name"] == "Kills":
                                        Kills = tracker["value"]
                                    elif tracker["name"] == "Special event kills":
                                        EventKills = tracker["value"]
                                    
                                    if EventKills > Kills:
                                        Kills = EventKills
                                    
                                try:
                                    data["comptes"][i]["stats"][legend]["kills"].append(Kills)
                                    data["comptes"][i]["stats"][legend]["date"].append(date)
                                # Si il n'y a pas encore de profil de légende
                                except: 
                                    data["comptes"][i]["stats"][legend] = {"kills":[],"date":[]}
                                    data["comptes"][i]["stats"][legend]["kills"].append(Kills)
                                    data["comptes"][i]["stats"][legend]["date"].append(date)
                            except Exception as e:
                                pass
                except Exception as e:
                    pass

            with open('accountLinks/save.txt', 'w') as outfile:
                json.dump(data, outfile)
