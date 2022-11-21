import turtle

def leggi_file(nome_file):
    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    diz = {"istruzione":[], "parametro":[]}

    for riga in lista_righe:
        riga_senza_linefeed = riga[:-1]
        lista_campi= riga_senza_linefeed.split(",")
        parametro=int(lista_campi[0])
        istruzione=lista_campi[1]
        diz["parametro"].append(parametro)
        diz["istruzione"].append(istruzione)

    return diz

def disegna(t, diz):
    diz2={
        "forward": t.forward, 
        "backward":t.backward,
        "right": t.right,
        "left": t.left
    }
    listaParametri=diz["parametro"]
    listaIstruzione=diz["istruzione"]
    for comando, valore in zip(listaIstruzione, listaParametri):
        diz2[comando](valore)
        turtle.done()

def main():
    dizionario=leggi_file("indicazioni.csv")
    print(dizionario)
    turtle.Screen()
    tartaruga=turtle.Turtle()
    disegna(tartaruga, dizionario)


if __name__ == "__main__":
    main()