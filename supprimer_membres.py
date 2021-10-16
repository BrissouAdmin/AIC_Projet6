import csv

from pyad import *

#########################################################################
# Suppression de membres à un groupe
#########################################################################

def supprimer_membres():

    # nom du groupe dans lequel ajouter les membres
    nom_groupe="test_group_python1"

    group=pyad.adgroup.ADGroup.from_cn(nom_groupe)

    # Déclaration du fichier csv contenant la liste des utilisateurs
    with open("base_utilisateurs.csv") as fichier_utilisateurs:
        
        # Lecture du fichier csv: les données sont délimitées par ","
            liste_utilisateurs=csv.reader(fichier_utilisateurs,delimiter=",")
                    
            print()
            print("Liste de membres supprimés ")
            print() 
        # Utilisation d'une boucle pour traiter toutes les lignes du fichier
            i=0
            for utilistateur in liste_utilisateurs:
            
                if(i>0):
                    
                    sAMAccountName=utilistateur[5]
                                        
                    utilisateur=pyad.aduser.ADUser.from_cn(sAMAccountName)
                
                    group.remove_members([utilisateur])
                    
                    print(sAMAccountName)
                i=i+1
