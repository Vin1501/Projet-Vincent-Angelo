 #Projet d'informatique - Vincent Breton et Angelo Mazzella#

#Préambule : 
#Nous avons choisi de travailler sur l'un de projets proposés sur le site de Mr Xavier Dupré, en apportant notre propre version nuancée.
#Il s'agira de coder le très fameux jeu de puissance 4, mais de telle manière à ce que l'utilisateur joueur puisse jouer à des variations du classique jeu de société.
#Le but est de permettre à l'utilisateur de choisir lui-même la taille de la fente dans laquelle l'on fait coulisser les jetons.
#Ceci permettra au joueur d'explorer plusieurs dynamiques de jeu, créera un nouvreau jeu qui permettra à l'utilisateur d'exprimer sa créativité en choisissant ses propres règles. #



#Partie 1 : La matrice meilleure manière de se réprésenter la planche de puissance 4 en Python#
import numpy as np
#Le tableau ou l'on fait coulisser les jetons sera représenté par une matrice dont l'utilisateur choisira la taille


#On demande donc à l'utilisateur la taille du tableau souhaité, ainsi que le nombre de jetons qu'il faudra aligner pour l'emporter 
Colonnestableau = int(input("Veuillez entrer le nombre de colonnes du tableau souhaité" ))
Lignestableau = int(input ("Veuillez entrer le nombre de lignes du tableau souhaités"))

#NB : il est important de mettre les valeurs demandée sous forme d'entiers, sinon Python les considère comme des chaines de caractères. La toute première erreur de code du projet.

def createur_tableau():
    tableau = np.zeros((Lignestableau, Colonnestableau))
    return tableau

#A noter : la "1ere" ligne de la matrice créé est libelée comme étant la 0è

def lacher_jeton(tableau, ligne, col, jeton):
    tableau[ligne][col] = jeton
    #cette fonction change le tableau à l'emplacement joué en remplaçant le 0 par un "1" ou un "2" qui symbolise les couleurs rouges ou jaunes

def Espace_valide(tableau, col):
    return tableau [int(0)][col] == 0
#cette fonction renvoie True si l'on peut jouer dans la colonne demandée par le joueur. 


def chercher_prochaine_ligne_ouverte(tableau, col):
    for l in reversed(range(Lignestableau)):
        if tableau[l][col] == 0:
            return l
        #cette fonction a pour rôle de déterminer la ligne ou placer le jeton. On utilise "reversed" range pour partir du bas du tableau
        


def jeton_gagnant(tableau, jeton):
	# Chercher les alignements horizontaux
	for c in range(Colonnestableau-3):
		for l in range(Lignestableau):
			if tableau[l][c] == jeton and tableau[l][c+1] == jeton and tableau[l][c+2] == jeton and tableau[l][c+3] == jeton:
				return True

	# Chercher les alignements verticaux
	for c in range(Colonnestableau):
		for l in range(Lignestableau-3):
			if tableau[l][c] == jeton and tableau[l+1][c] == jeton and tableau[l+2][c] == jeton and tableau[l+3][c] == jeton:
				return True

	# Chercher les alignements diagonaux à pente positive
	for c in range(Colonnestableau-3):
		for l in range(Lignestableau-3):
			if tableau[l][c] == jeton and tableau[l+1][c+1] == jeton and tableau[l+2][c+2] == jeton and tableau[l+3][c+3] == jeton:
				return True

	# # Chercher les alignements diagonaux à pente négative
	for c in range(Colonnestableau-3):
		for l in range(3, Lignestableau):
			if tableau[l][c] == jeton and tableau[l-1][c+1] == jeton and tableau[l-2][c+2] == jeton and tableau[l-3][c+3] == jeton:
				return True



tableau1 = createur_tableau()
print("Le tableau créé est :",tableau1)

#Le jeu doit faire le différence entre le tour du joueur 1 et celui du joueur 2
Tour = 0

# Début du jeu : le jeu doit continuer tant que le bon nombre de points de la même couleur n'a pas envore été aligné. 

jeu_terminé = False 

while jeu_terminé==False:
    #demander le choix du joueur 1
    if Tour == 0:
        colonnejouée = int(input('Joueur 1 faites votre choix entre 0 et ' + (str(Colonnestableau-1)+" : ")))
        if Espace_valide(tableau1,colonnejouée)==True:
            lignejouée = chercher_prochaine_ligne_ouverte(tableau1,colonnejouée)
            lacher_jeton(tableau1, lignejouée, colonnejouée, 1)
            
        if jeton_gagnant(tableau1,1):
            jeu_terminé==True
            print("Le joueur 1 a gagné")
            break
            
        
        
        #demander le choix joueur 2
    else: 
        colonnejouée = int(input('Joueur 1 faites votre choix entre 0 et ' + (str(Colonnestableau-1)+" : ")))
        if Espace_valide(tableau1,colonnejouée)==True:
            lignejouée = chercher_prochaine_ligne_ouverte(tableau1,colonnejouée)
            lacher_jeton(tableau1, lignejouée, colonnejouée, 2)
            
        if jeton_gagnant(tableau1,2):
            jeu_terminé==True
            print("Le joueur 2 a gagné")
            break
            
    
    #alterner entre tour du joueur 1 et tour du joueur 2 avec le reste de la division euclidienne
    Tour +=1
    Tour = Tour % 2
    
    print(tableau1)
            
