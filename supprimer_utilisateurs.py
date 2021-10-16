from pyad import *
import csv

##########################################################################
# Supression de plusieurs Utilisateurs via un fichier CSV
#########################################################################

def supprimer_utilisateurs():

# Déclaration du fichier csv contenant la liste des utilisateurs à suprimer
    with open("base_utilisateurs.csv") as fichier_utilisateurs:
    
        # Lecture du fichier csv: les données sont délimitées par ","
        liste_utilisateurs=csv.reader(fichier_utilisateurs,delimiter=",")

        print()
        print("Liste des utilisateurs supprimés")
        print()

        # Utilisation d'une boucle pour traiter toutes les lignes du fichier
        i=0
        for utilistateur in liste_utilisateurs:
                
            if(i>0):
                sAMAccountName=utilistateur[5]
                pyad.aduser.ADUser.from_cn(sAMAccountName).delete()
                                 
                print("ID-utilisateur supprimé est" + utilistateur[0])             
            i=i+1