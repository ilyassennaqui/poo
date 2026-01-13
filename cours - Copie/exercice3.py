class Client:
    def __init__(self,n,p,v):
        self.__nom=n
        self.__prenom=p
        self.__ville=v
    @property
    def nom(self):
        return self.nom
    @nom.setter
    def  nom(self,new):
        self.nom=new

    @property
    def prenom(self):
        return self.prenom
    @prenom.setter
    def  nom(self,new):
        self.prenom=new

    @property
    def ville(self):
        return self.ville
    @ville.setter
    def  nom(self,new):
        self.ville=new
class Compte:
    def __init__(self,number,name,solde):
        self.__numero=number
        self.__name=name
        self.__solde=solde
    #GETTERS FOR NUMBER
    def getNumber(self):
        return self.__numero
    #SETTERS FOR NUMBER
    def SetNumber(self,new):
        self.__numero=new
    #GETTERS FOR NAME
    def getName(self):
        return self.__name
    #SETTERS FOR NAME
    def SetName(self,new):
        self.__name=new
    #GETTERS FOR SOLDE
    def getSolde(self):
        return self.__solde
    #SETTERS FOR SOLDE
    def SetSolde(self,new):
        self.__solde=new
    #METHODE POUR DEPOSER D'ARGENT
    def Deposer(self,m):
        self.__solde+=m
    #METHODE POUR RETIRER D'ARGENT
    def Retirer(self,m):
        if m>self.__solde:
            print("Operation impossible")
        else:
            self.__solde-=m
    def __str__(self):
       return f"{self.__numero} \t {self.__name} \t {self.__solde}"

cmpte=Compte(1000,"ilyass",12000)
print(cmpte)
print("depot de 5000")
cmpte.Deposer(5000)
print(cmpte)
print("Retrait de 10000")
cmpte.Retirer(10000)
print(cmpte)