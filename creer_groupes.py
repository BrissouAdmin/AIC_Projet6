
from pyad import *

#########################################################################
# Création de groupes
#########################################################################

def creer_groupes():
    # nom du groupe à créer
    nom_groupe="test_group_python1"
    # l'OU du groupe à créer
    group_ou=pyad.adcontainer.ADContainer.from_dn("OU=Logistique,OU=Employés,DC=akb,DC=lab")
    # création du group
    creer_group=pyad.adgroup.ADGroup.create(nom_groupe, group_ou, security_enabled=True, scope='GLOBAL', optional_attributes={"description":"Créé via script Python"})

    print("Le groupe créé est: " + nom_groupe)