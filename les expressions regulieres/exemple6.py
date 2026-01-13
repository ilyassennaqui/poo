#verifier le cin d'un citoyen
import re
motif=r"^[A-Z]{2}[0-9]{5}$"
ch=input("Taper LE CODE CIN")
verifier=re.search(motif,ch)
if verifier:
    print("CIN verifier")
else:
    print("CIN n'est pas validée")