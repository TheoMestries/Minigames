from typing import BinaryIO, Dict
import pickle
import random
import time

class Joueur:
        Nom:str
        ScoreDevinette:int
        ScoreAllumettes:int
        ScoreMorpion:int
        ScorePuissance:int

def affichageunscore(tabJoueur:list[Joueur],i:int):
    #
    #Procédure permettant d'afficher le score d'une personne
    #Entrée: tabJoueur,i
    #Sortie: Rien
    #
    print("Nom du Joueur : ",tabJoueur[i].Nom)
    print("Score Devinettes : ",tabJoueur[i].ScoreDevinette)
    print("Score Allumettes : ",tabJoueur[i].ScoreAllumettes)
    print("Score Morpion : ",tabJoueur[i].ScoreMorpion)
    print("Score Puissance : ",tabJoueur[i].ScorePuissance)

def Affichage(tabJoueur:list[Joueur],nJoueur:int):
    #
    #Procédure permettant d'afficher les joueurs enregistrés 
    #Entrée: tabJoueur, nJoueur
    #Sortie: Rien 
    #

    #Initialisation
    i:int
    i=0
    #Affichage des joueurs
    for i in range (0,nJoueur):
        print("--------------------------------------------------")
        affichageunscore(tabJoueur,i)

def sauvegardescore(tabJoueur:list[Joueur],nJoueur:int):
    #
    #Procédure permettant de sauvegarder les scores d'un joueur
    #Entrée: tabJoueur, nJoueur
    #Sortie: Rien
    #

    #Initialisation
    i:int
    f:BinaryIO
    #Sauvegarde des scores
    f=open("/Users/Theo2/OneDrive/Bureau/SAE101_PICAUD_MESTRIES/Score.txt","wb")
    for i in range(0,nJoueur):
        pickle.dump(tabJoueur[i],f)
    f.close()

def lectureJoueur(tabJoueur:list[Joueur],nJoueur:int):
    #
    #Procédure permettant de lire le fichier des scores
    #Entrée: tabJoueur, nJoueur
    #Sortie: Rien
    #

    #Initialisation
    f:BinaryIO
    fin:bool
    unJoueur:Joueur

    #Lecture du fichier binaire
    f=open("/Users/Theo2/OneDrive/Bureau/SAE101_PICAUD_MESTRIES/Score.txt","rb")
    fin=False
    while not fin:
        try:
            unJoueur=pickle.load(f)
            tabJoueur.append(unJoueur)
            nJoueur=nJoueur+1
        except EOFError:
            fin=True
    f.close()

def rechercheJoueur(J1:str,tabJoueur:list[Joueur],nJoueur:int)->int:
    #
    #Fonction permettant de rechercher un joueur 
    #Entrée: J1, tabJoueur, nJoueur
    #Sortie: i
    #

    #Initialisation
    i:int
    trouve:bool
    trouve=False
    i=0
    nJoueur=len(tabJoueur)
    #Recherche du joueur souhaiter
    while i<nJoueur and not trouve :
        if tabJoueur[i].Nom==J1:
            trouve=True
        else:
            i=i+1
    #Montre si le joueur a été trouvé
    if trouve:
        return i
    else:
        return-1

def saisirEntierBorneIncluse(message: str, messerr:str, limiteBasse: int, limiteHaute: int)->int:
    #
    #Fonction permettant de saisir un nombre entre deux bornes délimités
    #Entrée: message, messrr, limiteBasse, limiteHaute
    #Sortie: variable
    #

    #Initialisation
    variable: int
    #Choix de la valeur(nombre à choisir) + vérification qu'il soit dans les délimitations
    variable = int(input(message))
    while variable <= limiteBasse or variable >= limiteHaute:
        print(messerr)
        variable = int(input())
    return variable
    
def ajoutJoueur(tabJoueur:list[Joueur],nJoueur:int,Personne:str):
    #
    #Procédure permettant d'ajouter un joueur
    #Entrée: tabJoueur, nJoueur, Personne
    #Sortie: tabJoueur
    #

    #Initialisation
    unJoueur:Joueur
    #Ajout du joueur
    unJoueur=Joueur()
    unJoueur.Nom=Personne
    unJoueur.ScoreAllumettes=0
    unJoueur.ScoreDevinette=0
    unJoueur.ScoreMorpion=0
    unJoueur.ScorePuissance=0
    tabJoueur.insert(nJoueur,unJoueur)

def menu():
    #
    #Procédure permettant d'afficher le menu
    #Entrée: Rien
    #Sortie: Rien
    #

    print("Voici la liste des Options disponibles")
    print("1- Le jeu des devinettes")
    print("2- Le jeu des alumettes")
    print("3- Le jeu du morpion")
    print("4- Le jeu du puissance 4 ")
    print("5- Récapulatif des scores")
    print("6- Quitter")

def verifJoueur(Joueur:str,tabJoueur:list[Joueur],nJoueur)->bool:
    #
    #Fonction permettant de vérifier si un joueur existe
    #Entrée: Joueur, tabJoueur, nJoueur
    #Sortie: Joueurvalide
    #

    #Initialisation
    JoueurValide:bool
    pos:int
    reponse:str
    JoueurValide=False
    #Vérifie si le joueur existe dans le fichier
    pos =rechercheJoueur(Joueur,tabJoueur,nJoueur)
    if pos >=0:
        #Le joueur existe
        print("Il existe un Joueur avec de nom est-ce bien vous (Oui/Non)")
        affichageunscore(tabJoueur,pos)
        reponse =input()
        #Vérifie que c'est vous
        if reponse =='Oui':
            print("Bienvenue",tabJoueur[pos].Nom)
            JoueurValide=True
        else:
            print("Si ce n'est pas vous nous vous demandons de prendre un autre nom le votre étant déjà utilisé")
    else:
        #Le joueur n'existe pas
        print("Vous n'avez pas encore de profile nous allons vous en créer un")
        ajoutJoueur(tabJoueur,nJoueur,Joueur)
        JoueurValide=True
    return JoueurValide


def menuJeu():
    #
    #Procédure permettant d'afficher le menu du jeu
    #Entrée: Rien
    #Sortie: Rien
    #

    print("1- Joueur contre Joueur")
    print("2- Joueur contre ordinateur")
    print("3- Ordinateur contre Ordinateur")
    print("4- Quitter ")

