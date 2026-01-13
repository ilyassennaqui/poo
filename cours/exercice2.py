class Person:
    def __init__(self,nom,ville="Casablanca"):
        self.nom=nom
        self.ville=ville
    def afficher(self):
        print(F"Nom:{self.nom}")
        print(F"Ville natale : {self.ville}")
if __name__=="__main__":
    p1=Person("Ayoub")
    p1.afficher()
    p2=Person("Aicha","Rabat")  
    p2.afficher()