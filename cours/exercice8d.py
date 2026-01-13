import re
class stagiaire:
    def __init__(self,n,nom):
        motif=r"^\d{12}$"
        v=re.search(motif,str(n))
        if v:
            self.__numero=str(n)
            self.__nom=nom
        else:
            raise Exception("le numero doit etre composee 12 chiffre")
    
    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,new):
        self.__numero=str(new)
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    def __eq__(self, value):
        if isinstance(value,stagiaire):
           return self.Numero==value.Numero
        return False 
    def __str__(self):
        return f"Stagiaire {self.__numero}:{self.__nom}"
    
class club:
    def __init__(self,nomclub):
        self.lmemberbs=[]
        self.__nomclub=nomclub
    
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new

    @property
    def Nom(self):
        return self.lmemberbs
    
    

    



if __name__=="__main__":
    s=stagiaire(199611050077,"Hassan SOUFIANI")
    s1=stagiaire(1996110500,"Imane BARKAOUI")
    