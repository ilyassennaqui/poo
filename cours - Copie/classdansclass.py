class Client:
    def __init__(self,n,p,v):
        self.__nom=n
        self.__prenom=p
        self.__ville=v
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def  nom(self,n):
        self.__nom=n

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def  prenom(self,p):
        self.__prenom=p

    @property
    def ville(self):
        return self.__ville
    @ville.setter
    def  ville(self,new):
        self.__ville=new
class Compte:
    def __init__(self,number,c,solde):
        self.__numero=number
        self.__Client=c
        self.__solde=solde
    #GETTERS FOR NUMBER
    def getNumber(self):
        return self.__numero
    #SETTERS FOR NUMBER
    def SetNumber(self,new):
        self.__numero=new
     #GETTERS FOR Client
    def getClient(self):
        return self.__Client
    #SETTERS FOR Client
    def SetClient(self,new):
        self.__Client=new
    
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
       return f"{self.__numero} \t {self.__Client.nom} \t {self.__Client.prenom}\t  {self.__Client.ville} \t {self.__solde}"


c1=Client("ilyass","Ennaqui","Casablanca")
c2=Client("Moha","Ennaqui","Rabat")
cpt=Compte(1000,c1,12000)
print(cpt)
print("depot de 5000")
cpt.Deposer(5000)
print(cpt)
print("Retrait de 10000")
cpt.Retirer(10000)
print(cpt)