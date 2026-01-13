from datetime import datetime,date,timedelta
class Article:
    def __init__(self, num, prix, qte_stock, qte_min):
        self._num = num
        self._prix = prix
        self._qte_stock = qte_stock
        self._qte_min = qte_min

    def get_num(self):
        return self._num

    def get_prix(self):
        return self._prix

    def get_qte_stock(self):
        return self._qte_stock

    def get_qte_min(self):
        return self._qte_min

    def set_prix(self, prix):
        self._prix = prix

    def set_qte_stock(self, qte_stock):
        self._qte_stock = qte_stock

    def set_qte_min(self, qte_min):
        self._qte_min = qte_min

    def approvisionner(self, qte):
        self._qte_stock += qte

    def achat(self, qte):
        if self._qte_stock-qte >= self._qte_min:
            self._qte_stock -= qte
        else:
            print("Achat impossible stock insuffisant ")

    def __str__(self):
        return (
            str(self._num) + "\t" +
            str(self._prix) + "\t" +
            str(self._qte_stock) + "\t" +
            str(self._qte_min)
        )

class Habit(Article):
    def __init__(self, num, prix, qte_stock, qte_min, couleur, taille):
        Article.__init__(self, num, prix, qte_stock, qte_min)
        self._couleur = couleur
        self._taille = taille

    def get_couleur(self):
        return self._couleur

    def get_taille(self):
        return self._taille

    def set_couleur(self, couleur):
        self._couleur = couleur

    def set_taille(self, taille):
        self._taille = taille

    def __str__(self):
        return (
            super().__str__() + "\t" +
            str(self._couleur) + "\t" +
            str(self._taille)
        )


class Electromenager(Article):
    def __init__(self, num, prix, qte_stock, qte_min, poids, garantie):
        Article.__init__(self, num, prix, qte_stock, qte_min)
        self._poids = poids
        self._garantie = garantie

    def get_poids(self):
        return self._poids

    def get_garantie(self):
        return self._garantie

    def set_poids(self, poids):
        self._poids = poids

    def set_garantie(self, garantie):
        self._garantie = garantie

    def dateFinGarantie(self):
        d=date.today()
        return d+timedelta(days=self._garantie*30)
    def __str__(self):
        return (
            super().__str__() + f"{self._poids} \t {self._garantie}"
        )

if __name__ == "__main__":
    h = Habit("H01", 200, 10, 3, "Noir", "L")
    print(h)

    h.approvisionner(5)
    print(h)

    e = Electromenager("E01", 1500, 6, 2, 18, 2)
    e.achat(5)
    print(e.dateFinGarantie())
    print(e)