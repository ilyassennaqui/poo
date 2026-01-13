#pourquoi on a ecrit compteur?
#le numero du stagiaire doit etre genere automatiquement par le système ¨
#le premier objet aura le numero :1
#le deuxieme objet aura le numero :1
class Salarié:
    compteur=1000
    def __init__(self,name=None,aka=None,salaire=None):
        self.__matrecule=Salarié.compteur
        self.__nom=name
        self.__prenom=aka
        self.__salaire=salaire
        Salarié.compteur+=1
    '''# GETTER FOR MATRECULE
    def getMatricule(self):
        return self.__matrecule
    #SETTER FOR MATRECULE
    def setMatricule(self,new):
        self.__salaire=new'''# on a supprimer ca car on a ajouter le compteur pour que 
    #le numero de matrecule saisie automatiquement
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

    def __str__(self):
        return f"{self.__matrecule} \t {self.__nom} \t {self.__prenom} \t {self.__salaire}"
    
sal1=Salarié()
sal1.setName("ilyass")
sal1.setAKA("ENNAQUI")
sal1.setSalaire(25000)
print(sal1)
#if we use @property we affecte les valeur en ecrivant nom d'objet.nomattribut
sal2=Salarié()
sal2.setName("ilyass")
sal2.setAKA("ENNAQUI")
sal2.setSalaire(25000)
print(sal2)