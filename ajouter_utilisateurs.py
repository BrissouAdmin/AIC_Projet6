from pyad import *
import csv

##########################################################################
# Création de plusieurs Utilisateurs via un fichier CSV
#########################################################################

def ajouter_utilisateurs():

    # Déclaration de l'OU dans laquelle on veut travailler
    ou=pyad.adcontainer.ADContainer.from_dn("OU=Logistique,OU=Employés,DC=akb,DC=lab") 

    # Déclaration du fichier csv contenant la liste des utilisateurs
    with open("base_utilisateurs.csv") as fichier_utilisateurs:
    
    # Lecture du fichier csv: les données sont délimitées par ","
        liste_utilisateurs=csv.reader(fichier_utilisateurs,delimiter=",")
    
        MDP_utilisateur="Logistique2021$"
        
        print()
        print("Liste des utilisateurs ajoutés")
        print() 
    # Utilisation d'une boucle pour traiter toutes les lignes du fichier
        i=0
        for utilistateur in liste_utilisateurs:
           
            if(i>0):
                employeeID=utilistateur[0]
                givenName=utilistateur[1]
                sn=utilistateur[2]
                department=utilistateur[3]
                mail=utilistateur[4]
                sAMAccountName=utilistateur[5]
            
                print(sAMAccountName)
            
                creer_utilisateur=pyad.aduser.ADUser.create(sAMAccountName, ou, password=MDP_utilisateur, upn_suffix=None, enable=True, optional_attributes={"employeeID":employeeID, "givenName":givenName, "sn":sn, "mail":mail, "department":department})               
            i=i+1
