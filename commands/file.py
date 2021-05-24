import json
import discord

class File:
    async def saveUser(self,arg,discordID,discordName):
        
        try:
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
                    "plateforme": str(plateforme),
                    "stats":{}
                })
                with open('accountLinks/save.txt', 'w') as outfile:
                    json.dump(data, outfile)
                embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description=f'Vote compte discord à bien été lié avec votre compte Apex Legends "{apexName}"')
                return embed
        except:
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description='Merci de bien verifier que votre commande ait la bonne syntaxe `;link <pseudo> <plateforme>`')
            return embed 
    
    async def delUser(self,discordID):
        with open('accountLinks/save.txt') as json_file:
            data = json.load(json_file)
            for i,compte in enumerate(data["comptes"]):
                if compte["discordID"] == str(discordID):
                    data["comptes"].pop(i)
                    with open('accountLinks/save.txt', 'w') as outfile:
                        json.dump(data, outfile)
                    embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description='Vote compte discord a été délié de votre compte Apex Legends.')
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
                    embed.set_footer(text="By Nave#1960")
                    embed.set_author(name="Erreur")
                    return embed
            embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description="Votre compte n'a pas été trouvé.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
            embed.set_footer(text="By Nave#1960")
            return embed

    async def getUser(self,discordID):
        with open('accountLinks/save.txt') as json_file:
            data = json.load(json_file)
            for i in data["comptes"]:
                if i["discordID"] == str(discordID):
                    return [i["apexUser"],i["plateforme"]]
