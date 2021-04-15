import discord
import librairies
import requests
import os
class Request:
    def __init__(self):
        librairies.dotenv.load_dotenv()
        self.trackerToken = os.getenv('TRACKER_TOKEN')
    
    async def getStats(self,*arg):
        print(arg)
        if len(arg) == 1:
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Cette fonctionnalité n'est pas encore disponible")
            return embed
        if len(arg) == 2:
            pseudo = arg[0]
            if arg[1] == "PC":
                plateforme = "PC"
            elif arg[1] == "PS4":
                plateforme = "PS4"
            elif arg[1] == "XBOX":
                plateforme = "X1"
            else:
                embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="La plateforme specifiée est invalide, vous pouvez verifier la commande avec ;help")
                return embed
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
            while len(trackers) < 2:
                trackers.append(["No Data","-"])

            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Légende sélectionnée: **"+ selected +"**")
            embed.set_image(url=banner)
            embed.set_author(name=pseudo)
            embed.add_field(name="Niveau: ",value=level,inline=True)
            embed.add_field(name="Classement ",value=rank,inline=True)
            embed.add_field(name="--------------------------------",value="**Statistique de "+ selected +":**",inline=False)
            print(trackers)
            embed.add_field(name=trackers[0][0]+":",value=trackers[0][1],inline=True)
            embed.add_field(name=trackers[1][0]+":",value=trackers[1][1],inline=True)
            embed.add_field(name=trackers[2][0]+":",value=trackers[2][1],inline=True)
            return embed
        try:
            pass
        except:
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Une erreur s'est produite")
            return embed