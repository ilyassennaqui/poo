#fonction lambda qui affiche un message
msg=lambda:print("bonjour")
#appel
msg()

#somme
s=lambda a,b:a+b
#appel
x=int(input("taper le 1er nombre:"))
y=int(input("taper le 2eme nombre:"))
print(f"la somme est:{s(x,y)}")

#carre
c=lambda x:x*x
x=int(f"le carre est:{c(x)}")

#parite
p=lambda n:"pair"if n%2==0 else "impaire" 
a=int(input("taper un nombre:"))
print(f"le nombre est {p(a)}")

#inverse les elements d une liste
i=lambda maliste:maliste[::-1]
filiere=["math","physique","info","chimie"]
print(i(filiere))