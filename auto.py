from renommer_pc import *
from configurer_reseau import *
from ajouter_utilisateurs import *
from supprimer_utilisateurs import *
from creer_groupes import *
from ajouter_membres import *
from supprimer_membres import *
from supprimer_membres import *
from supprimer_membres import *
from supprimer_all_membres import *
from supprimer_groupes import *
from ajouter_ordinateurs import *
from supprimer_ordinateurs import *

from pyad import *

import csv

############################################################################
# Connexion au serveur Active Directory avec un utilisateur admin du domaine
############################################################################
pyad.set_defaults(ladp_server="WINDOWS-AD.akb.lab",username="python.demo",password="Azerty2016$")



#########################################################################
# Menu pour le choix des tâches
#########################################################################

def menu():
    
    print()
    print("=============== CONFIGURATION DU SERVEUR ==================")
    print("[1] Renommage de la machine")
    print("[2] Configuration du réseau")
    print()
    print("=============== GESTION DES UTILISATEURS ==================")
    print("[3] Ajout d'utilisateurs à partir d'un fichier csv")
    print("[4] Supression d'utilisateurs à partir d'un fichier csv")
    print()
    print("================== GESTION DES GROUPES =====================")
    print("[5] Création de groupes")
    print("[6] Ajout de membres à un groupe")
    print("[7] Suppression de membres d'un groupe via fichier csv")
    print("[8] Suppression de tous les membres d'un groupe")
    print("[9] Supression de groupes")
    print()
    print("================== GESTION DES ORDINATEURS =================")
    print("[10] Ajout d'ordinanteurs via fichier csv")
    print("[11] Supression d'ordinanteurs via fichier csv")
    print()
    print("================== VERS LA SORTIE =================")
    print("[99] Sortie du Script")


menu()
choix = int(input("Entrer votre choix: "))

while choix != 0:
    if choix == 1:
        renommer_pc()  
    elif choix == 2:
        configurer_reseau()
    elif choix == 3:
        print("Vous avez choisi la création d'utilisateurs ........")
        ajouter_utilisateurs()
    elif choix == 4:
        print("Vous avez choisi la suppression d'utilisateurs ........")
        supprimer_utilisateurs()
    elif choix == 5:
        print("Vous avez choisi la création de groupes ........")
        creer_groupes()
    elif choix == 6:
        print("Vous avez choisi Ajout de membres à un groupe........")
        ajouter_membres()  
    elif choix == 7:
        print("Vous avez choisi la Suppression de membres d'un groupe via fichier csv ........")
        supprimer_membres()
    elif choix == 8:
        print("Vous avez choisi la Suppression de tous les membres d'un groupe ........")
        supprimer_all_membres()
    elif choix == 9:
        print("Vous avez choisi la Suppression de groupes ........")
        supprimer_groupes()
    elif choix == 10:
        print("Vous avez choisi Ajout d'ordinanteurs via fichier csv ........")
        ajouter_ordinateurs()
    elif choix == 11:
        print("Vous avez choisi la Suppression d'ordinanteurs via fichier csv ........")
        supprimer_ordinateurs()
    
    elif choix == 99:
        quit()

    else:
        print("Choix invalide")
    
    print()
    menu()
    choix = int(input("Entrer votre choix "))

print("Merci d'avoir utilisé le programme. Bye. ")


