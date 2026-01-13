import re
class Stagiaire:
    def __init__(self,nins,nom):
        motif=r"^[\d]+{12}]$"
        ver=re.search(motif,str(nins))
        if ver:
            self.__ninscription=str(nins)
            self.__nom=nom
        else:
             raise Exception("Le numero doit contenir 12 chiffres")
        
    @property
    def Ninscription(self):
        return self.__ninscription
    @Ninscription.setter
    def Ninscription(self,new):
        #motif=r"^[\d]+{12}]$"
        #ver=re.search(motif,self.ninscription)
        #if ver:
        #   self.ninscription=new
        #else:
        #    raise Exception("Le numero doit contenir 12 chiffres")
        self.__ninscription=str(new)
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    def __str__(self):
        return f"Stagiaire{self.__ninscription} : {self.__nom} "
    def __eq__(self,value):
        if isinstance(value,Stagiaire):
            return self.Ninscription==value.Ninscription
        return False
    
if __name__=="__main__":
    s=Stagiaire(120,"Amin")
    s1=Stagiaire(120,"Amina")
    print(s==s1)