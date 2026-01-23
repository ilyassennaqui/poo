from tkinter import *
from tkinter import messagebox
from tkinter import ttk
ctr=Tk()
ctr.title("Mon app")
ctr.geometry("500x500")
ctr.resizable(False,False)
ctr.config(bg="black")
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
#fonction
def afficher():
    liste=[]
    if v1.get()==1:
          liste.append("Python")
    if  v2.get()==1:
         liste.append("HTML")
    if v3.get()==1:
        liste.append("JavaScript")
    if v4.get()==1:
         liste.append("PHP")
    if liste:
        choix=""
        for i in liste:
           choix+=f" - {i}\n" #choix=choix+f"{i}/n"
        messagebox.showinfo("Choix",choix)
    else:
        messagebox.showerror("Attention","Vous devez choisir un langage")
#Label
Label(ctr, text="Choisissez vos langages préférés : ", font=('Segoe UI', 20, 'bold'), fg='cyan', bg="black").place(x=20, y=10)
#checkboxe
Checkbutton(ctr,text="Python",variable=v1,fg="cyan",bg="black", font=('Segoe UI', 15, 'bold')).place(x=200,y=100)
Checkbutton(ctr,text="HTML",variable=v2 ,fg="cyan",bg="black",font=('Segoe UI', 15, 'bold')).place(x=200,y=150)
Checkbutton(ctr,text="JavaScript" ,variable=v3 ,fg="cyan",bg="black",font=('Segoe UI', 15, 'bold')).place(x=200,y=200)
Checkbutton(ctr,text="PHP",variable=v4 ,fg="cyan",bg="black",font=('Segoe UI', 15, 'bold')).place(x=200,y=250)

#buttom
Button(ctr, text="Afficher", font=('Segoe UI', 12, 'bold'), bg="#2563eb", fg="#f8fafc",command=afficher).place(x=130, y=300,width=250)





ctr.mainloop()