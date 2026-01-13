#pour declarer une class en python on utilise le mot-clé  class
class Maclass:
    pass
#pour creer une instance de la classe 
#Maclasse:
obj=Maclass()
#exemple d'un attribut 
class Stagiaire:
   '''1' numero=0 #attribut age
    nom="" #attribut nom 
    note=0.0'''
   def __init__(self,numero,nom,note):
      self.numero=numero
      self.nom=nom
      self.note=note
   def decision(self):
       if self.note>=10:
           de="Admis"
       elif self.note>=9 and self.note<10:
           de="Racheté"
       else:
           de="Redouble"
       return de
#self.numero represente l'attribut d'instance c-a-d la variable associée à l'objet qui existe 
#à partir de la creation de l'objet jusqu'à sa destruction
#la variable numero reprèsente le paramètre reçu par le constructeur et n'existe pas 
# que dans le corps de ce dernier
   def afficher(self):
        print(f"l'age est {self.numero}")
        print(f"le nom est {self.nom}")
        print(f"la note est {self.note}")
        print(f"la decision est {self.decision()}")
#pour acceder a la valeur d'un attribut,on utilise la syntaxe suivante:
#nomInstance.nomAttribut
#question: definir deux objet de type stagiaire et afficher le meilleur stagiaire
#creation d'un objet de type stagiaire
'''if __name__=="__main__":'''
stg1=Stagiaire(100,"Mohamed",15.25)
stg1.afficher()
stg2=Stagiaire(101,"Moha",16)
stg2.afficher()
if stg1.note>stg2.note:
    print(f"stg1 est le meilleuire")
else:
    print(f"stg2 est le meilleuire")
'''1 façon'stg=Stagiaire()
stg.numero=100
stg.nom="Mohamed"
stg.note=15.25
stg.afficher()'''
#les parenthèses sont très important
#########################################seance 3:
# un stagiaire est definit par numero,nom et sa note à l'examen
#lea attributs doivent etre privés
#on utilise le double underscore __ pour rendre un attribut privé
class Stagiaire:
    def __init__(self,numero,nom,note):
        self.__numero=numero
        self.__nom=nom
        self.__note=note
    def afficher(self):
        print(F"Numero : {self.__numero}")
        print(F"Nom : {self.__nom}")
        print(F"Note : {self.__note}")
    # GETTER FOR NUMERO
    def getNumero(self):
        return self.__numero
    # SETTER FOR NUMERO
    def setNumero(self,new):
         self.__numero=new
    # GETTER FOR NOM
    def getNOM(self):
        return self.__nom
    # SETTER FOR NOM
    def setNOM(self,new):
         self.__nom=new
    # GETTER FOR NOTEE
    def getNote(self):
        return self.__note
    # SETTER FOR NOTEE
    def setNote(self,new):
         self.__note=new
    def __str__(self):
        return f"{self.__numero} \t {self.__nom} \t {self.__note}"

if __name__=="__main__":
    stg=Stagiaire(1000,"Ali",13.55)
    stg.afficher()
    print("-----------------------------------------------")
    # for numero
    #Lire la valeur de l'attribut numero
    print(stg.getNumero())
    # Modifier la valeur de l'attribut numero
    stg.setNumero(3000)
    print(f"Nouveau numero : {stg.getNumero()}")
    print("-----------------------------------------------")
    #for nom
    #Modifier la valeur de l'attribut numero
    stg.setNOM("mohamed")
    # lire la valeur de l'attribut numero
    print(stg.getNOM())
    print("-----------------------------------------------")
    #for notee
    #Modifier la valeur de l'attribut numero
    stg.setNote(18.4)
    # lire la valeur de l'attribut numero
    print(stg.getNote())
    print("-----------------------------------------------")
    stg.afficher()
    print("-----------------------------------------------")
    print(stg)

