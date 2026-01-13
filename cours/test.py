class Stagiaire:
    def __init__(self,nom=None,prenom=None,age=None):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    @property
    def Prenom(self):
        return self.__prenom
    @Prenom.setter
    def Prenom(self,new):
        self.__=new
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self,new):
        self.__age=new
    def __str__(self):
        return f"{self.__nom}\t{self.__prenom}\t{self.__age}"
    
stg1=Stagiaire("Mohamed","Ennaqui",58)
print(stg1)
stg1.Nom="Anass"
print(stg1)
print(stg1.Nom)
