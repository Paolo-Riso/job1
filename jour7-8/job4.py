mot = str(input("écrivais:"))

alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def cript(mot):
    for i in range (alph):
        
        lettre = alph
        for j in range (alph):
            if mot == lettre:
                mot = (lettre-3)
                print (mot)

cript(mot)