class salarie:
    def __init__(self,id,nom,prenom,adresse,genre,service,departement,ville):
        self.id=id
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.genre=genre
        self.service=service
        self.departement=departement
        self.ville=ville
    def __str__(self):
        return f"Salarie {self.id}: {self.nom} {self.prenom}, Adresse: {self.adresse}, Genre: {self.genre}, Service: {self.service}, Departement: {self.departement}, Ville: {self.ville}"
class depense:
    def __init__(self,n,l,lieu,cmt,montant):
        self.nom=n
        self.libelle=l
        self.lieu=lieu
        self.commentaire=cmt
        self.montant=montant
    def calculercharge(self,taux):
        return self.montant * taux / 100
    def __str__(self):
        return f"Depense {self.nom}: {self.libelle}, Lieu: {self.lieu}, Commentaire: {self.commentaire}, Montant: {self.montant}"
class cheveauException(Exception):
    pass
class chargeDeplacement(depense):
    def __init__(self,n,l,lieu,cmt,montant,salarie,marque,nb_chevaux,plaque,carburant,km):
        super().__init__(n,l,lieu,cmt,montant)
        self.salarie=salarie
        self.marque=marque
        if nb_chevaux<6 or nb_chevaux>14:
            raise cheveauException("le nombre de chevaux doit etre 6 et 14")
        self.nb_chevaux=nb_chevaux
        self.plaque=plaque
        self.carburant=carburant
        self.km=km
    def calculercharge(self):
        return self.km*11
    def __str__(self):
        return f"{super().__str__()} Voiture: {self.marque}, Nb Chevaux: {self.nb_chevaux}, Plaque: {self.plaque}, Carburant: {self.carburant}, Km: {self.km}"
class ListeCharges:
    def __init__(self):
        self.lcharges=[]

    def ajoutercharge(self,depense):
        rep=input("voulez vous ajouter la depense? (O/N): ")
        if rep.upper() == "O":
            self.lcharges.append(depense)
            print("depense ajoutee avec succes")
    def afficher(self):
        if not self.lcharges:
            print("la liste des charges est vide")
        for c in self.lcharges:
            print(c)
    def supprimer(self,depense):
        if depense in self.lcharges:
            self.lcharges.remove(depense)
            print("depense supprimee avec succes")
        else:
            print("la depense n'existe pas dans la liste")
    def rechercher(self):
        n=input("taper le nom de la depense a rechercher: ")
        for c in self.lcharges:
            if c.montant>1000:
                print(c)
                n=True
        if not n:
            print("aucune depense trouvee avec montant superieur a 1000")
def main():
    try:
        s1=salarie(1,"bennani","samir","123 Main St","M","IT","Development","Rabat")
        d1=depense(101,"missin rabt","rabat","train",1500)
        d2=depense(102,"mission casablanca","casablanca","voiture",800)
        v1=chargeDeplacement(103,"mission marrakech","marrakech","voiture",2000,s1,"toyota",10,"123-AB-45","essence",300)
        liste=ListeCharges()
        liste.ajoutercharge(d1)
        liste.ajoutercharge(d2)
        liste.ajoutercharge(v1)

        while True:
            print("*****Menu*****")
            print("1. Afficher toutes les depenses")
            print("2. Supprimer une depense")
            print("3. Rechercher des depenses")
            print("4. Quitter")
            choix=input("choisir une option: ")
            if choix=="1":
                liste.afficher()
            elif choix=="2":
                nom=input("taper le nom de la depense a supprimer: ")
                for c in liste.lcharges:
                    if c.nom==nom:
                        liste.supprimer(c)
                        break
                else:
                    print("depense non trouvee")
            elif choix=="3":
                liste.rechercher()
            elif choix=="4":
                print("fin du programme")
                break
            else:
                print("option invalide, ressayer")
    except cheveauException as e:
        print(f"Erreur: {e}")
if __name__=="__main__":
    main()