import wmi

def renommer_pc():
        # Connexion sur une machine locale
        c = wmi.WMI()

        # Connexion sur une machine distante
        #c = wmi.WMI("WINDOWS-AD.akb.lab", user=r"python.demo", password="Azerty2016$")

        # Nouveau nom de la machine
        nouveau_nom_pc="WINDOWS-AD"

        for system in c.Win32_ComputerSystem():
                system.Rename(nouveau_nom_pc)
        print()
        print("La machine a été renommée en " + nouveau_nom_pc)        
        print()