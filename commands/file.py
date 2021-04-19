import json
import discord

class File:
    def __init__(self):
        print("ui")

    async def saveUser(self,arg,discordID,discordName):
        discordID = discordID
        discordName = discordName
        apexName = arg[0]
        plateforme = arg[1]
        with open('accountLinks/save.txt') as json_file:
            data = json.load(json_file)
            for i in data["comptes"]:
                if i["discordID"] == str(discordID):
                    embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="""Vote compte discord :"{0}" est déja lié avec votre compte Apex Legends "{1}", si cette liaison n'est pas correcte, vous pouvez la supprimer avec ;unLink""".format(discordName,apexName))
                    return embed
            
            data["comptes"].append({
                "discordID":str(discordID),
                "apexUser": str(apexName),
                "plateforme": str(plateforme)
            })
            with open('accountLinks/save.txt', 'w') as outfile:
                json.dump(data, outfile)
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description='Vote compte discord :"{0}" est bien lié avec votre compte Apex Legends "{1}"'.format(discordName,apexName))
            return embed
    
    async def delUser(self,discordID):
        with open('accountLinks/save.txt') as json_file:
            data = json.load(json_file)
            for i,compte in enumerate(data["comptes"]):
                if compte["discordID"] == str(discordID):
                    data["comptes"].pop(i)
                    with open('accountLinks/save.txt', 'w') as outfile:
                        json.dump(data, outfile)
                    embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description='Vote compte discord a été delié de votre compte Apex Legends')
                    return embed
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Votre compte n'a pas été trouvé")
            return embed

    async def getUser(self,discordID):
        with open('accountLinks/save.txt') as json_file:
            data = json.load(json_file)
            for i in data["comptes"]:
                if i["discordID"] == str(discordID):
                    return [i["apexUser"],i["plateforme"]]
