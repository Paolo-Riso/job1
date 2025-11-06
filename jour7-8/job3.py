n = int(input("taille du tapis :"))

p = "+"
mo = "-"
l = "|"
m = "#"
s = " "

#def expend(n):
#    print (p+ mo*n+p)
#    for i in range (n):
#        print (l + m*n + l)
#    print (p+ mo*n+p)

#expend(n)
    


def expend(n):
    print(p + mo*(n) + p)
    for i in range(n):
        ligne = ""
        for j in range(n):
            if j == n - 1 - i:
                ligne += s
            else:
                ligne += m
        print(l + ligne + l)
    print(p + mo*(n) + p)

expend(n)