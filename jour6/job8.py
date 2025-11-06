liste = [8,24,27,48,2,16,9,7,84,91]

somme = 0

for x in liste:
    if x % 2 == 0:
        somme += x
    else:
        print (f"{x} n'est pas paire")

print ("La somme des valeur paire est :",somme)