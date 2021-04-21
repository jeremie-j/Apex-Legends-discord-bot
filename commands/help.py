import discord

class Help:
    async def displayHelp(self):
        embed = discord.Embed(colour=discord.Colour(8722986), url="https://discordapp.com", description='')
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/834216621152403457/8c3f25fead893348950aabcaf66d8707.png")
        embed.set_footer(text="By Nave#1960")
        embed.set_author(name="Liste des commandes")
        embed.add_field(name="Statistiques :",value="`;stats <pseudo> [plateforme]`\nPermet d'afficher les statistiques d'un joueur, les plateformes acceptés sont `[PC | PS4 | XBOX]`, la valeur par défaut est `PC` si aucune plateforme n'est pas specifiée.\nSi vous avez lié votre compte avec `;link`, la commande seule : `;stats`affichera vos statistiques",inline=False)
        embed.add_field(name="Lier un compte:",value="`;link <pseudo> <plateforme>`\nPermet de votre compte discord a un compte Apex Legends, les plateformes acceptés sont `[PC | PS4 | XBOX]`\n Vous aurez ensuite la permission d'utiliser `;stats` pour afficher les statistiques du compte lié",inline=False)
        embed.add_field(name="Délier un compte:",value="`;unlink`\nSupprime le lien entre votre compte discord et votre compte Apex Legends",inline=False)
        embed.add_field(name="Afficher la carte:",value="`;map`\nAffiche la rotation des cartes",inline=False)
        embed.add_field(name="Graphiques:",value="`;graph <pseudo> <légende>`\nLorsque vous liez votre compte Apex Legends, le bot stockera chaque jour le nombres frags de chacune de vos légendes (il faut que votre légende ait un tracker de kill sur sa bannière). Cette progression pourra ensuite être affichée à sous-forme de graphique. Idéalement, il faut laisser quelques jours pour qu'il y ait assez de données pour construire un graphique.\n**Attention :** si vous déliez votre compte, le bot arrêtera de stocker les données et **supprimera** les données existantes de votre compte.",inline=False)
        embed.add_field(name="Vos statistiques ne s'affichent pas correctement ?",value="Les statistiques de vos légendes sont recuperés à partir des trackers que vous mettez sur vos bannières, equipez en et réessayez.",inline=False)
        return embed