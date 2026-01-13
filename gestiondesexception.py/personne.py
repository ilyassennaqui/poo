class personne:
    def __init__(self,n,nom,age):
        self.numero=n
        self.nom=nom
        if age <0:
            raise  ErreurAge()
        self.age=age
    
    def __str__(self):
        return f"{self.numero}\t {self.nom} \t {self.age}"
class ErreurAge(Exception):
    def __init__(self):
        super().__init__("L'age doit etre positif")
if __name__=="__main__":
    try:
        p=personne(1,"ilyass",-18)
    except ErreurAge as e:
        print(F"Erreur:{e}")