def menuAllumettes(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant d'afficher le menu des allumettes
    #Entrée: tabJoueur, nJoueur
    #Sortie: Rien
    #
    #Initialisation
    choix:int
    choix=0
    #Affichage + choix de la partie
    print("Bienvenue dans les jeux des alumettes.")
    while choix !='4':
        print("Voici les différents choix que vous proposes le jeu des allumettes :")
        menuJeu()
        choix=input()
        if choix=='1':
            JcjAll(tabJoueur,nJoueur,J1)
        if choix =='2':
            JcOAll(tabJoueur,nJoueur,J1)
        if choix =='3':
            OcOAll()
        if choix =='4':
            print("Retour au menu principal")

def AjoutscoreAll(tabJoueur:list[Joueur],nJoueur:int,Joueur:str,temppartie:int,chiffrescore:int):
    #
    #Procédure permettant d'ajouter le score d'une partie d'allumettes
    #Entrée: tabJoueur, nJoueur, Joueur,temppartie, chiffrescore
    #Sortie: Rien
    #
    
    #Initialisation
    scoreajout:int
    pos:int
    #Recherche la position du joueur
    pos=rechercheJoueur(Joueur,tabJoueur,nJoueur)
    scoreajout=chiffrescore-temppartie
    #Ajout du score
    if scoreajout>20:
        tabJoueur[pos].ScoreAllumettes=tabJoueur[pos].ScoreAllumettes+scoreajout
        print("Le score de",Joueur,"a augmenté de",scoreajout,"points")
    else:
        tabJoueur[pos].ScoreAllumettes=tabJoueur[pos].ScoreAllumettes+20
        print("Le score de",Joueur,"a augmenté de 20 points")

def menuaDifficulté():
    #
    #Procédure permettant d'afficher la difficulté de ordinateur
    #Entrée: Rien
    #Sortie: Rien
    #
    print ("-1 Facile")
    print ("-2 Moyen")
    print ("-3 Difficile")
    
def enleveAll(Facile:int, Moyen:int, nbrAll:int)->int:
    #
    #Fonction permettant d'enlever des allumettes 
    #Entrée: Facile, Moyen, nbrAll
    #Sortie: nbrenleve
    #
    
    #Initialisation
    nbrenlève : int
    OrdiErreur:int
    nbrenlève = 0
    
    if Facile==True:
        OrdiErreur= random.randint(1,3)
    else:
        if Moyen==True:
            OrdiErreur=random.randint(1,2)
        else:
            OrdiErreur=1
    if OrdiErreur!=1:
        #Mode aléatoire
        if nbrAll >=3:
            nbrenlève=random.randint(1,3)
        else:
            nbrenlève=random.randint(1,nbrAll)
    else:
        #Mode difficile
        if nbrAll==20:
            nbrenlève=3
        if nbrAll==19:
            nbrenlève=2
        if nbrAll==18:
            nbrenlève=1
        if nbrAll==17:
            nbrenlève=1
        if nbrAll ==16:
            nbrenlève=3
        if nbrAll == 15:
            nbrenlève=2
        if nbrAll ==14:
            nbrenlève =1
        if nbrAll ==13:
            nbrenlève=1
        if nbrAll == 12:
            nbrenlève=3
        if nbrAll == 11:
            nbrenlève= 2
        if nbrAll==10:
            nbrenlève =1
        if nbrAll== 9:
            nbrenlève=1
        if nbrAll==8:
            nbrenlève=3
        if nbrAll==7:
            nbrenlève=2
        if nbrAll==6:
            nbrenlève=1
        if nbrAll==5:
            nbrenlève=1
        if nbrAll==4:
            nbrenlève=3
        if nbrAll==3:
            nbrenlève=2
        if nbrAll == 2:
            nbrenlève =1
        if nbrAll ==1:
            nbrenlève=1 
    return nbrenlève   


def JcjAll(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant à deux joueur de jouer aux Allumettes
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: Rien
    #
    
    #Initialisation
    Tour:bool
    nbrAll:int
    choixaléatoire:int
    nbrenlève:int
    t0:float
    tf:float
    J2:str
    temppartie:int
    chiffrescore:int
    chiffrescore=200
    JoueurValide=False
    ROUGE='\033[91m'
    NORMAL='\033[0m'
    print ("Bienvenue dans le mode Joueur contre Joueur ",J1)
    #Saisie du nom sur le deuxième joueur
    print ("Veuillez saisir le nom du deuxième Joueur")
    while JoueurValide !=True:
        J2=input()
        JoueurValide=verifJoueur(J2,tabJoueur,nJoueur)
    print ("Le choix de la personne commençant est choisis aléatoirement ")
    #Qui commence en premier
    choixaléatoire=random.randint(1,2)
    if choixaléatoire==1:
        Tour=False
        print("C'est",J1,"qui commencera")
    else:
        Tour=True
        print("C'est",J2,"qui commencera")
    #Début de la partie
    nbrAll=20
    nbrenlève=0
    t0=time.time()
    while nbrAll>0 :
        #Affiche le nombre d'allumettes
        if nbrAll>1:
            print("Il y a",nbrAll,"Alumettes")
            print("|"*nbrAll,ROUGE+"|"*nbrenlève+NORMAL)
        else:
            print("Il ne reste plus qu'une seule Alumette")
            print("|"*nbrAll,ROUGE+"|"*nbrenlève+NORMAL)
        
        if Tour==False:
            #La partie du premier joueur
            print("C'est au tour de",J1)
            if nbrAll >=3:
                nbrenlève=saisirEntierBorneIncluse("Veuillez saisir le nombre d'Alumettes que vous souhaites enlever entre 1 et 3 : ","Le nombre rentré n'est pas valide merci de réésayer",0,4)
            else:
                nbrenlève=saisirEntierBorneIncluse("Veuillez saisir le nombre d'Alumettes que vous souhaites enlever entre 1 et le Nombre d'Allumettes restantes : ","Le nombre rentré n'est pas valide merci de réésayer",0,nbrAll+1)
            Tour=True
        else:
            #La partie du deuxième joueur
            print("C'est au tour de",J2)
            if nbrAll >=3:
                nbrenlève=saisirEntierBorneIncluse("Veuillez saisir le nombre d'Alumettes que vous souhaites enlever entre 1 et 3 : ","Le nombre rentré n'est pas valide merci de réésayer",0,4)
            else:
                nbrenlève=saisirEntierBorneIncluse("Veuillez saisir le nombre d'Alumettes que vous souhaites enlever entre 1 et le Nombre d'Allumettes restantes : ","Le nombre rentré n'est pas valide merci de réésayer",0,nbrAll+1)
            Tour=False
        nbrAll=nbrAll-nbrenlève
        #Fin de partie
        if nbrAll==0:
            print ("Fin de la partie")
            tf=time.time()
            temppartie=int(tf)-int(t0)
    #Montre qui a gagné
    if Tour==True:
        print ("C'est donc",J2, "qui remporte la partie")
        AjoutscoreAll(tabJoueur,nJoueur,J2,temppartie, chiffrescore)
    if Tour ==False:
        print ("C'est donc",J1, "qui remporte la partie")
        AjoutscoreAll(tabJoueur,nJoueur,J1,temppartie,chiffrescore)

    
def JcOAll(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant qu'un joueur joue contre un ordinateur au jeu de Allumettes
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: Rien
    #
    
    #Initialisation
    Facile=bool
    Moyen=bool
    choix=int
    choixaléatoire:int
    nbrenlève:int
    t0:float
    tf:float
    nbrAll:int
    temppartie:int
    Tour:bool
    chiffrescore=int
    ROUGE='\033[91m'
    NORMAL='\033[0m'
    choix =0
    chiffrescore=150
    
    print ("Bienvenue dans le mode Joueur contre Ordinateur")
    #Choix de la difficulté
    print ("Veuillez choisir le niveau de difficulté de l'ordinateur")
    while choix !='1' and choix !='2' and choix !='3':
        menuaDifficulté()
        choix =input()
        if choix=='1':
            Facile=True
        if choix=='2':
            Moyen=True
            chiffrescore=chiffrescore+30
        if choix=='3':
            chiffrescore=chiffrescore+50
        if choix!='1' and choix !='2' and choix !='3':
            print("Erreur lors du choix de la difficulté. Merci de réessayer")
    #Qui commence la partie
    choixaléatoire=random.randint(1,2)
    if choixaléatoire==1:
        Tour=False
        print("C'est",J1,"qui commencera")
    else:
        Tour=True
        print("C'est l'Ordinateur qui commencera")
    #Début de la partie
    nbrAll=20
    nbrenlève=0
    t0=time.time()
    while nbrAll>0:
        #Affiche le nombre d'allumettes
        if nbrAll>1:
            print("Il y a",nbrAll,"Alumettes")
            print("|"*nbrAll,ROUGE+"|"*nbrenlève+NORMAL)  
        else:
            print("Il ne reste plus qu'une seule Alumette")
            print("|"*nbrAll,ROUGE+"|"*nbrenlève+NORMAL)
        
        if Tour==False:
            #La partie du joueur
            print("C'est au tour de",J1)
            if nbrAll >=3:
                nbrenlève=saisirEntierBorneIncluse("Veuillez saisir le nombre d'Alumettes que vous souhaites enlever entre 1 et 3 : ","Le nombre rentré n'est pas valide merci de réésayer",0,4)
            else:
                nbrenlève=saisirEntierBorneIncluse("Veuillez saisir le nombre d'Alumettes que vous souhaites enlever entre 1 et le Nombre d'Allumettes restantes : ","Le nombre rentré n'est pas valide merci de réésayer",0,nbrAll+1)
            Tour=True
        else:
            #La partie de l'ordinateur
            ("C'est au tour de l'ordinateur")
            nbrenlève=enleveAll(Facile,Moyen,nbrAll)
            print("L'ordinateur enlève", nbrenlève ,"allumettes")
            Tour=False
        nbrAll=nbrAll-nbrenlève
        #Fin de partie
        if nbrAll==0:
            print ("Fin de la partie")
            tf=time.time()
            temppartie=int(tf)-int(t0)
    #Affiche celui qui gagne
    if Tour==True:
        print ("C'est donc l'ordinateur qui remporte la partie")
    if Tour ==False:
        print ("C'est donc",J1, "qui remporte la partie")
        AjoutscoreAll(tabJoueur,nJoueur,J1,temppartie, chiffrescore)

        
def OcOAll():
    #
    #Procédure permettant à deux ordinateurs de jouer au jeu de Allumettes
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: Rien
    #
    
    #Initialisation
    Facile=bool
    Moyen=bool
    Facile2=bool
    Moyen2=bool
    choix=int
    choix2=int
    choixaléatoire:int
    nbrenlève:int
    nbrAll:int
    Tour:bool
    ROUGE='\033[91m'
    NORMAL='\033[0m'
    
    print ("Bienvenue dans le mode Ordinateur contre Ordinateur")
    #Choix de la difficulté des ordinateurs
    print ("Veuillez choisir le niveau de difficulté de l'ordinateur 1")
    while choix !='1' and choix !='2' and choix !='3':
        menuaDifficulté()
        choix =input()
        if choix=='1':
            print("Vous avez choisi la difficulté Facile")
            Facile=True
        if choix=='2':
            print("Vous avez choisi la difficulté Moyenne")
            Moyen=True
        if choix=='3':
            print("Vous avez choisi la difficulté Difficile")
        if choix!='1' and choix !='2' and choix !='3':
            print("Erreur lors du choix de la difficulté. Merci de rééssaueyer")
    print ("Veuillez choisir le niveau de difficulté de l'ordinateur 2")
    while choix2 !='1' and choix2 !='2' and choix2 !='3':
        menuaDifficulté()
        choix2 =input()
        if choix2=='1':
            print("Vous avez choisi la difficulté Facile")
            Facile2=True
        if choix2=='2':
            print("Vous avez choisi la difficulté Moyenne")
            Moyen2=True
        if choix2=='3':
            print("Vous avez choisi la difficulté Difficile")
        if choix2!='1' and choix2 !='2' and choix2 !='3':
            print("Erreur lors du choix de la difficulté. Merci de rééssaueyer")
    #Qui commence la partie
    choixaléatoire=random.randint(1,2)
    if choixaléatoire==1:
        Tour=False
        print("C'est l'ordianteur 1 qui commencera")
    else:
        Tour=True
        print("C'est l'ordinateur 2 qui commencera")
    #Début de la partie
    nbrAll=20
    nbrenlève=0
    while nbrAll>0:
        #Affichage du nombre d'allumettes
        if nbrAll>1:
            print("Il y a",nbrAll,"Alumettes")
            print("|"*nbrAll,ROUGE+"|"*nbrenlève+NORMAL)
        else:
            print("Il ne reste plus qu'une seule Alumette")
            print("|"*nbrAll,ROUGE+"|"*nbrenlève+NORMAL)
        
        if Tour==False:
            #La partie du permier ordinateur
            ("C'est au tour de l'ordinateur 1")
            nbrenlève=enleveAll(Facile,Moyen,nbrAll)
            print("L'ordinateur 1 enlève", nbrenlève ,"allumettes")
            Tour=True
        else:
            #La partie du deuxième ordinateur
            ("C'est au tour de l'ordinateur 2")
            nbrenlève=enleveAll(Facile2,Moyen2,nbrAll)
            print("L'ordinateur 2 enlève", nbrenlève ,"allumettes")
            Tour=False
        nbrAll=nbrAll-nbrenlève
        if nbrAll==0:
            print ("Fin de la partie")
    #Affiche qui gagne
    if Tour==True:
        print ("C'est donc l'ordinateur 2 qui remporte la partie")
    if Tour ==False:
        print ("C'est donc l'ordinateur 1 qui remporte la partie")

def AjoutscoreDev(tabJoueur:list[Joueur],nJoueur:int,Joueur:str,Nbrcoup:int,limite:int):
    #
    #Procédure permettant d'ajouter le score au jeu des devinettes
    #Entrée: tabJoueur, nJoueur, Joueur, Nbrcoup, limite
    #Sortie: tabJoueur
    #
    
    #Initialisation
    scoreajout:int
    pos:int
    difficulte:int
    #Recherche la position du joueur
    pos=rechercheJoueur(Joueur,tabJoueur,nJoueur)
    if limite >= 10000:
        difficulte=3
    else:
        if limite >=1000:
            difficulte=2
        else:
            difficulte=1
    #Ajoute le score
    scoreajout = 170-(5*Nbrcoup)
    scoreajout=scoreajout*difficulte
    if scoreajout>20:
        tabJoueur[pos].ScoreDevinette=tabJoueur[pos].ScoreDevinette+scoreajout
        print("Le score de",Joueur,"a augmenté de",scoreajout,"points")
    else:
        tabJoueur[pos].ScoreDevinette=tabJoueur[pos].ScoreDevinette+20
        print("Le score de",Joueur,"a augmenté de 20 points")

def JcJDev(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant à deux joueurs de jouer au jeu des devinettes
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: Rien
    #
    
    #Initialisation
    J2 : str
    premier_a_joue : int
    demande_commence : str
    verif_demande : bool
    demande_limite : str
    verif_limite : bool
    nombre : int
    limite : int
    trouver : bool
    recherche : int
    Joueurscore:bool
    JoueurValide:bool
    coup:int
    coup=0
    JoueurValide=False
    print ("Bienvenue dans le mode Joueur contre Joueur ",J1)
    #Saisie du nom sur le deuxième joueur 
    print ("Veuillez saisir le nom du deuxième Joueur")
    while JoueurValide !=True:
        J2=input()
        JoueurValide=verifJoueur(J2,tabJoueur,nJoueur)
    #Demande qu'elle joueur va commencer
    verif_demande = False
    while not verif_demande:
        demande_commence = str(input("Voulez-vous que le choix du joueur (qui commence/qui choisie le nombre) soit aléatoire (oui ou non)? "))
        if demande_commence=='oui':
            premier_a_joue = random.randint(1,2)
            verif_demande = True
        elif demande_commence=='non':
            premier_a_joue=int(input("Lequelle des deux joueurs veut commencé (1 pour joueur 1 et 2 pour joueur 2)? "))
            verif_demande = True
        else:
            print("La valeur choisi n'est pas un choix possible") 
         
           
    #Decide de la limite
    verif_limite = False
    while not verif_limite:
        demande_limite = str(input("Voulez-vous décider de la limite, la limite de base étant de 10000 (oui ou non)? ")) 
        if demande_limite=='oui':
            ##print("Le maximum est de ")
            limite = int(input("Quel est la limite du jeu ? "))
            while limite < 2 : # la limite doit etre supérieur à 1 qui est le plus petit nombre possible 
                print("Erreur, la limite n'est pas supérieur à 1")
                limite = int(input("Choisissez votre limite ? "))
            verif_limite = True
        elif demande_limite=='non':
            print("La limite est de 10000")
            limite = 10000
            verif_limite = True
        else:
            print("La valeur choisi n'est pas un choix possible")                
    
    #Demande le nombre a trouvé
    #Le 1er joueur qui commence(joueur 2 qui cherche le nombre)
    if premier_a_joue == 1:
        print(J1,"décide du nombre à rechercher")
        Joueurscore=False
        nombre = int(input("Choisissez votre nombre ? "))
        while nombre < 1 or nombre > limite:
            print("Erreur, le nombre n'est pas supérieur ou égale à 1 ou inférieur à la limite")
            nombre = int(input("Choisissez votre nombre ? "))  
    #Le 2eme joueur qui commence(joueur 1 qui cherche le nombre)
    elif premier_a_joue==2 :
        print(J2,"decide du nombre à rechercher")
        Joueurscore=True
        nombre = int(input("Choisissez votre nombre ? "))
        while nombre < 1 or nombre > limite:
            print("Erreur, le nombre n'est pas supérieur ou égale à 1 ou inférieur à la limite")
            nombre = int(input("Choisissez votre nombre ? "))

    else:
        print("La valeur choisi n'est pas un choix possible ")
    
    #Trouver le nombre
    if Joueurscore==True:
        print("C'est maintenant à",J1,"de joué :")
    else:
        print("C'est maintenant à",J2,"de joué :")
    trouver=False
    while not trouver:
        recherche = int(input("Saisir un nombre ? "))
        while recherche < 1 or recherche > limite:
            print("Erreur, le nombre n'est pas supérieur ou égale à 1 ou inférieur à la limite")
            recherche = int(input("Saisir votre nombre ? ")) 
        if recherche == nombre:
            print("C'est gagné")
            trouver = True
        elif recherche < nombre:
            print(recherche,"est trop petit")
        else:
            print(recherche,"est trop grand")
        coup=coup+1
    #Affiche qui a gagné et lui ajoute des points 
    if Joueurscore==True:
        print(J1,"a trouvé le nombre en ",coup,"de coups")
        AjoutscoreDev(tabJoueur,nJoueur,J1,coup,limite)
    else:
        print(J2,"a trouvé le nombre en ",coup,"de coups")
        AjoutscoreDev(tabJoueur,nJoueur,J2,coup,limite)

def JcODev(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant à un joueur de jouer aux devinettes avec un ordinateur 
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: Rien
    #

    #Initialisetion
    premier_a_joue : int
    demande_commence : str
    verif_demande: bool
    demande_limite : str
    verif_limite : bool
    nombre : int
    limite : int
    trouver : bool
    recherche : int
    coup:int
    a : int
    b : int
    m : int
    coup=0
    
    #Demande qu'elle joueur va commencer
    verif_demande = False
    while not verif_demande :
        demande_commence = str(input("Voulez-vous que le choix de qui commence se face aléatoirement(oui ou non)? "))
        if demande_commence=='oui':
            premier_a_joue = random.randint(1,2)
            verif_demande = True
        elif demande_commence=='non':
            premier_a_joue=int(input("Qui voulez-vous que commencer à jouer(1 pour joueur 1 et 2 pour ordinateur)? "))
            verif_demande = True
        else:
            print("La valeur choisi n'est pas un choix possible") 
    
    #Decide de la limite
    verif_limite = False
    while not verif_limite:
        demande_limite = str(input("Voulez-vous décider de la limite, la limite de base étant de 10000 (oui ou non)? ")) 
        if demande_limite=='oui':
            limite = int(input("Quel est la limite du jeu ? "))
            while limite < 2 : # la limite doit etre supérieur à 1 qui est le plus petit nombre possible 
                print("Erreur, la limite n'est pas supérieur à 1")
                limite = int(input("Choisissez votre limite ? "))
            verif_limite = True
        elif demande_limite=='non':
            print("La limite est de 10000")
            limite = 10000
            verif_limite = True
        else:
            print("La valeur choisi n'est pas un choix possible")              
    
    #Demande le nombre a trouvé
    #Le 1er joueur qui commence(joueur 2 qui cherche le nombre)
    if premier_a_joue == 1:
        print(J1,"décide du nombre à rechercher")
        nombre = int(input("Choisissez votre nombre ? "))
        while nombre < 1 or nombre > limite:
            print("Erreur, le nombre n'est pas supérieur ou égale à 1 ou inférieur à la limite")
            nombre = int(input("Choisissez votre nombre ? "))     
    #Le 2eme joueur qui commence(joueur 1 qui cherche le nombre)
    elif premier_a_joue==2 :
        print("L'ordinateur decide le nombre à rechercher")
        nombre = random.randint(1,limite)
    else:
        print("La valeur choisi n'est pas un choix possible ")  
        
    #Trouver le nombre
    trouver=False
    a=1
    b=limite-1
    if premier_a_joue!=1:
        #La partie pour le joueur
        print(J1,"à la recherche du nombre :")
        while not trouver:
            recherche = int(input("Saisir un nombre ? "))
            while recherche < 1 or recherche > limite:
                print("Erreur, le nombre n'est pas supérieur ou égale à 1 ou inférieur à la limite")
                recherche = int(input("Saisir votre nombre ? ")) 
            if recherche == nombre:
                print("C'est gagné")
                trouver = True
            elif recherche < nombre:
                print(recherche,"est trop petit")
            else:
                print(recherche,"est trop grand")
            coup=coup+1
        print(J1, "a trouvré le chiffre en",coup,"coups")
        AjoutscoreDev(tabJoueur,nJoueur,J1,coup,limite)
        
    else:
        #La partie de l'ordinateur
        print("C'est à l'ordinateur de trouver le nombre")
        while not trouver:
            m=(a+b)//2
            while a<=b:
                if m == nombre:
                    trouver = True
                    print(m)
                    print("L'ordinateur à gagné")
                    a = a+b
                elif m < nombre:
                    a = m+1
                    print(m,"est trop petit")
                else:
                    b = m-1 
                    print(m,"est trop grand")
                m=(a+b)//2
            coup=coup+1
        print("L'ordinateura trouvré le chiffre en",coup,"coups")

def OcODev():
    #
    #Procédure permettant à deux ordinateurs de jouer aux devinettes
    #Entrée: Rien
    #Sortie: Rien
    #
    
    #Initialisation
    demande_limite : str
    verif_demande : bool
    nombre : int
    limite : int
    trouver : bool
    a : int
    b : int
    m : int 
    coup:int
    coup=0

    #Decide de la limite
    verif_demande = False
    while not verif_demande:
        demande_limite = str(input("Voulez vous décider de la limite du jeu Ordinateur contre Ordinateur, la limite de base étant de 10000(oui ou non)? "))
        if demande_limite=='oui':
            limite = int(input("Quel est la limite ? "))
            while limite <2 :
                print("Erreur, la limite n'est pas supérieur à 1")
                limite = int(input("Choisissez la limite"))
            verif_demande = True
        elif demande_limite=='non':
            print("La limite est de 10000")
            limite = 10000
            verif_demande = True
        else : 
            print("La valeur choisi n'est pas un choix possible") 
        
    #Décide du nombre à trouver
    nombre = random.randint(1,limite)
    print("Le premier ordinateur a choisit",nombre,"comme nombre a chercher")
    
    #Trouver le nombre
    trouver = False
    a = 1
    b = limite-1
    while not trouver:
        m=(a+b)//2
        while a<=b:
            if m == nombre:
                trouver = True
                print (m)
                print("L'ordinateur à gagné")
                a = a+b
            elif m < nombre:
                a = m+1
                print(m,"est trop petit")
            else:
                b = m-1 
                print(m,"est trop grand")
            m=(a+b)//2
            coup=coup+1
        print ("L'ordinateur a trouvé le chiffre en",coup,"coups")

def menuDevinette(tabJoueur:list[Joueur],nJoueur,J1):
    #
    #Procédure permettant de choisir le mode de jeu sur le jeu de devinettes
    #Entrée: tabJoueur, nJoueur
    #Sortie: choix
    #
    
    #Initialisation
    choix : int
    choix = 0
    
    print("Bienvenue dans le jeu des devinettes")
    #Choix du mode de jeu
    while choix!=4:
        menuJeu() 
        choix=int(input("Quel est votre choix ? "))
        while choix<1 or choix >4 :
            print("Erreur lors de la saisie, veuillez réessayer")
            choix = int(input("Quel est votre choix ? "))
        if choix==1:
            print("Vous avez choisi Joueur contre Joueur")
            JcJDev(tabJoueur,nJoueur,J1)
        elif choix==2:
            print("Vous avez choisi Joueur contre Ordinateur")
            JcODev(tabJoueur,nJoueur,J1)
        elif choix==3:
            print("Vous avez choisi Ordinateur contre Ordinateur")
            OcODev()
        elif choix==4:
            print("Vous avez choisi le menu principale")

def AjoutscoreMorp(tabJoueur:list[Joueur],nJoueur:int,Joueur:str,temppartie:int,chiffrescore:int):
    #
    #Procédure permettant d'ajouter le score au morpion
    #Entrée: tabJoueur, nJoueur, Joueur, temppartie, chiffrescore
    #Sortie: tabJoueur
    #
    
    #Initialisation
    scoreajout:int
    pos:int
    #Recherche la position du joueur
    pos=rechercheJoueur(Joueur,tabJoueur,nJoueur)
    scoreajout=chiffrescore-temppartie
    scoreajout=scoreajout*3
    #Ajout du score
    if scoreajout>20:
        tabJoueur[pos].ScoreMorpion=tabJoueur[pos].ScoreMorpion+scoreajout
        print("Le score de",Joueur,"a augmenté de",scoreajout,"points")
    else:
        tabJoueur[pos].ScoreMorpion=tabJoueur[pos].ScoreMorpion+20
        print("Le score de",Joueur,"a augmenté de 20 points")

def JcJMorp(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant à deux joueurs de jouer au morpion
    #Entrée: tabJouer, nJoueur, J1
    #Sortie: rien
    #
    
    #Initialisation
    J2:str
    premier_a_joue : int
    demande_commence : str
    verif_demande : bool
    coup : int
    nombre : int
    gagner : bool
    tour : bool
    ok:bool
    chiffrescore:int
    t0:float
    tf:float
    ROUGE='\033[91m'
    VERT='\033[92m'
    NORMAL='\033[0m'
    temppartie:int
    JoueurValide:bool
    matrice : list[int]
    matrice = [1,2,3,4,5,6,7,8,9]
    JoueurValide=False
    chiffrescore=120

    print ("Bienvenue dans le mode Joueur contre Joueur ",J1)
    #Saisie du nom du deuxième joueur
    print ("Veuillez saisir le nom du deuxième Joueur")
    while JoueurValide !=True:
        J2=input()
        JoueurValide=verifJoueur(J2,tabJoueur,nJoueur)

    #Demande qu'elle joueur va commencer
    verif_demande = False
    while not verif_demande:
        demande_commence = str(input("Voulez-vous que le choix du joueur (qui commence/qui choisie le nombre) soit aléatoire (oui ou non)? "))
        if demande_commence=='oui':
            premier_a_joue = random.randint(1,2)
            verif_demande = True
        elif demande_commence=='non':
            premier_a_joue=int(input("Lequelle des deux joueurs veut commencé (1 pour joueur 1 et 2 pour joueur 2)? "))
            verif_demande = True
        else:
            print("La valeur choisi n'est pas un choix possible")
        
    #qIndique qui joue en premier
    if premier_a_joue==1:
        print("C'est",J1 ,"qui commence")
        tour=True    
    else :
        print("C'est",J2, "qui commence")
        tour=False
    
    #Début de la partie
    coup = 0
    gagner = False
    t0=time.time()
    while coup < 9 and not gagner:
        coup = coup + 1 
        if tour==True:
            #Partie du premier joueur
            affichage(matrice)
            ok=False
            #Choix + vérification de la case
            while not ok:
                print (J1,"choisissez une case entre 1 et 9: ")
                nombre = int(input())-1
                while nombre<0 or nombre>8:
                    print("Erreur dans la saisie")
                    print (J1,"choisissez une case entre 1 et 9: ")
                    nombre = int(input())-1
                if matrice[nombre]==VERT+'X'+NORMAL or matrice[nombre]==ROUGE+'O'+NORMAL:
                    print("Placement occuper, la case est déjà prise")
                else:
                    ok=True
            #Place le choix dans la case
            matrice[nombre]=VERT+'X'+NORMAL
            tour=False
            #Vérifie s'il a gagné
            gagner=verifMorp(matrice, gagner)
            
        else:
            #Partie du deuxième joueur
            affichage(matrice)
            ok=False
            #Choix + vérification da la case
            while not ok:
                print (J2,"choisissez une case entre 1 et 9: ")
                nombre = int(input())-1
                while nombre<0 or nombre>8:
                    print("Erreur dans la saisie")
                    print (J2,"choisissez une case entre 1 et 9: ")
                    nombre = int(input())-1
                if matrice[nombre]==VERT+'X'+NORMAL or matrice[nombre]==ROUGE+'O'+NORMAL:
                    print("Placement occuper, la case est déjà prise")
                else:
                    ok=True
            #Place le choix dans la case
            matrice[nombre]=ROUGE+'O'+NORMAL
            tour=True
            gagner=verifMorp(matrice, gagner) 
        #Partie fini, c'est une égalité
        if coup==9:
            affichage(matrice)
            print("La partie est finie, c'est une égalité")

    #Indique qui a gagné et ajoute le score 
    if gagner:
        tf=time.time()
        temppartie=int(tf)-int(t0)
        if tour==False:
            print(J1, "remporte la partie en" ,temppartie,"secondes")
            AjoutscoreMorp(tabJoueur,nJoueur,J1,temppartie,chiffrescore)
        
        else:
            print(J2, "remporte la partie en" ,temppartie,"secondes")
            AjoutscoreMorp(tabJoueur,nJoueur,J2,temppartie,chiffrescore)


def affichage(matrice):
    #
    #Procédure permettant d'afficher la jeu du morpion
    #Entrée: matrice
    #Sortie: rien
    #
    
    #Initialisation
    l:int

    #Affichage du jeu 
    for l in range (len(matrice)):
        if (l+1)%3==0 and l!=8 :
            print(str(matrice[l]))
            print("--|---|---")
        elif (l+1)%3==0:
            print(str(matrice[l]))
        else:
            print(matrice[l], "| ", end="") 
    print("") 

def verifMorp(matrice:list[int],gagner:bool):
     #
    #Fonction permettant de vérifier l'un des deux participant a gagné
    #Entrée: matrice, gagner, Joueur
    #Sortie: gagner
    #
    ROUGE='\033[91m'
    VERT='\033[92m'
    NORMAL='\033[0m'
    #Première participant
    if (matrice[0]==VERT+'X'+NORMAL and matrice[1]==VERT+'X'+NORMAL and matrice[2]==VERT+'X'+NORMAL) or (matrice[3]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[5]==VERT+'X'+NORMAL) or (matrice[6]==VERT+'X'+NORMAL and matrice[7]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL) or (matrice[0]==VERT+'X'+NORMAL and matrice[3]==VERT+'X'+NORMAL and matrice[6]==VERT+'X'+NORMAL) or (matrice[1]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[7]==VERT+'X'+NORMAL) or (matrice[2]==VERT+'X'+NORMAL and matrice[5]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL) or (matrice[0]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL) or (matrice[2]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[6]==VERT+'X'+NORMAL): 
        affichage(matrice)
        gagner=True
    #Deuxième participant  
    if (matrice[0]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL) or (matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[6]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL) or (matrice[1]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL): 
        affichage(matrice)
        gagner=True
    return gagner

def JcOMorp(tabJoueur:list[Joueur],nJoueur,J1:str):
    #
    #Fonction permettant qu'un joueur puisse jouer au Morpion contre un ordinateur
    #Entrée: nom du joueur, TabJoueur, nJoueur
    #Sortie: TabJoueur
    #
    
    #Initialisation
    ROUGE='\033[91m'
    VERT='\033[92m'
    NORMAL='\033[0m'
    chiffrescore:int
    premier_a_joue : int
    demande_commence : str
    verif_demande : bool
    tour : bool
    difficulte:int
    coup : int
    ok : bool
    t0:float
    tf:float
    temppartie:int
    nombre : int
    gagner : bool
    val : int 
    matrice : list[int]
    matrice = [1,2,3,4,5,6,7,8,9]
    chiffrescore=120
    
        
    #Choisir le niveau de l'ordinateur
    menuaDifficulté()
    difficulte=int(input("Choisir la difficulté de l'ordinateur ? "))
    while difficulte<1 or difficulte>3:
        print("Erreur de saisie, veuillez recommencer")
        difficulte=int(input("Choisir la difficulté de l'ordinateur ? "))
    if difficulte==1:
        chiffrescore=chiffrescore-30
    elif difficulte==2:
        chiffrescore=chiffrescore-15
    else :
        chiffrescore=chiffrescore+10

    #Demande qui commence
    verif_demande=False
    while not verif_demande:
        demande_commence = str(input("Voulez-vous que le choix du joueur (qui commence/qui choisie le nombre) soit aléatoire (oui ou non)? "))
        if demande_commence=='oui':
            premier_a_joue = random.randint(1,2)
            verif_demande = True
        elif demande_commence=='non':
            premier_a_joue=int(input("Lequelle des deux joueurs veut commencé (1 pour joueur 1 et 2 pour ordinateur 2)? "))
            verif_demande = True
        else:
            print("La valeur choisi n'est pas un choix possible")
    
    #Qui joue en premier
    if premier_a_joue==1:
        print("C'est",J1,"qui commence")
        tour=True    
    else:
        print("C'est l'ordinateur qui commence")
        tour=False

    #Lancement de la partie    
    coup = 0
    gagner = False
    affichage(matrice)
    t0=time.time()
    while coup < 9 and not gagner:
        #La partie du joueur
        if tour==True:
            ok=False
            #Vérification du choix de la case
            while not ok:
                nombre = int(input("Choisissez une case entre 1 et 9: "))-1
                while nombre<0 or nombre>8:
                    print("Erreur dans la saisie")
                    nombre = int(input("Choisissez une case : "))-1
                if matrice[nombre]=='X' or matrice[nombre]=='O':
                    print("Placement occuper, la case est déjà prise")
                else:
                    ok=True
            #Mise en place du choix de la case
            matrice[nombre]=VERT+'X'+NORMAL
            tour=False
            affichage(matrice)
            #Vérifie si le joueur a gagné
            gagner=verifMorp(matrice, gagner)
            coup = coup + 1    
        
        #La partie de l'ordinateur    
        else:    
            ok=False
            #Vérification de la case
            while not ok:
                #Niveau selon le choix de la difficulté
                if difficulte==1:
                    val=random.randint(1,3)
                elif difficulte==2:
                    val=random.randint(1,2)
                else:
                    val=1
                #Choix de la case
                if val!=1:
                    nombre=random.randint(0,8)   
                else:
                    nombre=coup_ordi_Morpion(coup,matrice)
                #Vérifie si la case est vide
                if matrice[nombre]==VERT+'X'+NORMAL or matrice[nombre]==ROUGE+'O'+NORMAL:
                    ok=False
                else:
                    ok=True
            #Mise en place du choix de la case
            matrice[nombre]=ROUGE+'O'+NORMAL
            tour=True
            affichage(matrice)
            #Vérifie si l'ordinateur a gagné
            gagner=verifMorp(matrice, gagner)
            coup = coup + 1    
        #Fin de partie lorsque c'est une égalité
        if coup==9 and not gagner:
            print("La parti est finie, c'est une égalité")
    tf=time.time()
    temppartie=int(tf)-int(t0)
    if gagner==True:
        if tour==False:
            print(J1, "remporte la partie en" ,temppartie,"secondes")
            AjoutscoreMorp(tabJoueur,nJoueur,J1,temppartie,chiffrescore)
            
        else:
            print("L'ordinateur remporte la partie en" ,temppartie,"secondes")

    
def OcOMorp():
    #
    #Fonction permettant à deux ordinateurs de jouer au Morpion
    #Entrée: Rien
    #Sortie: Rien
    #
    ROUGE='\033[91m'
    VERT='\033[92m'
    NORMAL='\033[0m'
    premier_a_joue : int
    tour : bool
    coup : int
    ok:bool
    t0:float
    tf:float
    temppartie:int
    nombre : int
    gagner : bool
    matrice : list[int]
    matrice = [1,2,3,4,5,6,7,8,9]
    difficulte:int
    difficulte2:int
    difficulte=0
    difficulte2=0
    #Choix de la difficulté du premier ordinateur
    print("Veuillez choisir la difficulté de l'ordinateur 1")
    while difficulte!='1' and difficulte!='2' and difficulte!='3':
        menuaDifficulté()
        difficulte=input("Choisir la difficulté de l'ordinateur 1 ? ")
    #Choix de la difficulté du deuxième ordinateur
    print("Veuillez choisir la difficulté de l'ordinateur 2")
    while difficulte2!='1' and difficulte2!='2' and difficulte2!='3':
        menuaDifficulté()
        difficulte2=input("Choisir la difficulté de l'ordinateur 2 ? ")

    #qui joue
    premier_a_joue=random.randint(1,2)
    if premier_a_joue==1:
        print("C'est l'ordinateur 1 qui commence")
        tour=True    
    else:
        print("C'est l'ordinateur 2 qui commence")
        tour=False
    
    #Lancement de la partie
    nombre=0    
    coup = 0
    gagner = False
    affichage(matrice)
    t0=time.time()
    while coup < 9 and not gagner:
        #La partie du premier ordinateur
        if tour==True:
            ok=False
            #Choix + vérification de la case
            while not ok:
                if difficulte==1:
                    val=random.randint(1,3)
                elif difficulte==2:
                    val=random.randint(1,2)
                else:
                    val=1
                #Choix de la case
                if val!=1:
                    nombre=random.randint(0,8)   
                else:
                    nombre=coup_ordi_Morpion(coup,matrice)
                #Vérifie si la case est vide
                if matrice[nombre]==VERT+'X'+NORMAL or matrice[nombre]==ROUGE+'O'+NORMAL:
                    ok=False
                else:
                    ok=True
            #Mise en place du choix de la case
            matrice[nombre]=VERT+'X'+NORMAL
            tour=False
            affichage(matrice)
            #Vérifie si l'ordinateur a gagné
            gagner=verifMorp(matrice, gagner)
            coup = coup + 1
                     
        #La partie du deuxième ordinateur    
        else:
            ok=False
            #Choix + vérification de la case
            while not ok:
                if difficulte2==1:
                    val=random.randint(1,3)
                elif difficulte2==2:
                    val=random.randint(1,2)
                else:
                    val=1
                #Choix de la case
                if val!=1:
                    nombre=random.randint(0,8)   
                else:
                    nombre=coup_ordi_Morpion(coup,matrice)
                #Vérifie si la case est vide
                if matrice[nombre]==VERT+'X'+NORMAL or matrice[nombre]==ROUGE+'O'+NORMAL:
                    ok=False
                else:
                    ok=True
            #Mise en place du choix de la case
            matrice[nombre]=ROUGE+'O'+NORMAL
            tour=True
            affichage(matrice)
            #Vérifie si l'ordinateur a gagné
            gagner=verifMorp(matrice, gagner)
            coup = coup + 1
        
        #Fin de la partie
        if coup==9 and not gagner:
            print("La parti est finie, c'est une égalité")
    tf=time.time()
    temppartie=int(tf)-int(t0)      
    if gagner==True:
        if tour==False:
            print("L'ordinateur 1 remporte la partie en",temppartie,"secondes")
            
        else:
            print("L'ordinateur 2 remporte la partie en" ,temppartie,"secondes")


def affichage(matrice):
    #
    #Fonction permettant d'afficher la jeu du morpion
    #Entrée: matrice
    #Sortie: rien
    #
    
    #Initialisation
    i : int
    
    #Affichage du jeu 
    for l in range (len(matrice)):
        if (l+1)%3==0 and l!=8 :
            print(str(matrice[l]))
            print("--|---|---")
        elif (l+1)%3==0:
            print(str(matrice[l]))
        else:
            print(matrice[l], "| ", end="") 
    print("") 




def coup_ordi_Morpion(coup:int,matrice:list[int])->int:
    #
    #Fonction permettant de faire les coups de l'ordinateur
    #Entrée: le nombre de coup, la matrice
    #Sortie: le nombre
    #
    
    #Initialiastion
    ROUGE='\033[91m'
    VERT='\033[92m'
    NORMAL='\033[0m'
    nombre : int
    contre : bool
    choix : int
    coup : int
    nombre=0
    contre=False
    
    #Quand le coup est égale à 0 soit quand l'ordinateur joue en premier
    if coup==0:
        #Le choix est l'un des quatre côtés du jeu
        choix=random.randint(0,3)
        if choix==0:
            nombre=0
        elif choix==1:
            nombre=2
        elif choix==2:
            nombre=6
        else:
            nombre=8
            
    #Quand le coup est égale à 1 soit le deuxième a joué dans la partie
    if coup==1:
        #Quand le permier coup est un côté, l'ordinateur joue au milieu
        if matrice[0]==VERT+'X'+NORMAL or matrice[2]==VERT+'X'+NORMAL or matrice[6]==VERT+'X'+NORMAL or matrice[8]==VERT+'X'+NORMAL or matrice[0]==ROUGE+'O'+NORMAL or matrice[2]==ROUGE+'O'+NORMAL or matrice[6]==ROUGE+'O'+NORMAL or matrice[8]==ROUGE+'O'+NORMAL:
            nombre=4
        #Quand le permier coup est le milieu, l'ordinateur joue un côté
        if matrice[4]==VERT+'X'+NORMAL:
            choix=random.randint(0,3)
            if choix==0:
                nombre=0
            elif choix==1:
                nombre=2
            elif choix==2:
                nombre=6
            else:
                nombre=8
                
    #Quand le coup est supérieur à 1 soit le joueur et l'ordinateur ont joué leurs permiers coups
    if coup != 1:
        #Pour contrer le joueur
        #Première ligne 
        if matrice[0]==VERT+'X'+NORMAL and matrice[1]==VERT+'X'+NORMAL and matrice[2]!=ROUGE+'O'+NORMAL:
            nombre=2
            contre=True
        if matrice[1]==VERT+'X'+NORMAL and matrice[2]==VERT+'X'+NORMAL and matrice[0]!=ROUGE+'O'+NORMAL:
            nombre=0
            contre=True
        if matrice[0]==VERT+'X'+NORMAL and matrice[2]==VERT+'X'+NORMAL and matrice[1]!=ROUGE+'O'+NORMAL:
            nombre=1
            contre=True
        #Deuxième ligne
        if matrice[3]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[5]!=ROUGE+'O'+NORMAL:
            nombre=5
            contre=True
        if matrice[4]==VERT+'X'+NORMAL and matrice[5]==VERT+'X'+NORMAL and matrice[3]!=ROUGE+'O'+NORMAL:
            nombre=3
            contre=True
        if matrice[3]==VERT+'X'+NORMAL and matrice[5]==VERT+'X'+NORMAL and matrice[4]!=ROUGE+'O'+NORMAL:
            nombre=4
            contre=True
        #Troisième ligne
        if matrice[6]==VERT+'X'+NORMAL and matrice[7]==VERT+'X'+NORMAL and matrice[8]!=ROUGE+'O'+NORMAL:
            nombre=8
            contre=True
        if matrice[7]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL and matrice[6]!=ROUGE+'O'+NORMAL:
            nombre=6
            contre=True
        if matrice[6]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL and matrice[7]!=ROUGE+'O'+NORMAL:
            nombre=7
            contre=True

        #Permière colonne
        if matrice[0]==VERT+'X'+NORMAL and matrice[3]==VERT+'X'+NORMAL and matrice[6]!=ROUGE+'O'+NORMAL:
            nombre=6
            contre=True
        if matrice[3]==VERT+'X'+NORMAL and matrice[6]==VERT+'X'+NORMAL and matrice[0]!=ROUGE+'O'+NORMAL:
            nombre=0
            contre=True
        if matrice[0]==VERT+'X'+NORMAL and matrice[6]==VERT+'X'+NORMAL and matrice[3]!=ROUGE+'O'+NORMAL:
            nombre=3
            contre=True
        #Deuxième colonne
        if matrice[1]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[7]!=ROUGE+'O'+NORMAL:
            nombre=7
            contre=True
        if matrice[4]==VERT+'X'+NORMAL and matrice[7]==VERT+'X'+NORMAL and matrice[1]!=ROUGE+'O'+NORMAL:
            nombre=1
            contre=True
        if matrice[1]==VERT+'X'+NORMAL and matrice[7]==VERT+'X'+NORMAL and matrice[4]!=ROUGE+'O'+NORMAL:
            nombre=4
            contre=True
        #Troixième colonne
        if matrice[2]==VERT+'X'+NORMAL and matrice[5]==VERT+'X'+NORMAL and matrice[8]!=ROUGE+'O'+NORMAL:
            nombre=8
            contre=True
        if matrice[5]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL and matrice[2]!=ROUGE+'O'+NORMAL:
            nombre=2
            contre=True
        if matrice[2]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL and matrice[5]!=ROUGE+'O'+NORMAL:
            nombre=5
            contre=True
                        
        #Première diagonale
        if matrice[0]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[8]!=ROUGE+'O'+NORMAL:
            nombre=8
            contre=True
        if matrice[4]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL and matrice[0]!=ROUGE+'O'+NORMAL:
            nombre=0
            contre=True
        if matrice[0]==VERT+'X'+NORMAL and matrice[8]==VERT+'X'+NORMAL and matrice[4]!=ROUGE+'O'+NORMAL:
            nombre=4
            contre=True
        #Deuxième diagonale
        if matrice[2]==VERT+'X'+NORMAL and matrice[4]==VERT+'X'+NORMAL and matrice[6]!=ROUGE+'O'+NORMAL:
            nombre=6
            contre=True
        if matrice[4]==VERT+'X'+NORMAL and matrice[6]==VERT+'X'+NORMAL and matrice[2]!=ROUGE+'O'+NORMAL:
            nombre=2
            contre=True
        if matrice[2]==VERT+'X'+NORMAL and matrice[6]==VERT+'X'+NORMAL and matrice[4]!=ROUGE+'O'+NORMAL:
            nombre=4 
            contre=True
                        
        #Pour gagner à l'ordinateur
        #Première ligne
        if matrice[0]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL and matrice[2]!=VERT+'X'+NORMAL:
            nombre=2
            contre=True
        if matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[0]!=VERT+'X'+NORMAL:
            nombre=0
            contre=True
        if matrice[0]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[1]!=VERT+'X'+NORMAL:
            nombre=1
            contre=True
        #Deuxième ligne
        if matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]!=VERT+'X'+NORMAL:
            nombre=5
            contre=True
        if matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[3]!=VERT+'X'+NORMAL:
            nombre=3
            contre=True
        if matrice[3]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[4]!=VERT+'X'+NORMAL:
            nombre=4
            contre=True
        #Troixième ligne
        if matrice[6]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL and matrice[8]!=VERT+'X'+NORMAL:
            nombre=8
            contre=True
        if matrice[7]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[6]!=VERT+'X'+NORMAL:
            nombre=6
            contre=True
        if matrice[6]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[7]!=VERT+'X'+NORMAL:
            nombre=7
            contre=True

        #Première colonne 
        if matrice[0]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[6]!=VERT+'X'+NORMAL:
            nombre=6
            contre=True
        if matrice[3]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL and matrice[0]!=VERT+'X'+NORMAL:
            nombre=0
            contre=True
        if matrice[0]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL and matrice[3]!=VERT+'X'+NORMAL:
            nombre=3
            contre=True
        #Deuxième colonne
        if matrice[1]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[7]!=VERT+'X'+NORMAL:
            nombre=7
            contre=True
        if matrice[4]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL and matrice[1]!=VERT+'X'+NORMAL:
            nombre=1
            contre=True
        if matrice[1]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL and matrice[4]!=VERT+'X'+NORMAL:
            nombre=4
            contre=True
        #Troixième colonne
        if matrice[2]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[8]!=VERT+'X'+NORMAL:
            nombre=8
            contre=True
        if matrice[5]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[2]!=VERT+'X'+NORMAL:
            nombre=2
            contre=True
        if matrice[2]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[5]!=VERT+'X'+NORMAL:
            nombre=5
            contre=True
                        
        #Première diagonale
        if matrice[0]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[8]!=VERT+'X'+NORMAL:
            nombre=8
            contre=True
        if matrice[4]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[0]!=VERT+'X'+NORMAL:
            nombre=0
            contre=True
        if matrice[0]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[4]!=VERT+'X'+NORMAL:
            nombre=4
            contre=True
        #Deuxième diagonale
        if matrice[2]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[6]!=VERT+'X'+NORMAL:
            nombre=6
            contre=True
        if matrice[4]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL and matrice[2]!=VERT+'X'+NORMAL:
            nombre=2
            contre=True
        if matrice[2]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL and matrice[4]!=VERT+'X'+NORMAL:
            nombre=4
            contre=True
        
        #Si il n'y a pas à contrer
        if contre==False:
            nombre=random.randint(0,8)
    return nombre

def menuMorpion(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant de choisir le mode de jeu du morpion
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: fonction de son choix
    #
    
    #Initialisation
    choix : int
    choix = 0
    
    print("Bienvenue dans le morpion")
    menuJeu() 
    #Choix du mode de jeu
    while choix!=4:
        choix=int(input("Quel est votre choix ? "))
        while choix<1 or choix >4 :
            print("Erreur lors de la saisie, veuillez réessayer")
            choix = int(input("Quel est votre choix ? "))
        if choix==1:
            print("Vous avez choisi Joueur contre Joueur")
            JcJMorp(tabJoueur,nJoueur,J1)
            menuJeu()
        elif choix==2:
            print("Vous avez choisi Joueur contre Ordinateur")
            JcOMorp(tabJoueur,nJoueur,J1)
            menuJeu()
        elif choix==3:
            print("Vous avez choisi Ordinateur contre Ordinateur")
            OcOMorp()
            menuJeu()
        elif choix==4:
            print("Vous avez choisi le menu principale")


def AjoutscorePuissance4(tabJoueur:list[Joueur],nJoueur:int,Joueur:str,temppartie:int,chiffrescore:int):
    #
    #Procédure permettant d'ajouter le score du puissance 4 
    #Entrée: tabJoueur, nJoueur, Joueur, temppartie,chiffrescore
    #Sortie: scoreajout
    #
    
    #Initialisation
    scoreajout:int
    pos:int
    #Rechercher la position du joueur
    pos=rechercheJoueur(Joueur,tabJoueur,nJoueur)
    scoreajout=chiffrescore-temppartie
    #Ajout du score
    if scoreajout>20:
        tabJoueur[pos].ScorePuissance=tabJoueur[pos].ScorePuissance+scoreajout
        print("Le score de",Joueur,"a augmenté de",scoreajout,"points")
    else:
        tabJoueur[pos].ScorePuissance=tabJoueur[pos].ScorePuissance+20
        print("Le score de",Joueur,"a augmenté de 20 points")


def joueparfaitpuissance4(matrice:list[str]):
     #
    #Fonction permettant de faire les coups des ordinateurs dans le jeu du puissance 4
    #Entrée: matrice
    #Sortie: pos
    #
    
    #Initialisation
    ROUGE='\033[91m'
    BLEU='\033[94m'
    NORMAL='\033[0m'
    pos:int
    pos=-1

    #Coups
    if ((matrice[1]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL) or (matrice[21]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL and matrice[7]==BLEU+'O'+NORMAL) or (matrice[8]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[1]== ROUGE+'O'+NORMAL and matrice[2]== ROUGE+'O'+NORMAL and matrice[3]== ROUGE+'O'+NORMAL) or (matrice[21]== ROUGE+'O'+NORMAL and matrice[14]== ROUGE+'O'+NORMAL and matrice[7]== ROUGE+'O'+NORMAL) or (matrice[8]== ROUGE+'O'+NORMAL and matrice[16]== ROUGE+'O'+NORMAL and matrice[24]== ROUGE+'O'+NORMAL)) and  matrice[7]!="O" and  matrice[0]=="O":
        pos=1
    if ((matrice[0]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL)or (matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL)or (matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL) or (matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL)or (matrice[0]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)or (matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL)or (matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL))and matrice[8]!="O" and  matrice[1]=="O":
        pos=2
    if ((matrice[0]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL)or (matrice[1]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL) or (matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL) or (matrice[9]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL)or (matrice[10]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)or (matrice[1]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL) or (matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[9]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL)or(matrice[10]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL))and matrice[9]!="O" and  matrice[2]=="O":
        pos=3
    if ((matrice[0]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL) or (matrice[1]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL) or (matrice[2]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL) or (matrice[4]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL) or (matrice[10]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[21]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL) or (matrice[11]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL) or (matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL) or (matrice[10]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL) or (matrice[11]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL)) and matrice[10]!="O" and  matrice[3]=="O":
        pos=4
    if ((matrice[1]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL) or (matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL) or (matrice[3]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL) or (matrice[11]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[10]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL) or (matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[3]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL) or (matrice[11]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[10]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL)) and matrice[11]!="O" and  matrice[4]=="O":
        pos=5
    if ((matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL) or(matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL) or (matrice[26]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL) or(matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL) or (matrice[26]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL))and matrice[12]!="O" and  matrice[5]=="O":
        pos=6
    if ((matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL) or (matrice[27]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[27]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL)) and matrice[13]!="O" and matrice[6]=="O":
        pos=7
    if ((matrice[8]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[28]==BLEU+'O'+NORMAL and matrice[21]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL) or (matrice[15]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL) or (matrice[8]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[21]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL) or (matrice[15]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL)) and matrice[14]!="O" and matrice[7]=="O":
        pos=1
    if ((matrice[7]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL)or (matrice[29]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL) or  (matrice[0]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[16]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL) or (matrice[7]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL)or (matrice[29]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL)) and matrice[15]!="O" and matrice[8]=="O":
        pos=2
    if ((matrice[7]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[8]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or (matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[30]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL) or (matrice[1]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[17]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL) or (matrice[21]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL) or (matrice[7]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[8]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL) or (matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL) or (matrice[1]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[17]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)) and matrice[16]!="O" and  matrice[9]=="O":
        pos=3
    if ((matrice[7]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL) or (matrice[8]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or (matrice[9]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[11]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[22]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL) or (matrice[28]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL)or (matrice[2]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL) or (matrice[18]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL) or (matrice[7]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL) or (matrice[8]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL) or (matrice[9]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[11]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL)or (matrice[2]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL) or (matrice[18]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL)) and  matrice[17]!="O" and  matrice[10]=="O": 
        pos=4
    if ((matrice[8]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[10]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL) or (matrice[18]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL) or (matrice[29]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[27]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL) or (matrice[8]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[10]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL) or (matrice[18]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[27]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)) and   matrice[18]!="O" and  matrice[11]=="O": 
        pos=5
    if ((matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or (matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL) or (matrice[19]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL)or (matrice[30]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL) or (matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL) or (matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL) or (matrice[19]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL)or (matrice[30]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL)) and matrice[19]!="O" and matrice[12]=="O":
        pos=6
    if ((matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[34]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[34]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL)) and  matrice[20]!="O" and  matrice[13]=="O": 
        pos=7
    if ((matrice[15]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[35]==BLEU+'O'+NORMAL and matrice[28]==BLEU+'O'+NORMAL and matrice[21]==BLEU+'O'+NORMAL)or (matrice[22]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL) or(matrice[15]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[35]==ROUGE+'O'+NORMAL and matrice[28]==ROUGE+'O'+NORMAL and matrice[21]==ROUGE+'O'+NORMAL)or (matrice[22]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL))and  matrice[21]!="O" and  matrice[14]=="O": 
        pos=1
    if ((matrice[14]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[22]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[36]==BLEU+'O'+NORMAL)or (matrice[21]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL)or(matrice[7]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL)or(matrice[14]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[36]==ROUGE+'O'+NORMAL)or (matrice[21]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)or(matrice[7]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL)) and matrice[22]!="O" and matrice[15]=="O":
        pos=2
    if ((matrice[14]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[15]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL)or (matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL) or (matrice[28]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL)or (matrice[22]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL) or (matrice[0]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[8]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL) or (matrice[14]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[15]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL)or (matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL)or (matrice[22]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[8]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL)) and  matrice[23]!="O" and  matrice[16]=="O":
        pos=3
    if ((matrice[14]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL) or (matrice[15]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[16]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[18]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL) or (matrice[35]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL) or (matrice[29]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL)or (matrice[41]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL)or (matrice[33]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL) or (matrice[25]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL) or (matrice[14]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL) or (matrice[15]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL) or (matrice[18]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL) or (matrice[35]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL)or (matrice[41]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL)or (matrice[33]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL)) and matrice[24]!="O" and  matrice[17]=="O":
        pos=4
    if ((matrice[15]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[17]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[25]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL)or (matrice[34]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[26]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL) or (matrice[36]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[30]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL)or (matrice[15]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL) or (matrice[17]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL)or (matrice[34]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[26]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL)) and  matrice[25]!="O" and  matrice[18]=="O":
        pos=5
    if ((matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[26]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL) or (matrice[37]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[13]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[3]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL) or (matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL) or (matrice[26]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[13]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[3]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL)) and matrice[26]!="O" and matrice[19]=="O":
        pos=6
    if ((matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[27]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL and matrice[41]==BLEU+'O'+NORMAL) or (matrice[38]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL) or(matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL) or (matrice[27]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL and matrice[41]==ROUGE+'O'+NORMAL) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL)) and  matrice[27]!="O" and  matrice[20]=="O":
        pos =7
    if ((matrice[22]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[15]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[15]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)) and  matrice[28]!="O" and  matrice[21]=="O":
        pos=1
    if ((matrice[21]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[28]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[16]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL) or (matrice[14]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL) or(matrice[21]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL) or (matrice[14]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL)) and  matrice[29]!="O" and  matrice[22]=="O":
        pos=2
    if ((matrice[21]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL)or (matrice[22]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL)or (matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL)or (matrice[35]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL)or (matrice[29]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or (matrice[17]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL) or (matrice[39]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[7]==BLEU+'O'+NORMAL) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL)or (matrice[22]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL)or (matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL)or (matrice[35]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL)or (matrice[29]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL) or (matrice[17]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL) or (matrice[39]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL)) and matrice[30]!="O" and matrice[23]=="O":
        pos=3
    if ((matrice[21]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL) or (matrice[22]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL) or (matrice[25]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL) or (matrice[36]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[30]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[18]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL) or (matrice[40]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL) or (matrice[32]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL) or (matrice[16]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[0]==BLEU+'O'+NORMAL) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[18]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL) or (matrice[40]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL) or (matrice[32]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[0]==ROUGE+'O'+NORMAL))and matrice[31]!="O" and  matrice[24]=="O":
        pos=4
    if ((matrice[22]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL)or (matrice[24]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL) or (matrice[37]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL) or (matrice[41]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[33]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL) or (matrice[17]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL)or (matrice[24]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL) or (matrice[41]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[33]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL) or (matrice[17]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL)) and matrice[32]!="O" and matrice[25]=="O":
        pos=5
    if ((matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL) or (matrice[38]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[34]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[18]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL) or (matrice[34]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL) or (matrice[18]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL)) and  matrice[33]!="O" and  matrice[26]=="O":
        pos=6
    if ((matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL) or (matrice[19]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL) or (matrice[19]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL)) and  matrice[34]!="O" and  matrice[27]=="O":
        pos=7
    if ((matrice[29]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL) or (matrice[22]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL)) and  matrice[35]!="O" and  matrice[28]=="O":
        pos=1
    if ((matrice[28]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL)or (matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL)  or (matrice[35]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL) or  (matrice[28]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL)or (matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL)  or (matrice[35]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL)) and  matrice[36]!="O" and  matrice[29]=="O":
        pos=2
    if ((matrice[28]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL) or (matrice[29]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL)or (matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL) or (matrice[36]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL) or (matrice[38]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL) or  (matrice[28]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL)or (matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL))and  matrice[37]!="O" and  matrice[30]=="O":
        pos=3
    if ((matrice[28]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL) or (matrice[29]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL) or (matrice[30]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL) or (matrice[32]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL) or (matrice[37]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or (matrice[25]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL) or (matrice[39]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL) or (matrice[23]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[7]==BLEU+'O'+NORMAL) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL) or (matrice[32]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL) or (matrice[39]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL)) and matrice[38]!="O" and matrice[31]=="O":
        pos=4
    if ((matrice[29]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL) or (matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL) or (matrice[38]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[40]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL) or (matrice[24]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL) or  (matrice[29]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL) or (matrice[40]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL)) and  matrice[39]!="O" and  matrice[32]=="O":
        pos=5
    if ((matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL) or (matrice[41]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL) or  (matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL) or (matrice[41]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL)) and  matrice[40]!="O" and  matrice[33]=="O":
        pos=6
    if ((matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL) or (matrice[26]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL) or (matrice[26]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL)) and  matrice[41]!="O" and  matrice[34]=="O":
        pos=7
    if ((matrice[36]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL) or (matrice[29]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or  (matrice[36]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL)) and  matrice[35]=="O":
        pos=1
    if ((matrice[35]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL)or (matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL) or (matrice[30]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL) or (matrice[35]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL)or (matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL)) and  matrice[36]=="O":
        pos=2
    if ((matrice[35]==BLEU+'O'+NORMAL and matrice[36]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL) or (matrice[36]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL)or (matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL) or (matrice[31]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL) or  (matrice[35]==ROUGE+'O'+NORMAL and matrice[36]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL)or (matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL)) and  matrice[37]=="O":
        pos=3
    if ((matrice[35]==BLEU+'O'+NORMAL and matrice[36]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL)or (matrice[36]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL) or (matrice[37]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL) or (matrice[39]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL and matrice[41]==BLEU+'O'+NORMAL)or (matrice[30]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL) or (matrice[32]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL) or (matrice[35]==ROUGE+'O'+NORMAL and matrice[36]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL)or (matrice[36]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL) or (matrice[39]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL and matrice[41]==ROUGE+'O'+NORMAL)or (matrice[30]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL) or (matrice[32]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL)) and  matrice[38]=="O":
        pos=4
    if ((matrice[36]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL)or (matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL)or (matrice[38]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL and matrice[41]==BLEU+'O'+NORMAL)or (matrice[31]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL)or (matrice[36]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL)or (matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL)or (matrice[38]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL and matrice[41]==ROUGE+'O'+NORMAL)or (matrice[31]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL)) and  matrice[39]=="O":
        pos=5
    if ((matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL)or(matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL and matrice[41]==BLEU+'O'+NORMAL)or (matrice[32]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL)or (matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL)or(matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL and matrice[41]==ROUGE+'O'+NORMAL)or (matrice[32]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL)) and  matrice[40]=="O":
        pos=6
    if ((matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL) or (matrice[33]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL) or (matrice[33]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL))and  matrice[41]=="O":
        pos=7
    return pos 

def JCOPuissance4 (tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant à un joueur de joue contre un ordinateur au jeu du puissance 4
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: rien
    #
    
    #Initialisation
    premier_a_joue : int
    demande_commence : str
    verif_demande : bool
    coup : int
    nombre : int
    gagner : bool
    tour : bool
    ok:bool
    tourfinis:bool
    t0:float
    tf:float
    pos:int
    ROUGE='\033[91m'
    BLEU='\033[94m'
    NORMAL='\033[0m'
    temppartie:int
    chiffrescore:int
    difficulte:int
    aleatoire:int
    matrice : list[str]
    matrice = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
    difficulte=0
    print ("Bienvenue dans le mode Joueur contre Ordinateur ",J1)
    verif_demande=False
    chiffrescore=200

    print("Veuillez choisir la difficulté de l'ordinateur")
    #Demande de choisir la difficulté de l'ordinateur
    while difficulte!='1' and difficulte!='2' and difficulte!='3':
        menuaDifficulté()
        difficulte=input("Choisir la difficulté de l'ordinateur ? ")
        if difficulte=='1':
            chiffrescore=chiffrescore-120
        if difficulte=='2':
            chiffrescore=chiffrescore-80
    

    #Demande qui commence la partie
    while not verif_demande:
        demande_commence = str(input("Voulez-vous que le choix du joueur qui commence soit aléatoire (oui ou non)? "))
        if demande_commence=='oui':
            premier_a_joue = random.randint(1,2)
            verif_demande = True
        elif demande_commence=='non':
            premier_a_joue=int(input("Lequelle des deux joueurs veut commencé (1 pour joueur 1 et 2 pour ordinateur )? "))
            verif_demande = True
        else:
            print("La valeur choisi n'est pas un choix possible")
        
        
    #Affiche celui qui joue ne premier 
    if premier_a_joue==1:
        print("C'est",J1 ,"qui commence")
        tour=True    
    else :
        print("C'est l'ordinateur qui commence")
        tour=False
    
    #Début de la partie
    coup = 0
    gagner = False
    t0=time.time()
    while coup < 42 and not gagner:
        coup = coup + 1 
        if tour==True:
            #Partie du joueur
            tourfinis=False
            #Vérification de la case
            while not tourfinis:
                affichepuissance(matrice)
                ok=False
                #Choix de la case
                while not ok:
                    print (J1,"choisissez une colonne  entre 1 et 7: ")
                    nombre = int(input())
                    while nombre<1 or nombre>7:
                        print("Erreur dans la saisie")
                        print (J1,"choisissez une colonne  entre 1 et 7: ")
                        nombre = int(input())
                    ok=True
                tourfinis=ecritpuissance(matrice,tourfinis,nombre,tour)
                if tourfinis==False:     
                    print ("Vous ne pouvez pas mettre de jeton dans cette colonne , elle est complète ")
                
            tour=False
            gagner=verifpuissance(matrice, gagner)
            
        else:
            #Partie de l'ordinateur
            affichepuissance(matrice)
            tourfinis=False
            #Choix de la case + vérification de cette case
            while not tourfinis:
                if difficulte=='1':
                    aleatoire=2
                elif difficulte=='2':
                    aleatoire=random.randint(1,2)
                else:
                    aleatoire=1
                
                if aleatoire==1:
                    pos=joueparfaitpuissance4(matrice)
                    if pos==-1:
                        nombre=random.randint(1,7)
                    else:
                        nombre=pos
                else:
                    nombre=random.randint(1,7)
                tourfinis=ecritpuissance(matrice,tourfinis,nombre,tour)
            tour=True
            gagner=verifpuissance(matrice, gagner) 

        #Fin de partie si toutes les cases sont remplies donc c'est un égalité   
        if coup==42:
            affichepuissance(matrice)
            print("La partie est finie, c'est une égalité")
    tf=time.time()
    temppartie=int(tf)-int(t0)
    #Dit qui a gagné + ajout du score
    if gagner==True:
        if tour==False:
            print(J1, "remporte la partie en" ,temppartie,"secondes")
            AjoutscorePuissance4(tabJoueur,nJoueur,J1,temppartie,chiffrescore)
            
        else:
            print("L'ordinateur remporte la partie en" ,temppartie,"secondes")
       
                    

def menupuissance4(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant de choisir le mode de jeu sur le puissance 4
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: choix du mode
    #
    
    #Initialisation
    choix:int 
    choix=0
    print("Bienvenue dans le puissance 4")
    menuJeu() 
    #Choix du mode de jeu
    while choix!=4:
        choix=int(input("Quel est votre choix ? "))
        while choix<1 or choix >4 :
            print("Erreur lors de la saisie, veuillez réessayer")
            choix = int(input("Quel est votre choix ? "))
        if choix==1:
            print("Vous avez choisi Joueur contre Joueur")
            JcJPuissance4(tabJoueur,nJoueur,J1)
            menuJeu()
        elif choix==2:
            print("Vous avez choisi Joueur contre Ordinateur")
            JCOPuissance4(tabJoueur,nJoueur,J1)
            menuJeu()
        elif choix==3:
            print("Vous avez choisi Ordinateur contre Ordinateur")
            OCOPuissance4()
            menuJeu()
        elif choix==4:
            print("Vous avez choisi le menu principale")

def affichepuissance(matrice):
    #
    #Procédure afin d'afficher le tableau du puissance 4
    #Entrée: matrice
    #Sortie: rien
    #
    
    #Affichage
    l:int
    print("  1   2   3   4   5   6   7  ")
    print("-----------------------------")
    for l in range (len(matrice)):
        if  l==0 or  l==7 or l==14 or l== 21 or l==28 or l==35 or l==42:
            print("|",matrice[l],"| ",end="")
          
        elif (l+1)%7==0 and l!=41 :
            print(matrice[l],"|")
            print("|---|---|---|---|---|---|---|")
        
        else:
            print(matrice[l], "| ", end="") 
    print("") 
    print("-----------------------------")

def verifpuissance(matrice:list[int],gagner:bool):
    #
    #Fonction permettant de vérifier si l'un des deux participant a gagner
    #Entrée: matrice, gagner
    #Sortie: gagner
    #
    ROUGE='\033[91m'
    BLEU='\033[94m'
    NORMAL='\033[0m'
    #Vérification du premier participant
    if (matrice[35]==BLEU+'O'+NORMAL and matrice[36]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL ) or (matrice[36]==BLEU+'O'+NORMAL and matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL ) or (matrice[37]==BLEU+'O'+NORMAL and matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL ) or (matrice[38]==BLEU+'O'+NORMAL and matrice[39]==BLEU+'O'+NORMAL and matrice[40]==BLEU+'O'+NORMAL and matrice[41]==BLEU+'O'+NORMAL ) or (matrice[28]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL ) or (matrice[29]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL ) or (matrice[30]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL ) or (matrice[31]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL ) or (matrice[21]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL ) or (matrice[22]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL )  or (matrice[23]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL ) or (matrice[24]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL ) or (matrice[14]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL ) or (matrice[15]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL ) or (matrice[16]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL ) or (matrice[17]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL ) or  (matrice[7]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL )  or (matrice[8]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL )  or (matrice[9]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL )  or (matrice[10]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL ) or (matrice[0]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL ) or (matrice[1]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL ) or (matrice[2]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL ) or (matrice[3]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL ) or (matrice[35]==BLEU+'O'+NORMAL and matrice[28]==BLEU+'O'+NORMAL and matrice[21]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL ) or (matrice[28]==BLEU+'O'+NORMAL and matrice[21]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL and matrice[7]==BLEU+'O'+NORMAL ) or (matrice[21]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL and matrice[7]==BLEU+'O'+NORMAL and matrice[0]==BLEU+'O'+NORMAL ) or (matrice[36]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL ) or (matrice[29]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL ) or (matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL ) or (matrice[37]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL ) or (matrice[30]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL ) or (matrice[23]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL ) or (matrice[38]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL ) or (matrice[31]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL ) or (matrice[24]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL ) or (matrice[39]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL ) or (matrice[32]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL ) or (matrice[25]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL ) or (matrice[40]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL ) or (matrice[33]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL ) or (matrice[26]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL ) or (matrice[41]==BLEU+'O'+NORMAL and matrice[34]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL ) or  (matrice[34]==BLEU+'O'+NORMAL and matrice[27]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL ) or (matrice[27]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL ) or (matrice[35]==BLEU+'O'+NORMAL and matrice[29]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL ) or (matrice[36]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL ) or (matrice[29]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL ) or (matrice[23]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[5]==BLEU+'O'+NORMAL ) or (matrice[30]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL ) or (matrice[24]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[12]==BLEU+'O'+NORMAL and matrice[6]==BLEU+'O'+NORMAL ) or (matrice[37]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL ) or (matrice[31]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[13]==BLEU+'O'+NORMAL ) or (matrice[38]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[20]==BLEU+'O'+NORMAL ) or (matrice[41]==BLEU+'O'+NORMAL and matrice[33]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL ) or (matrice[33]==BLEU+'O'+NORMAL and matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL ) or (matrice[25]==BLEU+'O'+NORMAL and matrice[17]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[1]==BLEU+'O'+NORMAL ) or (matrice[40]==BLEU+'O'+NORMAL and matrice[32]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL ) or (matrice[32]==BLEU+'O'+NORMAL and matrice[24]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL ) or (matrice[24]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL and matrice[0]==BLEU+'O'+NORMAL ) or (matrice[39]==BLEU+'O'+NORMAL and matrice[31]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL ) or  (matrice[31]==BLEU+'O'+NORMAL and matrice[23]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[7]==BLEU+'O'+NORMAL ) or (matrice[29]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL ) or (matrice[38]==BLEU+'O'+NORMAL and matrice[30]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[14]==BLEU+'O'+NORMAL ) or (matrice[28]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL ) or (matrice[22]==BLEU+'O'+NORMAL and matrice[16]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[4]==BLEU+'O'+NORMAL ) or (matrice[21]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[9]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL ) or (matrice[34]==BLEU+'O'+NORMAL and matrice[26]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL )or (matrice[26]==BLEU+'O'+NORMAL and matrice[18]==BLEU+'O'+NORMAL and matrice[10]==BLEU+'O'+NORMAL and matrice[2]==BLEU+'O'+NORMAL ) or (matrice[29]==BLEU+'O'+NORMAL and matrice[22]==BLEU+'O'+NORMAL and matrice[15]==BLEU+'O'+NORMAL and matrice[8]==BLEU+'O'+NORMAL ) or (matrice[27]==BLEU+'O'+NORMAL and matrice[19]==BLEU+'O'+NORMAL and matrice[11]==BLEU+'O'+NORMAL and matrice[3]==BLEU+'O'+NORMAL ):
        affichepuissance(matrice)
        
        gagner=True
    #Vérification du deuxième participant
    if (matrice[35]==ROUGE+'O'+NORMAL and matrice[36]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL ) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL ) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL ) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[39]==ROUGE+'O'+NORMAL and matrice[40]==ROUGE+'O'+NORMAL and matrice[41]==ROUGE+'O'+NORMAL ) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL ) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL ) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL ) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL ) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL ) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL )  or (matrice[23]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL ) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL ) or (matrice[14]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL ) or (matrice[15]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL ) or (matrice[16]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL ) or (matrice[17]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL ) or  (matrice[7]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL )  or (matrice[8]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL )  or (matrice[9]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL )  or (matrice[10]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL ) or (matrice[0]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL ) or (matrice[1]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL ) or (matrice[2]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL ) or (matrice[3]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL ) or (matrice[35]==ROUGE+'O'+NORMAL and matrice[28]==ROUGE+'O'+NORMAL and matrice[21]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL ) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[21]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL ) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL and matrice[0]==ROUGE+'O'+NORMAL ) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL ) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL ) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL ) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL ) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL ) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL ) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL ) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL ) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL ) or (matrice[39]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL ) or (matrice[32]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL ) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL ) or (matrice[40]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL ) or (matrice[33]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL ) or (matrice[26]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL ) or (matrice[41]==ROUGE+'O'+NORMAL and matrice[34]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL ) or  (matrice[34]==ROUGE+'O'+NORMAL and matrice[27]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL ) or (matrice[27]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL ) or (matrice[35]==ROUGE+'O'+NORMAL and matrice[29]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL ) or (matrice[36]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL ) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL ) or (matrice[23]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[5]==ROUGE+'O'+NORMAL ) or (matrice[30]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL ) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[12]==ROUGE+'O'+NORMAL and matrice[6]==ROUGE+'O'+NORMAL ) or (matrice[37]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL ) or (matrice[31]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[13]==ROUGE+'O'+NORMAL ) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[20]==ROUGE+'O'+NORMAL ) or (matrice[41]==ROUGE+'O'+NORMAL and matrice[33]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL ) or (matrice[33]==ROUGE+'O'+NORMAL and matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL ) or (matrice[25]==ROUGE+'O'+NORMAL and matrice[17]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[1]==ROUGE+'O'+NORMAL ) or (matrice[40]==ROUGE+'O'+NORMAL and matrice[32]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL ) or (matrice[32]==ROUGE+'O'+NORMAL and matrice[24]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL ) or (matrice[24]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL and matrice[0]==ROUGE+'O'+NORMAL ) or (matrice[39]==ROUGE+'O'+NORMAL and matrice[31]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL ) or  (matrice[31]==ROUGE+'O'+NORMAL and matrice[23]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[7]==ROUGE+'O'+NORMAL ) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL ) or (matrice[38]==ROUGE+'O'+NORMAL and matrice[30]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[14]==ROUGE+'O'+NORMAL ) or (matrice[28]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL ) or (matrice[22]==ROUGE+'O'+NORMAL and matrice[16]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[4]==ROUGE+'O'+NORMAL ) or (matrice[21]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[9]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL ) or (matrice[34]==ROUGE+'O'+NORMAL and matrice[26]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL )or (matrice[26]==ROUGE+'O'+NORMAL and matrice[18]==ROUGE+'O'+NORMAL and matrice[10]==ROUGE+'O'+NORMAL and matrice[2]==ROUGE+'O'+NORMAL ) or (matrice[29]==ROUGE+'O'+NORMAL and matrice[22]==ROUGE+'O'+NORMAL and matrice[15]==ROUGE+'O'+NORMAL and matrice[8]==ROUGE+'O'+NORMAL ) or (matrice[27]==ROUGE+'O'+NORMAL and matrice[19]==ROUGE+'O'+NORMAL and matrice[11]==ROUGE+'O'+NORMAL and matrice[3]==ROUGE+'O'+NORMAL ):
        affichepuissance(matrice)
        
        gagner=True
    return gagner 

