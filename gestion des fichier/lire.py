f=open("gestion des fichier/monfichier.txt","r")
A=f.read()
#A=f.readline() #permet d'afficher la 1ere ligne
#A=f.readline() #permet d'afficher les lignes  sous forme de liste
f.close()
print(A)
#cette methode permet de creer une nouvelle 
montexte="Bonjour tout le monde"
c=open("data.txt","w")
c.write(montexte)
c.close()
print("Sauvegarde avec succes")
#pour eviter le probleme de la fermeture

with open("gestion des fichier/monfichier.txt","r") as f:
  d=f.read()
  print(d)
