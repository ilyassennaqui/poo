import json
class Employe:
    def __init__(self,Matricule,Nom,service,salaire,Taux):
        self.__matricule=Matricule
        self.__nom=Nom
        self.__service=service
        self.__salaire=salaire
        self.__taux=Taux

    @property
    def Matricule(self):
        return self.__matricule
    @Matricule.setter
    def Matricule(self,new):
        self.__matricule=new

    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new

    @property
    def Service(self):
        return self.__service
    @Service.setter
    def Service(self,new):
        self.__service=new
    
    @property
    def Salaire(self):
        return self.__salaire
    @Salaire.setter
    def Salaire(self,new):
        self.__salaire=new

    @property
    def Taux(self):
        return self.__taux
    @Taux.setter
    def Taux(self,new):
        self.__taux=new

    def SalaireNet(self):
        return self.__salaire-(self.__salaire*self.__taux)
    def todict(self):
        return {
            "Matricule": self.__matricule,
            "Nom": self.__nom,
            "Service": self.__service,
            "Salaire": self.__salaire,
            "Taux": self.__taux,
            "SalaireNet": self.SalaireNet()
        }
    
    def __str__(self):
        return f"{self.__matricule}\t{self.__nom}\t{self.__service}\t{self.SalaireNet()}"
    
class Entreprise:
    cd=1
    def __init__(self,raison,ville):
        self.code=Entreprise.cd
        self.raison=raison
        self.ville=ville
        Entreprise.cd+=1
        self.Lemp=[]
        self.nbremp=0
    
    def Ajouter(self,emp):
        if emp in self.Lemp:
            print("Employe deja existe ")
        else:
           self.Lemp.append(emp)
           print("Ajout avec succes ")
           self.nbremp+=1
           ''' ma=int(input("Taper le matricule d'employé :"))
            no=(input("Taper le nom d'employé :"))
            ser=(input("Taper le service d'employé :"))'''
    def Afficher(self):
        print(f"{self.code} \t {self.raison} \t {self.ville}" )
        print("Matricule \t Nom \t Service \t Salaire Net")
        for emp in self.Lemp:
            print(emp)
    def Supprimer(self,emp):
        if emp in self.Lemp:
            rep=bool(input("Voulez vous vraiment supprimer cet employe ? (1/0) :"))
            if rep:
                self.Lemp.remove(emp)
                print("Suppression avec succes ")
                self.nbremp-=1
        else:
            print("Employe n'existe pas ")
    def Exporter(self):
        with open ("employe.json",'w') as f:
            liste=[]
            for emp in self.Lemp:
                liste.append(emp.todict())
            json.dump(liste,f)
            print("Exportation avec succes ")

if __name__=="__main__":
    emp1=Employe(1,"Anass","Dev",10000,0.20)
    emp2=Employe(1,"Yahya","ID",10300,0.20)
    ent=Entreprise("Oracle","Casablanca")
    ent.Ajouter(emp1);ent.Ajouter(emp2)
    Entreprise.Afficher()