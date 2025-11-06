wi = int(input("largeur : "))
he = int(input("hauteur : "))
h = "|"
w = "-"
s = " "
def DrawRectangle(wi,he):
    print (h,w * wi,h)
    for i in range (he - 2):
        print(h,s * wi,h)
    print (h,w * wi,h)

DrawRectangle(wi,he)