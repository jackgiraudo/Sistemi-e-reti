diz={"w":"avanti", "a": "sinistra", "d":"destra", "s":"indietro", "i":"avanti", "j":"sinistra", "k":"indietro", "l":"destra"}

lista=[]

for chiave in diz:
    if diz[chiave] == "avanti":
        lista.append(chiave)

print(lista)