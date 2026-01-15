import math
from abc import ABC,abstractmethod
class Forme(ABC):
    def __init__(self,nom):
        self._nom=nom
    @property
    def Nom(self):
        return self._nom
    @Nom.setter
    def Nom(self,new):
        self._nom=new

    #methodde abstraite pour le perimetre 
    @abstractmethod
    def CalculerPerimetre(self):
        pass
    @abstractmethod
    def CalculerSurface(self):
        pass
    def __str__(self):
        return f"{self._nom}"

class Rectangle(Forme):
    def __init__(self, nom,long,larg):
        super().__init__(nom)
        self.long=long
        self.larg=larg
    def __str__(self):
        a=super().__str__()
        a+=f"\t{self.long}\t {self.larg}"
        return a
    def CalculerPerimetre(self):
        return (self.long+self.larg)*2
    def CalculerSurface(self):
        return self.long*self.larg
    
class Cercle(Forme):
    def __init__(self, nom,r):
        super().__init__(nom)
        self.rayon=r
    def CalculerPerimetre(self):
        return 2*math.pi*self.rayon
    def CalculerSurface(self):
        return math.pi*self.rayon**2
    def __str__(self):
        return super().__str__()+f"\t {self.rayon}"

    
if __name__=="__main__":
    rect=Rectangle("rect1",6,3)
    print(rect)
    print("Le perimitre du rectangle")
    print(rect.CalculerPerimetre())
    print("La surface du rectangle")
    print(rect.CalculerSurface())
