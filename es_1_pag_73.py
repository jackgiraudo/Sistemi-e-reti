"""
pag 73 es 1
n = int(input("Inserire numero"))

if n%3 == 0:
    print("divisibile per 3")
else:
    print("non divisibile")
"""

"""
#pag 73 n2
n = int(input("Inserire numero"))

if n%3 == 0:
    print("divisibile oer 3")
    if n%5 == 0:
        print("divisibile per 5")
"""

#pag 73 n3
def somma(n1,n2):
    ris=n1+n2;
    return ris;

def differenza(n1,n2):
    return n1-n2

def moltiplicazione(n1,n2):
    return n1*n2

def divisione(n1,n2):
    return n1/n2

operazione =input("Inserire quale operazione vuoi: 0->somma , 1->sottrazione, 2->moltiplicazione, 3->divisione ")
n1= int(input("inserire numei su cui eseguire l'operazione"))
n2= int(input("inserire numei su cui eseguire l'operazione"))
diz = {"+":somma, "-":differenza, "*":moltiplicazione, "/":divisione}
print(diz[operazione](n1,n2))

