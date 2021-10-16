



from pyad import *
import csv



##########################################################################
# Création de plusieurs Ordinateurs via un fichier CSV
#########################################################################

def ajouter_ordinateurs():

        # Déclaration de l'OU dans laquelle on veut travailler
    pc_ou=pyad.adcontainer.ADContainer.from_dn("OU=Ordinateurs,OU=Logistique,OU=Employés,DC=akb,DC=lab") 

        # Déclaration du fichier csv contenant la liste des PC
    with open("base_utilisateurs.csv") as fichier_utilisateurs:
        
        # Lecture du fichier csv: les données sont délimitées par ","
            liste_utilisateurs=csv.reader(fichier_utilisateurs,delimiter=",")
                        
            print()
            print("Liste des PC ajoutés")
            print() 
        # Utilisation d'une boucle pour traiter toutes les lignes du fichier
            i=0
            for utilistateur in liste_utilisateurs:
            
                if(i>0):
                    
                    nom_pc=utilistateur[7]
                
                    print(nom_pc)
                
                    #ajouter_pc=pyad.aduser.ADUser.create(sAMAccountName, pc_ou, upn_suffix=None, enable=True, optional_attributes={"employeeID":employeeID, "givenName":givenName, "sn":sn, "mail":mail, "department":department})               
                    ajouter_pc=pyad.adcomputer.ADComputer.create(nom_pc, pc_ou, enable=True, optional_attributes={"Description":"PC ajouté via script Python"})

                i=i+1
