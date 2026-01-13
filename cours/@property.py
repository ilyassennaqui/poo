class person:
    def __init__(self,nom,prenom,ville='casablanca'):
        self.__nom=nom
        self.__prenom=prenom
        self.__ville=ville
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    
    def __str__(self):
        return f"{self.__nom}\t{self.__prenom}\t{self.__ville}"

if __name__=="__main__":
    p1=person ('ayoub',22)
    print(p1)
    
    p2=person ('aicha')
    print(p2.Nom)