def ecritpuissance (matrice: list[str],tourfinis:bool,nombre:int,tour:bool)->bool:
    #
    #Fonction permettant d'écrire dans la matrice
    #Entrée: matrice, tourfinis, nombre, tour
    #Sortie: tourfinis
    # 

    ROUGE='\033[91m'
    BLEU='\033[94m'
    NORMAL='\033[0m'
    #Premier participant
    if tour==True:
        if nombre==1:
            if matrice[35]=="O":
                matrice[35]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[28]=="O":
                matrice[28]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[21]=="O":
                matrice[21]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[14]=="O":
                matrice[14]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[7]=="O":
                matrice[7]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[0]=="O":
                matrice[0]= ROUGE+'O'+NORMAL
                tourfinis=True
                
        if nombre ==2:
            if matrice[36]=="O":
                matrice[36]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[29]=="O":
                matrice[29]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[22]=="O":
                matrice[22]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[15]=="O":
                matrice[15]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[8]=="O":
                matrice[8]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[1]=="O":
                matrice[1]= ROUGE+'O'+NORMAL
                tourfinis=True
                
        if nombre==3:
            if matrice[37]=="O":
                matrice[37]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[30]=="O":
                matrice[30]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[23]=="O":
                matrice[23]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[16]=="O":
                matrice[16]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[9]=="O":
                matrice[9]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[2]=="O":
                matrice[2]= ROUGE+'O'+NORMAL
                tourfinis=True
                
        if nombre==4:
            if matrice[38]=="O":
                matrice[38]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[31]=="O":
                matrice[31]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[24]=="O":
                matrice[24]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[17]=="O":
                matrice[17]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[10]=="O":
                matrice[10]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[3]=="O":
                matrice[3]= ROUGE+'O'+NORMAL
                tourfinis=True
                

        if nombre==5:
            if matrice[39]=="O":
                matrice[39]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[32]=="O":
                matrice[32]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[25]=="O":
                matrice[25]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[18]=="O":
                matrice[18]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[11]=="O":
                matrice[11]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[4]=="O":
                matrice[4]= ROUGE+'O'+NORMAL
                tourfinis=True
                
        if nombre==6:
            if matrice[40]=="O":
                matrice[40]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[33]=="O":
                matrice[33]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[26]=="O":
                matrice[26]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[19]=="O":
                matrice[19]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[12]=="O":
                matrice[12]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[5]=="O":
                matrice[5]= ROUGE+'O'+NORMAL
                tourfinis=True
                
        if nombre==7:
            if matrice[41]=="O":
                matrice[41]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[34]=="O":
                matrice[34]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[27]=="O":
                matrice[27]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[20]=="O":
                matrice[20]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[13]=="O":
                matrice[13]= ROUGE+'O'+NORMAL
                tourfinis=True
            elif matrice[6]=="O":
                matrice[6]= ROUGE+'O'+NORMAL
                tourfinis=True
    #Deuxième participant
    else:
        if nombre==1:
            if matrice[35]=="O":
                matrice[35]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[28]=="O":
                matrice[28]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[21]=="O":
                matrice[21]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[14]=="O":
                matrice[14]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[7]=="O":
                matrice[7]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[0]=="O":
                matrice[0]= BLEU+'O'+NORMAL
                tourfinis=True
                
        if nombre ==2:
                
            if matrice[36]=="O":
                print("oui")
                matrice[36]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[29]=="O":
                matrice[29]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[22]=="O":
                matrice[22]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[15]=="O":
                matrice[15]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[8]=="O":
                matrice[8]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[1]=="O":
                matrice[1]= BLEU+'O'+NORMAL
                tourfinis=True
        
        if nombre==3:
            if matrice[37]=="O":
                matrice[37]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[30]=="O":
                matrice[30]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[23]=="O":
                matrice[23]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[16]=="O":
                matrice[16]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[9]=="O":
                matrice[9]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[2]=="O":
                matrice[2]= BLEU+'O'+NORMAL
                tourfinis=True
        
        if nombre==4:
            if matrice[38]=="O":
                matrice[38]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[31]=="O":
                matrice[31]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[24]=="O":
                matrice[24]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[17]=="O":
                matrice[17]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[10]=="O":
                matrice[10]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[3]=="O":
                matrice[3]= BLEU+'O'+NORMAL
                tourfinis=True
            
        if nombre==5:
            if matrice[39]=="O":
                matrice[39]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[32]=="O":
                matrice[32]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[25]=="O":
                matrice[25]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[18]=="O":
                matrice[18]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[11]=="O":
                matrice[11]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[4]=="O":
                matrice[4]= BLEU+'O'+NORMAL
                tourfinis=True
        
        if nombre==6:
            if matrice[40]=="O":
                matrice[40]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[33]=="O":
                matrice[33]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[26]=="O":
                matrice[26]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[19]=="O":
                matrice[19]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[12]=="O":
                matrice[12]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[5]=="O":
                matrice[5]= BLEU+'O'+NORMAL
                tourfinis=True
        if nombre==7:
            if matrice[41]=="O":
                matrice[41]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[34]=="O":
                matrice[34]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[27]=="O":
                matrice[27]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[20]=="O":
                matrice[20]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[13]=="O":
                matrice[13]= BLEU+'O'+NORMAL
                tourfinis=True
            elif matrice[6]=="O":
                matrice[6]= BLEU+'O'+NORMAL
                tourfinis=True
    return tourfinis
    
