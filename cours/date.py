from datetime import datetime

class Stagiaire:
    def __init__(self, code, nom, note, dn):
        self.__code = code
        self.__nom = nom
        self.__note = note
        self.__dn =datetime.strptime(dn,"%d/%m/%Y")

    @property
    def Code(self):
        return self.__code

    @Code.setter
    def Code(self, new):
        self.__code = new

    @property
    def Nom(self):
        return self.__nom

    @Nom.setter
    def Nom(self, new):
        self.__nom = new

    @property
    def Note(self):
        return self.__note

    @Note.setter
    def Note(self, new):
        self.__note = new

    @property
    def DateNaissance(self):
        return self.__dn

    @DateNaissance.setter
    def DateNaissance(self, new):
        self.__dn = new

    def __str__(self):
        return f"{self.__code}\t{self.__nom}\t{self.__note}\t{self.__dn.date()}"

if __name__ == '__main__':
    maliste = []

    stg1 = Stagiaire(1, "anas", 18, "03/03/2006")
    stg2 = Stagiaire(2, "yahya", 16, "04/04/2006")
    stg3 = Stagiaire(3, "salma", 19, "05/02/2006")
    stg4 = Stagiaire(4, "kenza", 18, "29/10/2006")

    maliste.extend([stg1, stg2, stg3, stg4])

    maliste.sort(key=lambda m: m.Note, reverse=True)

    for m in maliste:
        print(m)