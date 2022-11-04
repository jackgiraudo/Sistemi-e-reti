def leggi_file(nome_file):
    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    diz = {"id":[], "nomi":[]}

    for riga in lista_righe[1:]:
        riga_senza_linefeed = riga[:-1]
        lista_campi= riga_senza_linefeed.split(",")
        id=int(lista_campi[0])
        nome=lista_campi[1]
        diz["id"].append(id)
        diz["nomi"].append(nome)

    return diz


def trova_nome_con_id(id, diz):
    listaId=diz["id"]
    listaNomi=diz["nomi"]
    for i, n in zip(listaId, listaNomi):
        if i == id:
            return n

def main():
    diz=leggi_file("./matematici.csv")
    print(diz)
    id=2
    nome = trova_nome_con_id(id, diz)
    print(nome)

if __name__=="__main__":
    main()
