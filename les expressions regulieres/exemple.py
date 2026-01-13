#Verifier qu'une chaine comporte un caractere majuscule
import re
motif=r"[A-Z]"
#Exemple de la chaine
ch="deveLoppemEnt"
verifier=re.search(motif,ch)
if verifier:
    print("Chaine validée")
else:
    print("Chaine n'est pas validée")
#la fonction findall() toutes les correspondance d'un motif dans une chaine 
verif=re.findall(motif,ch)
print(verif)