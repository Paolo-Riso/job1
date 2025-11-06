b = "_"
g = "/"
d = "\\"
e = " "
haut= int(input("hauteur :"))

print (e*(haut) + 1 + d )
def drw_tri (haut):
    for i in range (haut - 2):
        print(e*haut - (1+i)) + 1 + e * (((i+2)+i) + d)
drw_tri(haut)
print(e+1+b*((haut -1)* 2) + d)