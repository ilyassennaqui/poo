from abc import ABC , abstractmethod
class Comparable:
    @abstractmethod
    def CompareTo(self):
        pass
class Person(Comparable):
    def __init__(self,n,a):
        self.__nom=n
        self.__age=a
    def CompareTo(self,p):
        if isinstance(p,Person):
          return self.__age==p.__age
        return False

class Outils(Comparable):
    def __init__(self,prix,long):
        self.__prix=prix
        self.__longeur=long
    def CompareTo(self,o):
        if isinstance(o,Outils):
            return self.__longeur==o.__longeur
        return False
    
if __name__=="__main__":
    p1=Person("Anass",22)
    p2=Person("Rayan",23)
    if p1.CompareTo(p2):
        print("Les deux personnes ont le même âge")
    else:
        print("Les deux personnes n'ont pas le même âge")
        