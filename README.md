# Apex Legends discord bot
Un bot permettant d'afficher diverses informations d'Apex legends.


## Fonctionalitées :
Avec `<Argument Obligatoire>` et `[Argument Facultatif]`.

<pseudo> sont les pseudos Origin.

### `;help`

Affiche les commandes disponibles.

## `;stats <pseudo> [plateforme]`
Plateformes : PC (par défault), PS4, XBOX.

Affiche les statistiques du joueur.

![Statistiques](https://raw.githubusercontent.com/jeremie-j/Apex-Legends-discord-bot/main/img/stats.png)

## `;map`

Affiche la rotation des cartes pour le mode Battle royale et Arène.

![Map](https://raw.githubusercontent.com/jeremie-j/Apex-Legends-discord-bot/main/img/map.png)

## `;link <pseudo> <plateforme>`

Lie votre compte Discord au compte Origin spécifié dans la commande, donne accès au `;stats` sans arguments et `;graph`.
	
## `;unlink`
	
Délie le compte Origin associé a votre Discord.
	
## `;graph <pseudo> [légende]`

Affiche un graphique de progression des kills sur la légende spécifié, le nombre de kills sur chaque légendes est enregistré tous les jours partir du jour ou vous associez votre compte avec `;link`, chaque jour rajoute un point sur le graphique.

![Graphique légende](https://raw.githubusercontent.com/jeremie-j/Apex-Legends-discord-bot/main/img/graph-legend.png)

La commande `;graph ` affiche les graphiques disponibles a l'affichage pour le pseudo spécifié, ainsi que le nombre de points sur le graphique pour chaque légende.
	
![Graphique compte](https://raw.githubusercontent.com/jeremie-j/Apex-Legends-discord-bot/main/img/graph%20.png)

## ToDo
- [x] Stats
- [x] Map
- [x] Link/Unlink
- [x] saveData
- [x] Graph
- [ ] Stats sur la légende spécifiée
- [ ] Graph "all" avec toutes les légendes
