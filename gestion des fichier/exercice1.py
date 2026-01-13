#\t
f=open("table.txt","w")
f.write("\t \t Table de multiplication \n") 
f.write("X \t")
for i in range(1,10):
    f.write(str(i))
    f.write("\t")
f.write("\n")
for i in range(1,10):
    f.write(str(i))
    f.write("\t")
    for j in range(1,10):
        f.write(str(i*j))
        f.write("\t")
    f.write("\n")
f.close()
#version amelioree
'''n = 9
with open("table.txt", "w") as f:
    f.write("\t\tTable de multiplication\n")
    f.write("X\t")

    # En-tête
    for i in range(1, n + 1):
        f.write(f"{i}\t")
    f.write("\n")

    # Corps de la table
    for i in range(1, n + 1):
        f.write(f"{i}\t")
        for j in range(1, n + 1):
            f.write(f"{i * j}\t")
        f.write("\n")'''

