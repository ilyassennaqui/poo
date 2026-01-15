from abc import ABC , abstractmethod
class ObjetPostal(ABC):
    def __init__(self,n,adr,cdpos,ville,exp):
        self.nom=n
        self.adresse=adr
        self.postal=cdpos
        self.ville=ville
        self.expedite=exp

    @abstractmethod
    def Prix(self):
        pass
class Lettre(ObjetPostal):
    def __init__(self, n, adr, cdpos, ville, exp,expurge):
        super().__init__(n, adr, cdpos, ville, exp)
        self.expurge=expurge

    def Prix(self):
        if self.expedite:
            return f"le prix est 2.03 Euros"
        elif self.expurge:
            return f"Le prix est 2.63 Euros"
        return f"Le prix est 0.53 Euros "
    
class Colis(ObjetPostal):
    def __init__(self, n, adr, cdpos, ville, exp,poids):
        super().__init__(n, adr, cdpos, ville, exp)
        self.poids=poids

    def Prix(self):
        unite=self.poids/100
        if self.expedite:
            return f"{(0.8 * unite )+3} Euros "
        return f"{0.8 * unite} Euros "
    
if __name__=="__main__":
    print("---------Menu--------")
    print("---------")
    

    