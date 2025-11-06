L=[10,20,30,40,50]
x=L[2]+L[4]
def i():
    print(L)
    print(L[1])
    L[3]=[x]
    print(L)
    print (L[-1])
print (i())