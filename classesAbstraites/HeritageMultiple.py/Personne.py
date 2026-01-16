class Personne:
    def __init__(self,n,p):
        self._nom=n
        self._prenom=p
    def __str__(self):
        return F"{self._nom} {self._prenom}"
class InfoSupp:
    def __init__(self,adr,em):
        self._adresse=adr
        self._email=em
    def __str__(self):
        return f"{self._adresse} {self._email}"

class Etudiant(Personne,InfoSupp):
    def __init__(self, n, p,adr,em,f):
        Personne.__init__(self,n,p)
        InfoSupp.__init__(self,adr,em)
        self.filiere=f

    def __str__(self):
        return Personne.__str__(self)+InfoSupp.__str__(self)
    