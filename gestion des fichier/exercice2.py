class Stagiaire:
    c=1
    def __init__(self,name,aka,filiere):
        self.Numero=Stagiaire.c
        self.__nom=name
        self.__prenom=aka
        self.__filiere=filiere
        Stagiaire.c+=1
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,n):
        self.__nom=n
    @property
    def Prenom(self):
        return self.__prenom
    @Prenom.setter
    def Prenom(self,n):
        self.__prenom=n
    @property
    def Filiere(self):
        return self.__filiere
    @Filiere.setter
    def Filiere(self,n):
        self.__filiere=n
    def __str__(self):
        return f"{self.Numero}\t{self.__nom}\t{self.__prenom}\t{self.__filiere}"

if __name__=="__main__":
    Lstg=[]
    s1=Stagiaire("Adam","Elbahja","Dev")
    s2=Stagiaire("Mohamed","Elmzabite","Dev")
    s3=Stagiaire("Rayane","Lasfar","Dev")
    s4=Stagiaire("Abdellah","yassin","Dev")
    Lstg.append(s1) 
    Lstg.append(s2)
    Lstg.append(s3)
    Lstg.append(s4)

    with open("data2.csv","w") as g:
        for s in Lstg:
            g.write(str(s.Numero)+";"+ s.Nom +";" + s.Prenom +";" + s.Filiere + "\n")
    print("Exportation avec succes ")
    
