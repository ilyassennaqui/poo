class Chauffeur:
    def __init__(self,c,n,pre):
        self.__cin=c
        self.__nom=n
        self.__prenom=pre
    #for the cin
    @property
    def Cin(self):
        return self.__cin
    #for the name
    @property
    def Nom(self):
        return self.__nom
    #for the prenom
    @property
    def Prenom(self):
        return self.__prenom
    #methode str
    def __str__(self):
        return f"{self.__cin} \t {self.__nom} \t {self.__prenom}"
    
class Bus:
    def __init__(self,matr,marq,typ):
        self.__immatriculation=matr
        self.__marque=marq
        self.__type=typ
    
    #for the immatriculation
    @property
    def Immatriculation(self):
        return self.__immatriculation
    #for marque
    @property
    def Marque(self):
        return self.__marque
    #for type
    @property
    def Type(self):
        return self.__type
    #methode str
    def __str__(self):
        return F"{self.__immatriculation} \t {self.__marque} \t {self.__type}"
    
class Voyage:
    num=1
    def __init__(self,vchauffeur,vbus,date,depart,arrivee,nbvoayageurs,prix):
        self.__numero=Voyage.num
        self.__vchauffeur=vchauffeur
        self.__vbus=vbus
        self.__depart=depart
        self.__arrivee=arrivee
        self.__nbvoyageurs=nbvoayageurs
        self.__prix=prix
        self.__date=date
        Voyage.num+=1
    def Recette(self):
        return self.__nbvoyageurs*self.__prix
    #accesseurs for Numero
    @property
    def Numero(self):
        return self.__numero
    #accesseurs for le chauffeur
    @property
    def Vchauffeur(self):
        return self.__vchauffeur  
    #accesseurs for le bus
    @property
    def Vbus(self):
        return self.__vbus
    #accesseurs for la date de voyage
    @property
    def Date(self):
        return self.__date
    #accesseurs for ville de depart
    @property
    def Depart(self):
        return self.__depart
    #accesseurs for ville d'arrivee
    @property
    def Arrivee(self):
        return self.__arrivee
    #accesseurs for Numero de voyageurs
    @property
    def Nbvoyageurs(self):
        return self.__nbvoyageurs
    #accesseurs for Prix
    @property
    def Prix(self):
        return self.__prix
    #methode str
    def __str__(self):
        return f"{self.__numero} \t {self.__date} \t{self.__vchauffeur.Nom} \t {self.__vbus.Immatriculation} \t  {self.__depart} \t {self.__arrivee} \t {self.__nbvoyageurs} \t {self.__prix} \t {self.Recette()}"
#listes globales
chauffeurs=[]
bus=[]
voyages=[]

def rechercher_chauffeur(cin):
    for c in chauffeurs:
        if c.Cin==cin:
            return c
    return None