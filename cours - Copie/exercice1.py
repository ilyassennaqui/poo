import math
class Cercle:
    def __init__(self,ra,x,y):
        self.rayon=ra
        self.absci=x
        self.ordon=y
    def surface(self):
        return math.pi*self.rayon**2
    def perimetre(self):
        return self.rayon*2*math.pi
    def afficher(self):
        print(f"la cercle de rayon : {self.rayon} , la position de son centre est O({self.absci},{self.ordon})")
        print(F"Sa surface : {self.surface():.2f}")
        print(F"Son perimetre : {self.perimetre():.2f}")
r=float(input("taper le rayon du cercle : "))
xe=float(input("taper l'abscisse du centre : "))
ye=float(input("taper l'ordonnee du centre : "))
cer1=Cercle(r,xe,ye)
cer1.afficher()