def OCOPuissance4():
    #
    #Procédure permettant à un ordinateur de jouer contre un autre ordinateur au jeu du puissance 4
    #Entrée: /
    #Sortie:/
    #
    
    #Initialisation
    coup : int
    nombre : int
    gagner : bool
    tour : bool
    ok:bool
    tourfinis:bool
    ROUGE='\033[91m'
    BLEU='\033[94m'
    NORMAL='\033[0m'
    matrice : list[str]
    matrice = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
    coup=0
    gagner=False
    premier_a_joue:int
    premier_a_joue = random.randint(1,2)
    difficulte:int
    difficulte2:int
    difficulte=0
    difficulte2=0
    #Choix de la difficulté du premier ordinateur
    print("Veuillez choisir la difficulté de l'ordinateur 1")
    while difficulte!='1' and difficulte!='2' and difficulte!='3':
        menuaDifficulté()
        difficulte=input("Choisir la difficulté de l'ordinateur 1 ? ")
    #Choix de la difficulté du deuxième ordinateur
    print("Veuillez choisir la difficulté de l'ordinateur 2")
    while difficulte2!='1' and difficulte2!='2' and difficulte2!='3':
        menuaDifficulté()
        difficulte2=input("Choisir la difficulté de l'ordinateur 2 ? ")

    #Affiche le joueur qui commence la partie
    if premier_a_joue==1:
        print("C'est l'ordianteur 1 qui commence")
        tour=True    
    else :
        print("C'est l'ordinateur 2 qui commence")
        tour=False
    
    #Début de la partie 
    while coup < 42 and not gagner:
        coup = coup + 1 
        if tour==True:
            #Tour de l'ordinateur 1
            affichepuissance(matrice)
            tourfinis=False
            while not tourfinis:
                if difficulte=='1':
                    aleatoire=2
                elif difficulte=='2':
                    aleatoire=random.randint(1,2)
                else:
                    aleatoire=1
                
                if aleatoire==1:
                    pos=joueparfaitpuissance4(matrice)
                    if pos==-1:
                        nombre=random.randint(1,7)
                    else:
                        nombre=pos
                else:
                    nombre=random.randint(1,7)
                tourfinis=ecritpuissance(matrice,tourfinis,nombre,tour)
            tour=False
            gagner=verifpuissance(matrice, gagner)
            
        else:
            #Tour de l'ordinateur 2
            affichepuissance(matrice)
            tourfinis=False
            while not tourfinis:
                if difficulte2=='1':
                    aleatoire=2
                elif difficulte2=='2':
                    aleatoire=random.randint(1,2)
                else:
                    aleatoire=1
                
                if aleatoire==1:
                    pos=joueparfaitpuissance4(matrice)
                    if pos==-1:
                        nombre=random.randint(1,7)
                    else:
                        nombre=pos
                else:
                    nombre=random.randint(1,7)
                tourfinis=ecritpuissance(matrice,tourfinis,nombre,tour)
            tour=True
            gagner=verifpuissance(matrice, gagner) 
        
        if coup==42:
            affichepuissance(matrice)
            print("La partie est finie, c'est une égalité")
    
    if tour==False:
        print("L'ordinateur 1 remporte la partie ")
        
    else:
        print("L'ordinateur 2 remporte la partie ")

   

