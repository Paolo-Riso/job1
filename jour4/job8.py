

def question():
    type = str(input("fruits ou legumes ? :"))
    saison = str(input("été ou hiver ? :"))
    if type == "fruits" and saison == "hiver" :
        return ("orange . mandarine et kiwi")

    elif type == "fruits" and saison == "été" :
        return ("poire, fraise, cassis")

    elif type == "légume" and saison == "hiver" :
        return ("caritte, topinambour, endive")

    elif type == "légume" and saison == "été" :
        return ("artichaut,aubergine,navet")
print (question())