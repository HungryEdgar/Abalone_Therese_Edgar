# Abalone
Par Thérèse Ntabuhashe et Edgar Antunes

### Liste des fonctions utilisés:
	- client_s() => on crée un socket client qui va essayer de se connecter au server
	- run() => pour lancer le programe
	- subscribe() => pour se connecter au serveur
	- listen() => pour écouter sur un certain port
	- accept() => pour attendre que les clients se connectent et les accepter
	- request() => pour les requêtes fa
	- play() => pour commencer à jouer et récupérer l'état du jeux
	- give_up() => pour abondonner si jamais on ne sait pas quoi faire
    - move() => on renvoie le mouvement qu'on everra par la suite
	- find_partners() => renvoie une liste de pions qui peuvent bouger dans la même direction
	- can_move_width() => renvoie une liste de pions qui peuvent bouger ensemble
	- get_moves() => renvoie quels moves sont possible 
	- possible_moves() => renvoie des moves en fonction de la couleur des pions

### Liste des modules utilisés:
	- socket 
    - from jsonNetwork import sendJSON, receiveJSON

### Stratégie utilisé

#### Proximité au centre
Le but du jeu c'est de pousser les pions ennemies hors du terrain de jeux. L'ennemie devra faire de même, ce qui veut 
dire que le centre du terrain est l'emplacement le plus optimal vu que, de un, on est éloigné des bords et donc il est 
plus difficiles de se faire ejecter, et de deux, une position central oblige l'ennemie à occuper le bord du terrain, 
facilitant ainsi son expulsion.

#### Regroupement des pions 
Dans Abalone, il est impossible de pousser 3 pions ou plus, ce qui veut dire que garder une certaine cohésion rend 
l'expulsion des pions aliés impossible.
