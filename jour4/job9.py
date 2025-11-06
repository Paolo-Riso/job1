def moyenne():
    nt_1 = int(input("1er note :"))
    nt_2 = int(input("2eme note :"))
    nt_3 = int(input("3eme note :"))
    
    return (nt_1 + nt_2 + nt_3) / 3
    
moy = moyenne()

if moy <8:
    print(f"{moy} : élève devant faire des efforts")
elif moy <11:
    print (f"{moy} élève moyen")
elif moy <15:
    print (f"{moy}Bon élève")
else:
    print (f"{moy}Très bon élève")

print (moy)




    