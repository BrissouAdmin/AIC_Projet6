import wmi

def configurer_reseau():
    # Connexion sur une machine locale
    c = wmi.WMI()

    # Connexion sur une machine distante
    #c = wmi.WMI("WINDOWS-AD.akb.lab", user=r"python.demo", password="Azerty2016$")

    # obtention des configurations des adaptateurs réseau
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # premier adaptateur réseau
    nic = nic_configs[0]

    # Adresse IP, Masque de sous-réseau et Passerelle devraient être des objets Unicode (u avant les adresses)
    ip = u'192.168.0.11'
    subnetmask = u'255.255.255.0'
    gateway = u'192.168.0.1'

    #print(nic)

    # Configuration de l'adresse IP , le masque de sous-réseau et la passerelle
    # Les méthodes EnableStatic() et SetGateways() demandent une "liste" de valeurs
    nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])

    print()
    print("La carte réseau a été reconfigurée avec les données suivantes")
    print("Ip: " + ip + " /Masque de sous-réseau: " + subnetmask + " /Passerelle: " + gateway)
    print()
