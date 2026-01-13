T=[]
class Voiture:
    # Attributs
    nom=""
    matricule=""
    pays="Allmend"
    # Méthodes
    def afficher(self):
        print(f"le nom est {vtr1.nom}")
        print(f"le matricule est {vtr1.matricule}")
        print(f"le pays de fabrication est {Voiture.pays}")
#premiere voiture
vtr1=Voiture()
vtr1.nom="BMW"
vtr1.matricule="A13288"
vtr1.afficher()
#deuxieme voiture
vtr2=Voiture()
vtr2.nom="audi"
vtr2.matricule="B214125"
vtr2.afficher()
#ajouter les voitures dans la liste T
T.append(vtr1)
T.append(vtr2)
#afficher les voitures de la liste T
for vtr in T:
    print("---------------")
    print(f"le nom est {vtr.nom}")
    print(f"le matricule est {vtr.matricule}")
    print(f"le pays de fabrication est {vtr.pays}")
    



