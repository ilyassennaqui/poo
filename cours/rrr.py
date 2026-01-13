'''@classmethod
def AjouterChauffeur(cls):
    cin=input("Taper le CIN du chauffeur : ")
    nom=input("Taper le nom du chauffeur : ")
    prenom=input("Taper le prenom du chauffeur : ")
    ch=Chauffeur(cin,nom,prenom)
    cls.Lchauffeurs.append(ch)
    print("Chauffeur ajoute avec succes")
@classmethod
def AjouterBus(cls):
    immatriculation=input("Taper l'immatriculation du bus : ")
    marque=input("Taper la marque du bus : ")
    typ=input("Taper le type du bus : ")
    b=Bus(immatriculation,marque,typ)
    cls.Lbus.append(b)
    print("Bus ajoute avec succes")'''