from pyad import *
import csv


##########################################################################
# Suppression de plusieurs PC via un fichier CSV
#########################################################################



def supprimer_ordinateurs():

    # Déclaration du fichier csv contenant la liste des PC
    with open("base_utilisateurs.csv") as fichier_utilisateurs:
    
    # Lecture du fichier csv: les données sont délimitées par ","
        liste_utilisateurs=csv.reader(fichier_utilisateurs,delimiter=",")
                    
        print()
        print("Liste des PC supprimés")
        print() 
    # Utilisation d'une boucle pour traiter toutes les lignes du fichier
        i=0
        for utilistateur in liste_utilisateurs:
           
            if(i>0):
                
                nom_pc=utilistateur[7]
            
                print(nom_pc)
            
                #ajouter_pc=pyad.aduser.ADUser.create(sAMAccountName, pc_ou, upn_suffix=None, enable=True, optional_attributes={"employeeID":employeeID, "givenName":givenName, "sn":sn, "mail":mail, "department":department})               
                ajouter_pc=pyad.adcomputer.ADComputer.from_cn(nom_pc).delete()

            i=i+1
