from time import sleep
import turtle

def disegna_campo(t):
    #disegno le righe verticali
    posx=-200
    posy=150
    t.right(90)
    for i in range(0,4):
        t.penup()
        t.goto(posx, posy)
        t.pendown()
        t.forward(300)
        posx=posx+100
    
    #righe orizzontali 
    posx=-200
    posy=150
    t.left(90)
    for i in range(0,4):
        t.penup()
        t.goto(posx, posy)
        t.pendown()
        t.forward(300)
        posy=posy-100

#controllo se un giocatore vince 
def vittoria(l_v, n): 
 if ((l_v[0] == n  and l_v[1] == n and l_v[2] == n) or (l_v[3] == n and l_v[4] == n and l_v[5] == n) or 
 (l_v[6] == n and l_v[7] == n and l_v[8] == n) or 
 (l_v[0] == n and l_v[3] == n and l_v[6] == n) or (l_v[1] == n and l_v[4] == n and l_v[7] == n) or 
 (l_v[2] == n and l_v[5] == n and l_v[8] == n) or 
 (l_v[0] == n and l_v[4] == n and l_v[8] == n) or (l_v[2] == n and l_v[4] == n and l_v[6] == n)): 
    EsisteVincitore = True
 else: 
    EsisteVincitore = False
 return EsisteVincitore


#disegna cerchio giocatore 1
def g1(x, y, t):
    t.penup()
    t.goto(x, y-10)
    t.pencolor("blue")
    t.pendown()
    t.circle(25)

#disegno cerchio giocatore 2
def g2(x, y, t):
    t.penup()
    t.goto(x, y-10)
    t.pencolor("red")
    t.pendown()
    t.circle(25)



def start_game(t):
    cont=0
    controllo=False
    esci=False
    valori_pos={1:(-150, 100) ,2:(-50,100), 3:(50,100), 4: (-150, 0), 5: (-50, 0), 6: (50, 0), 7 : (-150, -100), 8:(-50, -100),9 : (50, -100) }
    l_valori=[0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("INIZIA GIOCATORE 1.\n")

    while cont<9 and esci == False:
        #ciclo per controllare se la posizione è già occupata
        while controllo == False:
            #controllo se giocatore 1 o 2
            if cont%2 == 0:
                num=1
            else:
                num=2

            #in base al giocatore scrivo a chi tocca nel riquadro della posizione 
            if num==1:
             pos=int(turtle.numinput("GIOCATORE 1", "Inserire posizione",default=0, minval=1, maxval=9 ))
            else:
                pos=int(turtle.numinput("GIOCATORE 2", "Inserire posizione",default=0, minval=1, maxval=9 ))
           
            #se il valore nella posizione inserita è 0 vado ad assegnare ad esso il numero del giocatore          
            if l_valori[pos-1]==0:
                l_valori[pos-1]=num
                controllo=True
            else:
                t.write("POSIZIONE GIA OCCUPATA")

                
        #disegno i cerchi di colore diverso in base al giocatore
        if(num==1):
            g1(valori_pos[pos][0], valori_pos[pos][1], t)
        if (num==2):
            g2(valori_pos[pos][0], valori_pos[pos][1], t)

        #controllo se uno dei 2 giocatori ha vinto
        if vittoria(l_valori, 1):
            t.write("GIOCATORE 1 VINCE!")
            sleep(5)
            esci=True
        if vittoria(l_valori, 2):
            t.write("GIOCATORE 2 VINCE!")
            sleep(5)
            esci=True

        cont=cont+1
        controllo=False


def main():
    turtle.Screen
    tris = turtle.Turtle()
    tris.speed(3)
    disegna_campo(tris)
    start_game(tris)



if __name__ == "__main__":
    main()