from os import defpath
from pyad import *

# Connexion au serveur Active Directory avec un utilisateur admin du domaine
pyad.set_defaults(ladp_server="WINDOWS-AD.akb.lab",username="administrateur",password="WindowsServer2016$")

#########################################################################
# Suppression de tous les  membres d'un groupe
#########################################################################

def supprimer_all_membres():
    # nom du groupe dont tous les membres seront supprimés
    nom_groupe="test_group_python1"

    # suppression de tous les membres du groupe
    group=pyad.adgroup.ADGroup.from_cn(nom_groupe)

    # affichage de message suite à la suppression de tous les membres
    print()
    print("Le groupe " + nom_groupe + " ne contient plus de membres")
    print()   
            
    group.remove_all_members()
                
        