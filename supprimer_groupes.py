from pyad import *


# Connexion au serveur Active Directory avec un utilisateur admin du domaine
pyad.set_defaults(ladp_server="WINDOWS-AD.akb.lab",username="administrateur",password="WindowsServer2016$")

#########################################################################
# Suppression de groupes
#########################################################################

def supprimer_groupes():
    # nom du groupe à supprimer
    nom_groupe="test_group_python1"

    group=pyad.adgroup.ADGroup.from_cn(nom_groupe).delete()

    print("Le groupe supprimé est " + nom_groupe)

