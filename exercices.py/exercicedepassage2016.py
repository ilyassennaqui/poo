import re
class Salarié:
    def __init__(self,id,nom,prenom,adresse,genre,age,service,departement,ville):
        self.id=id
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.genre=genre
        self.age=age
        self.service=service
        self.departement=departement
        self.ville=ville
    
    def __str__(self):
        return f"{self.id}\t {self.nom}\t{self.prenom}\t{self.adresse}\t{self.genre}\t{self.age}\t{self.service}\t{self.departement}\t{self.ville}"

class Depense:
    def __init__(self, num, lib, lieu, comment, mt):
        self.num=num
        self.libelle=lib
        self.lieu=lieu
        self.commentaire=comment
        self.montant=mt
    def CalculerCharge(self,taux):
        return self.montant * taux
    def __str__(self):
        return f"Numero: {self.num}\nLibelle: {self.libelle}\nLieu: {self.lieu}\nCommentaire: {self.commentaire}\nMontant: {self.montant}"
    
class ChargeDeplacementVoiture(Depense):
    def __init__(self, num, lib, lieu, comment, mt, salarie, marque, ndch, ndpl, tdc, km):
        super().__init__(num, lib, lieu, comment, mt)
        self.salarie=salarie
        self.marque=marque
        motif=r"^/d{6,14}$"
        ver=re.search(motif,ndch)
        if ver:
          self.nbchevaux=ndch
        else:
            raise cheveauexception()
        self.nbplaque=ndpl
        self.typecarburant=tdc
        self.kilometrage=km
    def CalculerCharge(self, taux):
        return super().CalculerCharge(taux)+self.kilometrage*11
    def __str__(self):
        return f"{self.salarie}\t{self.marque}\t{self.nbchevaux}\t{self.nbplaque}\t{self.typecarburant}\t{self.kilometrage}"
class cheveauexception(Exception):
    def __init__(self):
        super().__init__("le nombre doit être compris entre 6 et 14")
class ListeChargeDeplacement:
    def __init__(self):
        self.LCD=[]
    def ajouter(self, Depense):
        if Depense not in self.LCD:
            self.LCD.append(Depense)
            print("Depense ajouter avec succes")
        else:
            print("Depense existante")
    def afficher(self):
        for m in self.LCD:
            print(m)
    def supprimer(self, Depense):
        if Depense in self.LCD:
            self.LCD.remove(Depense)
            print("Depense supprimer avec succes")
        else:
            print("Depense introuvable")
    def rechercher(self):
        for s in self.LCD:
            if s.montant>1000:
                print(s)

if __name__=="__main__":
    while True:  
        print("**************Menu General***********")
        print("1----------Ajouter une depense-------")
        print("2----------Afficher les depenses-----")
        print("3----------Supprimer une depense-----")
        print("4----------Rechercher une depense----")
        print("5----------------Quitter-------------")
        rep=int(input("tapez votre choix: "))
        if rep==1:
            try:
                # Création du salarié
                sal = Salarié(
                    id=input("ID salarié : "),
                    nom=input("Nom : "),
                    prenom=input("Prénom : "),
                    adresse=input("Adresse : "),
                    genre=input("Genre : "),
                    age=int(input("Age : ")),
                    service=input("Service : "),
                    departement=input("Département : "),
                    ville=input("Ville : ")
                )

                # Création de la dépense
                dep = ChargeDeplacementVoiture(
                    num=input("Numéro dépense : "),
                    lib=input("Libellé : "),
                    lieu=input("Lieu : "),
                    comment=input("Commentaire : "),
                    mt=float(input("Montant : ")),
                    salarie=sal,
                    marque=input("Marque voiture : "),
                    ndch=input("Nombre de chevaux : "),
                    ndpl=input("Numéro de plaque : "),
                    tdc=input("Type carburant : "),
                    km=float(input("Kilométrage : "))
                )

                ListeChargeDeplacement.LCD.ajouter(dep)

            except cheveauexception as e:
                print("Erreur :", e)

            except ValueError:
                print("Erreur de saisie ❌")
    
        elif rep == 2:
            ListeChargeDeplacement.LCD.afficher()

        elif rep == 3:
            num = input("Donner le numéro de la dépense à supprimer : ")
            for d in ListeChargeDeplacement.LCD:
                if d.num == num:
                    ListeChargeDeplacement.supprimer(d)
                    break
            else:
                print("Dépense non trouvée")

        elif rep == 4:
            ListeChargeDeplacement.LCD.rechercher()

        elif rep == 5:
            print("Au revoir 👋")
            break

        else:
            print("Choix invalide ❌")