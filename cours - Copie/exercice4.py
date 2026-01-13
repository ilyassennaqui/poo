class Salarié:
    def __init__(self,matrec,name,aka,salaire,taux):
        self.__matrecule=matrec
        self.__nom=name
        self.__prenom=aka
        self.__salaire=salaire
        self.__taux=taux
    def calculerSalaireNet(self):
        return self.__salaire-(self.__salaire*self.__taux)
    # GETTER FOR MATRECULE
    def getMatricule(self):
        return self.__matrecule
    #SETTER FOR MATRECULE
    def setMatricule(self,new):
        self.__salaire=new
    # GETTER FOR NAME
    def getName(self):
        return self.__nom
    #SETTER FOR NAME
    def setName(self,new):
        self.__nom=new
    # GETTER FOR AKA
    def getAKA(self):
        return self.__prenom
    # SETTER FOR AKA
    def setAKA(self,new):
        self.__prenom=new
    # GETTER FOR SALAIRE
    def getSalaire(self):
        return self.__salaire
    # SETTER FOR SALAIRE
    def setSalaire(self,new):
        self.__salaire=new
    # GETTER FOR SALAIRE
    def getTauxCharge(self):
        return self.__taux
    # SETTER FOR SALAIRE
    def setTauxCharge(self,new):
        self.__taux=new
    def __str__(self):
        return f"{self.__matrecule} \t {self.__nom} \t {self.__prenom} \t {self.__salaire} \t {self.__taux} \t {self.calculerSalaireNet()}"
    
sal1=Salarié(1000,"Ali","Mohamed",5000,0.25)
#print(f"le salaire net est {sal1.calculerSalaireNet()}")
sal2=Salarié(1000,"Alaa","yassin",10000,0.25)
#print(f"le salaire net est {sal2.calculerSalaireNet()}")
print(sal1)
print(sal2)


    
    
    