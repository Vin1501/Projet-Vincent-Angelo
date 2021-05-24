 #Projet d'informatique - Vincent Breton et Angelo Mazzella#

#Préambule : 
#Nous avons choisi de travailler sur l'un de projets proposés sur le site de Mr Xavier Dupré, en apportant notre propre version nuancée.
#Il s'agira de coder le très fameux jeu de puissance 4, mais de telle manière à ce que l'utilisateur joueur puisse jouer à des variations du classique jeu de société.
#Le but est de permettre à l'utilisateur de choisir lui-même le nombre de points qu'il faut aligner pour l'emporter, ainsi que de choisir la taille de la fente dans laquelle l'on fait coulisser les jetons.
#Ceci permettra au joueur d'explorer plusieurs dynamiques de jeu, créera un nouvreau jeu qui permettra à l'utilisateur d'exprimer sa créativité en choisissant ses propres règles. #



#Partie 1 : La meilleure manière de se réprésenter la planche de puissance 4 en Python#
import numpy as np
#Le tableau ou l'on fait coulisser les jetons sera représenté par une matrice dont l'utilisateur choisira la taille


#On demande donc à l'utilisateur la taille du tableau souhaité, ainsi que le nombre de jetons qu'il faudra aligner pour l'emporter 
Abcisse = int(input("Veuillez entrer la taille de l'axe des abscisses souhaitée" ))
Ordonnée = int(input ("Veuillez entrer la taille de l'axe des ordonnées souhaitée"))
Victoire = int(input("Veuillez entrer le nombre de jetons que vous souhaitez voir alignés pour gagner"))

#NB : il est important de mettre les valeurs demandée sous forme d'entiers, sinon Python les considère comme des string. La toute première erreur de code du projet.

def createur_tableau():
    tableau = np.zeros((Abcisse, Ordonnée))
    return tableau

def lacher_jeton(tableau, ligne, col, jeton):
    tableau[ligne][col] == jeton
def Espace_valide(tableau, col):
    return tableau [Abcisse-1,col] == 0
def chercher_prochaine_ligne_ouverte(tableau, col):
    for l in range(Abcisse):
        if tableau[l][col] == 0:
            return l

A = createur_tableau()
print("Le tableau créé est :",A)

#Le jeu doit faire le différence entre le tour du joueur 1 et celui du joueur 2
Tour = 0

# Début du jeu : le jeu doit continuer tant que le bon nombre de points de la même couleur n'a pas envore été aligné. 

jeu_terminé = False 

while not jeu_terminé:
    #demander le choix du joueur 1
    if Tour == 0:
        col = int(input('Joueur 1 faites votre choix entre 0 et' + (str(Abcisse-1))) 
        if Espace_valide(tableau,col) :
            ligne = chercher_prochaine_ligne_ouverte(tableau,col)
            lacher_jeton(tableau, ligne, col, 1)
            
        
        
        
        #demander le choix joueur 2
    else: 
        col = int(input('Joueur 2 faites votre choix entre 0 et ' + str(Abcisse-1)))
        if Espace_valide(tableau,col):
            ligne = chercher_prochaine_ligne_ouverte(tableau,col)
            lacher_jeton(tableau, ligne, col, 2)
    
    #alterner entre tour du joueur 1 et tour du joueur 2 avec le reste de la division euclidienne
    Tour +=1
    Tour = Tour % 2
    
    print(tableau)
            