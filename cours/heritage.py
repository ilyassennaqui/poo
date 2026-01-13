class Personne:
    def __init__(self,num,n,a):
        self.numero=num
        self.nom=n
        self.age=a
    def afficher(self):
        print(f"Numero:{self.numero}")
        print(f"Nom:{self.nom}")
        print(f"Age:{self.age}")
#class stagiaire herite de la classe personne
#creer la classe stagiaire qui a de plus une filiere
class Stagiaire(Personne):
    def __init__(self,num,n,a,f):
        #appele le constructeur de la classe mere
        super().__init__(num,n,a) 
        self.filiere=f
    def afficher(self):
         super().afficher()
         print(f"filiere:{self.filiere}")
if __name__=='__main__':
    stg=Stagiaire(100,"ayoub",19,"dev")
    stg.afficher()
   # print(f"{stg.numero}\t{stg.nom}\t{stg.filiere}\t{stg.age}")