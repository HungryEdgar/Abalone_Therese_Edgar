Thérèse Ntabuhashe 195320
Antunes Edgar 195123


"Au sens étroit, plus fréquent, une heuristique est une méthode de calcul qui fournit 
	rapidement une solution réalisable, pas nécessairement optimale ou exacte, pour un problème d'optimisation difficile. "
							-Wikipedia

On utilisera principalement 3 stratégies pour gagner un match:
	- proximité au centre
	- regroupement des pions 
	- le nombre de pions sur le terrain


Proximité au centre (h1):
Le but du jeu c'est de pousser les pions ennemies hors du terrain de jeux. L'ennemie devra faire de même, ce qui veut dire que le centre 
du terrain est l'emplacement le plus optimal vu que, de un, on est éloigné des bords et donc il est plus difficiles de se faire ejecter, 
et de deux, une position central oblige l'ennemie à occuper le bord du terrain, facilitant ainsi son expulsion.
On calculera la distance entre chaque pions et le centre du terrain pour ensuite calculer leur différence. Le joueur maxi favorisera des 
score de h1 faibles.


Regroupement des pions (h2):
Dans Abalone, il est impossible de pousser 3 pions ou plus, ce qui veut dire que garde une certaine cohésion rend l'expulsion des pions
aliés impossible. 
Le regroupement est calculé par la distance entre chaque pions. Le joueur maxi favorise des scores de h2 faible.


Le nombre de pions sur le terrain (h3):
Encore une fois, le but du jeu est d'éliminer les pions adverses. Il en va de soit que garder un nombre de pions élevés garantie la 
survie et un nombre faible de pions enemies garantie la victoire.
Ici, le calcul se fera par la différence entre le nombre pions des deux joueurs. Le joueur maxi favorisera des scores de h3 élevés.
