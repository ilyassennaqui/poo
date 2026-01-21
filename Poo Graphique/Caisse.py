#A al caisee d'un super marche nous beneficions d'une remise sur le montant de nos achats lorsque celle ci 
#depasse 1000DH 
#ecrire un programme qui apres lecture du montant de nos achats , calcule et affiche le montant
#de remise et le montant a payer
# la remise est de :
#5% pour un achat superieure strictement a 1000 et inferieur ou egal a 3000
#7% pour un achat >3000 et inferieure ou egale a 5000dh
#10% au dela 
from tkinter import *
from tkinter import messagebox
import re
mt=Tk()
mt.title("la caisse ")
mt.geometry("500x500")
mt.resizable(False,False)
mt.config(bg="#5E6A7B")
a=StringVar()
b=StringVar()
c=StringVar()
def nouveau():
    rep=messagebox.askyesno("Attention","Réinitialiser le programme ")
    if rep:
        a.set("")
        b.set("")
        c.set("")
        E1.focus()

def calculer():
    motif=r"^\d+\.?\d+$"
    ver=re.search(motif,a.get())
    if ver==None:
        messagebox.showwarning("Attention?","Veuillez saisir un nombre")
    else:
        n=float(a.get())
        if n>1000 and n<=3000:
            r=n*0.05#prix de remise
            p=n-r
            b.set(f"{r:.2f} DHS")
            c.set(f"{p:.2f} DHS")
        elif n>3000 and n<=5000:
            r=n*0.07#prix de remise
            p=n-r
            b.set(f"{r:.2f} DHS")
            c.set(f"{p:.2f} DHS")
        elif n<1000:
            messagebox.showinfo("NOtification","Tu dois depasser 1000DH ")
        else:
            r=n*0.1#prix de remise
            p=n-r
            b.set(f"{r:.2f} DHS")
            c.set(f"{p:.2f} DHS")
def quitter():
    rep=messagebox.askyesno("Quitter","Voulez-vous vraiment quitter")
    if rep:
        mt.destroy()
        

Label(mt, text="Montant Achat :", font=('Segoe UI', 12, 'bold'), bg="#5E6A7B", fg='black').place(x=30, y=70)
E1= Entry(mt, bg="#FCFCFC", fg="#000000", textvariable=a,justify=CENTER)
E1.place(x=210, y=73,width=190,height=30)

Button(mt, text="Nouveau", font=('Segoe UI', 12, 'bold'), bg="#2B2F34", fg="#ffffff", command=nouveau).place(x=50, y=130,width=130,height=45)
Button(mt, text="Calculer", font=('Segoe UI', 12, 'bold'), bg="#2B2F34", fg="#ffffff",command=calculer).place(x=200, y=130 ,width=130,height=45)
Button(mt, text="Quitter", font=('Segoe UI', 12, 'bold'), bg="#2B2F34", fg="#ffffff",command=quitter).place(x=350, y=130 ,width=130,height=45)

Label(mt,text="Montant Remise :",font=('Segoe UI', 12, 'bold'), bg="#5E6A7B",fg="black").place(x=30,y=200)
Label(mt,text="Montant à payer :",font=('Segoe UI', 12, 'bold'), bg="#5E6A7B",fg="black").place(x=30,y=260)
E2= Entry(mt, bg="#FCFCFC", fg="#000000", textvariable=b,justify=CENTER,state="readonly")
E2.place(x=210, y=200,width=190,height=30)
E3= Entry(mt, bg="#FCFCFC", fg="#000000", textvariable=c,justify=CENTER,state="readonly")
E3.place(x=210, y=260,width=190,height=30)


mt.mainloop()