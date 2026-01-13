class personne:
    def __init__(self,n,nom,age):
        self.Numero=n
        self.__nom=nom
        #if age <0:
            #raise  ErreurAge() on peut mettre ca et c'est juste mais il est meilleur de :
        self.Age=age
    
    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,n):
        
        self.Numero=n
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,n):
        self.__nom=n
    
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self,n):
        if n<0:
            raise ErreurAge()
        self.__age=n

    def __str__(self):
        return f"{self.__numero}\t {self.__nom} \t {self.__age}"
class ErreurAge(Exception):
    def __init__(self):
        super().__init__("L'age doit etre positif")

if __name__=="__main__":
    try:
        p=personne(1,"ilyass",-18)
    except ErreurAge as e:
        print(F"Erreur:{e}")
    