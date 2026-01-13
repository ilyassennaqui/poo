#pour declarer une class en python on utilise le mot-clé  class
class Maclass:
    pass
#pour creer une instance de la classe 
#Maclasse:
obj=Maclass()
#pour acceder a un attribut de la classe on utilise le point
obj.attribut=5
#pour acceder a l'attribut de la classe on utilise le point
print(obj.attribut)
#pour declarer un attribut de la classe on utilise le mot-clé  def
class Maclass2:
    def __init__(self, attribut):
        self.attribut=attribut
