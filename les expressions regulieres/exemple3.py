#L'utilisateur doir saisir exactement 2 chiffres
import re
motif=r"^[0-9]{2}$"
ch=input("Taper 2 chiffre :")
verifier=re.search(motif,ch)
if verifier:
    print("Chaine verifier ")
else:
    print("saisie n'est pas validée")