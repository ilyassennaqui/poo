from datetime import datetime ,date,timedelta
d1=datetime.today()
#pour afficher la date complet avec l'horaire jour+heure
print(d1)
d2=date.today()
#pour afficher juste la date du joure
print(d2)
#pour extraire le jour , mois , annee
j=d2.day
print(f"Jour : {j} ")
m=d2.month
print(f"le mois est : {m} ")
y=d2.year
print(f"l'annee est : {y} ")
#pour afficher les heures seulement
h=d1.hour#ici d2 doesn't work car d2 contient seulement la date du jour
print(f"le nombre d'heure est : {h} ")
#pour afficher les minutes seulement
min=d1.minute
print(f"minutes : {min}")
#pour afficher les secondes seulement
sec=d1.second
print(f"secondes : {sec}")
#en utilisant les formats 
print(f"le jour est : {d1:%d}")
print(f"le mois est : {d1:%B}")
print(f"l'annee est : {d1:%Y}")
#Comparaison entre 2 dates 
#Date 1
'''j1=int(input("Taper le jour du premier date :"))
m1=int(input("Taper le mois du premier date :"))
a1=int(input("Taper l'anneè du premier date :"))
d1=date(a1,m1,j1)
#Date 2
j2=int(input("Taper le jour du deuxieme date :"))
m2=int(input("Taper le mois du deuxieme date :"))
a2=int(input("Taper l'anneè du deuxieme date :"))
d2=date(a2,m2,j2)
#Apres les construction des deux dates , on compare:
if d1>d2:
    print("la premiere date est superieure à la seconde")
else:
    print("la premiere date est inferieure à la seconde")'''
#pour ajouter un intervalle sur le temps on importe timedelta
delta=timedelta(days=10)
print(F"dans dix jours , la date sera : {d1+delta}")
print(F"Avant dix jours , la date sera : {d1-delta}")
#comment convertir la saisie de l'utilisateur à une date
dt=input(F"Taper la date de votre naissance sous forme jj/mm/aa : ")
#print(F"l'annee est {dt.year}")
#pour cela on utlise la methode strptime() de la class datetime
#quui prend comme parametre la chaine et le format
#strptime=string Parse Time
dns=datetime.strptime(dt,"%d/%m/%Y")
print(F"L'année est :{dns.year}")
def getAge(inputdate:str):
    auj=date.today()
    dnb=datetime.strptime(inputdate,"%d/%m/%Y")
    age=auj.year - dnb.year
    if auj.month<dnb.month or (auj.month==dnb.month and auj.day<dnb.day):
        age-=1
    return age
A=getAge("10/12/2010")
print(F"L'age est : {A} ans")