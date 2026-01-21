#Tkinter est une bibliotheque qui permet de generer (creer) une interface graphique utilisateur GUI
from tkinter import *
from tkinter import messagebox
import re
win=Tk()
#Tk est la classe qui contient tout ce qu'il faut pour engendrer une fenetre et la personnaliser (titre, taille, couleur,...)
#definir un titre pour notre fenetre
win.title("Calculator") #exemple: Mon APP
win.geometry("500x400") #redefinir la taille de notre fenetre
#Empecher l'utilisateur de redimensionner notre fenetre (augmenter ou reduire la taille de notre fenetre)
win.resizable(False, False)
#un icone pour notre fenetre
win.iconbitmap()
#couleur d'arriere-plan pour notre fenetre
win.config(bg="#0f172a")
#Declaration des variables
a=StringVar() #pour le 1er nombre
b=StringVar() #pour le 2nd nombre
r=StringVar() #pour le resultat
def nouveau():
  a.set("") #vider le contenu du widget
  b.set("") 
  r.set("")
  E1.focus() #mettre le curseur sur widget E1
def addition():
  motif=r"^\d+\.\d$"
  ver1=re.search(motif,a.get())
  ver2=re.search(motif,b.get())
  if ver1==None:
    messagebox.showerror("error","Veuillez saisir un nombre ")
    a.set("")
    E1.focus()
  if ver2==None:
    messagebox.showerror("Error","Veuillez saisir un nombre ")
    b.set("")
    E2.focus()
  n1=float(a.get())#convertir la le contenue du variable en string
  n2=float(b.get())#convertir la le contenue du variable en string
  r.set(f"{n1+n2:.2f}")#met le resultat 
def quitter():
  rep=messagebox.askyesno("Quitter" ,"Voulez-vous vraiment quitter l'application")
  if rep :
    win.destroy() #permet de quitter l'application
#Labels
Label(win, text="Simple Calculatrice", font=('Segoe UI', 12, 'bold'), fg='cyan', bg='#0f172a').place(x=170, y=10)
Label(win, text="Nombre 1: ", font=('Segoe UI', 11, 'bold'), fg='white', bg="#0f172a").place(x=80, y=65)
Label(win, text="Nombre 2: ", font=('Segoe UI', 11, 'bold'), fg='white', bg="#0f172a").place(x=80, y=100)
Label(win, text="Resultat: ", font=('Segoe UI', 11, 'bold'), fg='white', bg="#0f172a").place(x=80, y=250)
Button(win, text="Nouveau", font=('Segoe UI', 12, 'bold'), bg="#475569", fg="#f8fafc", command=nouveau).place(x=100, y=170)
Button(win, text="Calculer", font=('Segoe UI', 12, 'bold'), bg="#2563eb", fg="#f8fafc",command=addition).place(x=230, y=170)
Button(win, text="Quitter", font=('Segoe UI', 12, 'bold'), bg="#dc2626", fg="#f8fafc" ,command=quitter ).place(x=350, y=170)
#lier le widget E1 a la var a via l'attribut: textvariable
E1= Entry(win, bg="#020617", fg="#f8fafc", textvariable=a)
E1.place(x=220, y=70)
E2= Entry(win, bg="#020617", fg="#f8fafc", textvariable=b)
E2.place(x=220, y=105)
E3= Entry(win, bg="#020617", fg="#f8fafc", textvariable=r)
E3.place(x=220, y=255)
win.mainloop() #pour faire apparaitre notre fenetre
#comment declarer un variable ?
#Stringvar est une classe de tkinter qui est utilisee pour creer et manipuler des variables de chaine de caracteres
#dans une interface graphique
#elle permet de lier dynamiquement une variable de chaine de caracteres a un widgetm de sorte que toute modification de
#la variable sera automatiquement refletee dans le widget et vice-versa

#Syntaxe de declaration:

                      #nomVar=Stringvar()
#la classe StringVar() possede 2 methodes importantes:
# a) nomVar.get(): pour recuperer la valeur du variable nomVar
# b) nomVar.set(new): pour modifier la valeur du variable nomVar
