import re
motif=r"^[A-Z][a-z]+$"
ch=input("Taper un chiffre")
verifier=re.search(motif,ch)
if verifier:
    print("Chaine verifier")
else:
    print("saisie n'est pas validée")
