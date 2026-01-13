import re
motif=r"[0-9]"
ch=input("Taper un chiffre")
verifier=re.search(motif,ch)
if verifier:
    print("Chaine verifier")
else:
    print("saisie n'est pas validée")
    #Si on saisie par exemple 78 la saisie 