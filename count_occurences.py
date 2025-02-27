nombres = []
for i in range (5):
    num = int(input("Ton nombre :" ))
    nombres.append(num)
numero_different = int(input("Entre un nouveau nombre ici: "))
resultat = nombres.count(numero_different)
print("Le nombre apparait", resultat, "fois")