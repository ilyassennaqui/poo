a=int(input("Taper la date de votre naissance :"))
#a= 2026
try:
    result=2026-a
    print(f"Votre age est {result} ans")
except ValueError:
    print("Erreur de saisie")   
except TypeError:
    print("Type de donnée incorrect")
finally:
    print(" Àge calcul terminé")