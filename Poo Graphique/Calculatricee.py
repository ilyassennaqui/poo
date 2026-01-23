from tkinter import *
from tkinter import messagebox
from tkinter import ttk #pour combobox
import re

def nouveau():
    a.set("")   
    b.set("")   
    r.set("")   
    E1.focus() 
    op.set(-1) 
def quitter():
    rep=messagebox.askyesno("Quitter","Voulez-vous vraiment quitter l'application?")
    if rep:
        win.destroy() #permet de quitter l'application
operations=['addition','soustraction','multiplication','division']
def calculer():
    motif=r"^-?\d+(\.\d+)?$"
    v1=re.search(motif,a.get())
    v2=re.search(motif,b.get())
    if v1==None:
        messagebox.showerror("Erreur","Veuillez saisir un nombre")
        a.set("")
        E1.focus()
    elif v2==None:
        messagebox.showerror("Erreur","Veuillez saisir un nombre")
        b.set("")
        E2.focus()
    else:
        
        x=float(a.get())#convertit le contenu du variable en float
        y=float(b.get())#convertit le contenu du variable en float
        ope=op.get()
        if ope==0:
            z=x+y
            r.set(f"{z:.2f}")
        elif ope==1:
            z=x-y
            r.set(f"{z:.2f}")
        elif ope==2:
            z=x*y
            r.set(f"{z:.2f}")
        elif ope==3:
            if y==0:
                messagebox.showerror("Erreur","Division par zéro impossible")
                b.set("")
                E2.focus()
                return 
            else:
                z=x/y
            r.set(f"{z:.2f}")
        else:
            messagebox.showerror("Erreur","Veuillez choisir une opération")

win=Tk()

win.title("Mon App")#exemple: Mon App
win.geometry("400x300+300+150")#définir une taille
win.resizable(False,False)
win.config(bg='gray')
a=StringVar()   
b=StringVar()     
r=StringVar()   
op=IntVar()
   
       
#label pour le titre
Label(win,text="Simple Claculatrice",font=('Courier New',12,'bold'),fg='blue',bg='yellow').place(x=150,y=10)
Label(win,text="Le premier nombre:",font=('Courier New',11,'bold'),bg='gray').place(x=20,y=50)
Label(win,text="Le second nombre:",font=('Courier New',11,'bold'),bg='gray').place(x=20,y=80)

Label(win,text="Choisir une opération:",font=('Courier New',11,'bold'),bg='gray').place(x=15,y=110)
#cbo=ttk.Combobox(win,values=operations,textvariable=op)
#cbo.place(x=220,y=110)
#cbo.current(0)  #l'addittion sera séléctionnée par défaut
Button(win,text="Nouveau",font=('Courier New',12,'bold'),bg='black',fg='yellow',command=nouveau).place(x=30,y=200)
Button(win,text="Calculer",font=('Courier New',12,'bold'),bg='black',fg='yellow',command=calculer).place(x=150,y=200)
Button(win,text="Quitter",font=('Courier New',12,'bold'),bg='black',fg='yellow',command=quitter).place(x=270,y=200)
#Radio button
Radiobutton(win,value=0,variable=op,bg="gray",text="+").place(x=20,y=140)
Radiobutton(win,value=1,variable=op,bg="gray",text="-").place(x=80,y=140)
Radiobutton(win,value=2,variable=op,bg="gray",text="x").place(x=160,y=140)
Radiobutton(win,value=3,variable=op,bg="gray",text="/").place(x=240,y=140)
op.set(-1)
E1=Entry(win,textvariable=a)
E1.place(x=220,y=50)
E2=Entry(win,textvariable=b)
E2.place(x=220,y=80)
Label(win,text="Resultat:",font=('Courier New',11,'bold'),bg='gray').place(x=20,y=250)
E3=Entry(win,textvariable=r,state="readonly")
E3.place(x=220,y=250)
win.mainloop() #pour faire apparaître la fenetre