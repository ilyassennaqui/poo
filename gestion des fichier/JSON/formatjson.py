import json

class Etudiant:  # comme stagiaire

    def __init__(self, num: int, nc: str, nte: float):
        self.__numero = num
        self.__nomComplet = nc
        self.__note = nte

    # les propriétés

    @property
    def Numero(self):
        return self.__numero

    @Numero.setter
    def Numero(self, value):
        self.__numero = value

    @property
    def NomComplet(self):
        return self.__nomComplet

    @NomComplet.setter
    def NomComplet(self, value):
        self.__nomComplet = value

    @property
    def Note(self):
        return self.__note

    @Note.setter
    def Note(self, value):
        self.__note = value

    def toDict(self):
        mondict = {
            "numero": self.Numero,
            "nomComplet": self.NomComplet,
            "noteExam": self.Note
        }
        return mondict

if __name__ == '__main__':
    maliste = []  # pour stocker les etudiants

    et1 = Etudiant(10, "Abid Akram", 17.75)
    et2 = Etudiant(20, "Mourabit Nadia", 18.45)
    et3 = Etudiant(30, "Alami Rachid", 11.05)

    maliste.append(et1)
    maliste.append(et2)
    maliste.append(et3)

    etudiants = []  # nouvelle liste dont les entrées sont des dictionnaires

    for m in maliste:
        etudiants.append(m.toDict())

    # sauvegarder cette nouvelle liste dans un fichier de format JSON
    with open("etudiants.json", "w") as F:
        json.dump(etudiants, F)

    print("Sauvegarde avec succès")