def JcJPuissance4(tabJoueur:list[Joueur],nJoueur:int,J1:str):
    #
    #Procédure permettant à deux joueurs de jouer au jeu du puissance 4
    #Entrée: tabJoueur, nJoueur, J1
    #Sortie: AjoutscorePuissance4
    #
    
    #Initialisation
    J2:str
    premier_a_joue : int
    demande_commence : str
    verif_demande : bool
    coup : int
    nombre : int
    gagner : bool
    tour : bool
    ok:bool
    tourfinis:bool
    t0:float
    tf:float
    chiffrescore:int
    ROUGE='\033[91m'
    BLEU='\033[94m'
    NORMAL='\033[0m'
    temppartie:int
    JoueurValide:bool
    matrice : list[str]
    matrice = ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
    JoueurValide=False
    chiffrescore=300

    print ("Bienvenue dans le mode Joueur contre Joueur ",J1)
    #Saisie du deuxième joueur
    print ("Veuillez saisir le nom du deuxième Joueur")
    while JoueurValide !=True:
        J2=input()
        JoueurValide=verifJoueur(J2,tabJoueur,nJoueur)
    #Demande qu'elle joueur va commencer
    verif_demande = False
    while not verif_demande:
        demande_commence = str(input("Voulez-vous que le choix du joueur (qui commence/qui choisie le nombre) soit aléatoire (oui ou non)? "))
        if demande_commence=='oui':
            premier_a_joue = random.randint(1,2)
            verif_demande = True
        elif demande_commence=='non':
            premier_a_joue=int(input("Lequelle des deux joueurs veut commencé (1 pour joueur 1 et 2 pour joueur 2)? "))
            verif_demande = True
        else:
            print("La valeur choisi n'est pas un choix possible")
        
    #Affiche le joueur qui commence 
    if premier_a_joue==1:
        print("C'est",J1 ,"qui commence")
        tour=True    
    else :
        print("C'est",J2, "qui commence")
        tour=False
    
    #Début de la partie
    coup = 0
    gagner = False
    t0=time.time()
    while coup < 42 and not gagner:
        coup = coup + 1 
        if tour==True:
            #Partie du permier joueur
            tourfinis=False
            while not tourfinis:
                affichepuissance(matrice)
                ok=False
                #Choix + vérification da la case
                while not ok: 
                    print (J1,"choisissez une colonne  entre 1 et 7: ")
                    nombre = int(input())
                    while nombre<0 or nombre>7:
                        print("Erreur dans la saisie")
                        print (J1,"choisissez une colonne  entre 1 et 7: ")
                        nombre = int(input())
                    ok=True 
                #Place le choix de la case                      
                tourfinis=ecritpuissance(matrice,tourfinis,nombre,tour)
                if tourfinis==False:     
                    print ("Vous ne pouvez pas mettre de jeton dans cette colonne , elle est complète ")
            tour=False
            #Vérifie si le joueur a gagné
            gagner=verifpuissance(matrice, gagner)
            
        else:
            #Partie du deuxième joueur
            affichepuissance(matrice)
            tourfinis=False
            while not tourfinis:
                ok=False
                #Choix + vérification de la case
                while not ok:
                    print (J2,"choisissez une colonne  entre 1 et 7: ")
                    nombre = int(input())
                    while nombre<0 or nombre>7:
                        print("Erreur dans la saisie")
                        print (J2,"choisissez une colonne  entre 1 et 7: ")
                        nombre = int(input())
                    ok=True
                #Place le choix dans la case
                tourfinis=ecritpuissance(matrice,tourfinis,nombre,tour)
                if tourfinis==False:     
                    print ("Vous ne pouvez pas mettre de jeton dans cette colonne , elle est complète ")
            tour=True
            #Vérifie si le joueur a gagné
            gagner=verifpuissance(matrice, gagner)
        
        #Fin de partie, c'est une égalité
        if coup==42:
            affichepuissance(matrice)
            print("La partie est finie, c'est une égalité")
    tf=time.time()
    temppartie=int(tf)-int(t0)
    #Qui a gagné + ajout du score
    if tour==False:
        print(J1, "remporte la partie en" ,temppartie,"secondes")
        AjoutscorePuissance4(tabJoueur,nJoueur,J1,temppartie,chiffrescore)
        
    else:
        print(J2, "remporte la partie en" ,temppartie,"secondes")
        AjoutscorePuissance4(tabJoueur,nJoueur,J2,temppartie,chiffrescore)

if __name__=='__main__':

    choix:int
    tabJoueur:list[Joueur]
    J1:str
    nJoueur:int
    pos:int
    reponse:str
    JoueurValide:bool
    JoueurValide=False
    nJoueur=0
    choix=0
    tabJoueur=[]
    

    lectureJoueur(tabJoueur,nJoueur)
    nJoueur=len(tabJoueur)
    print("Bonjour veuillez saisir le nom du Joueur 1")
    while JoueurValide !=True:
        J1=input()
        JoueurValide=verifJoueur(J1,tabJoueur,nJoueur)

    while choix !='6':
        nJoueur=len(tabJoueur)
        menu()
        print("Veuillez saisir votre choix")
        choix=input()
        if choix =='1':
            menuDevinette(tabJoueur,nJoueur,J1)
        if choix =='2':
            menuAllumettes(tabJoueur,nJoueur,J1)
        if choix =='3':
            menuMorpion(tabJoueur,nJoueur,J1)
        if choix == '5':
            Affichage(tabJoueur,nJoueur)
        if choix =='4':
            menupuissance4(tabJoueur,nJoueur,J1)
        if choix =='6':
            print("Au revoir")
            sauvegardescore(tabJoueur,nJoueur)

