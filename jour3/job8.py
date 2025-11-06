a = float(input("entrer la longeure du coté a:"))
b = float(input("entrer la longeure du coté b:"))
c = float(input("entrer la longeure du coté c:"))

if a + b > c and a + c > b and b + c > a:
    print ("\n le tritri peux exister !")

    if a == b == c:
         print("est un triangle équilateral!")

    elif a == b or a == c or b == c:
         if(a**2 + b**2 == c**2)or(a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
              print ("le triangle est isocèle et rectangle!")
         else:
              print ("le triangle est isocèle !")
    elif (a**2 + b**2== c**2)or(a**2 + c**2 == a**2):
         print ("le triangle est rectangle !")
    else:
         print("le triangle est quelconque (aucune égalité particulière)!")
else:
     print ("\n ca ne peux pas former un triangle.")


         
