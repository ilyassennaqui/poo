#verifier que tout les caracteres d'une chaine sont en minuscule 
import re
motif=r"^[a-z]+?"
ch=input("Taper ")
verifier=re.search(motif,ch)
if verifier:
    print("Chaine verifier")
else:
    print("saisie n'est pas validée")