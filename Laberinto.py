from typing import List
import numpy as np
import pandas as pd
import matplotlib as plt
import random

def Generar_mapa():
    N = int(input("Los mapas son cuadrados, el mapa mas chico es de 5x5, elija el tamano del mapa: "))+2
    if(N<7):
        return print("Error, no se puede hacer mapas mas chicos que 5x5.")
        
    Map = np.arange(N*N)
    Map = Map.reshape(N, N)
    Map = Map.tolist()

    for i in range(1, N, 1):
        for u in range(1, N, 1):
            num = random.randint(0, 4)
            if(num==0):
                Map[i][u] = " "
            else:
                Map[i][u] = "X"

    #Generate the walls and the beginning and end of the route
    Map[0] = ["X" for i in range(0, N, 1)]
    Map[0][1] = "▀"
    Map[N-1] = ["X" for i in range(0, N, 1)]
    Map[N-1][N-2] = "◯"
    for i in range(1, N-1, 1):
        Map[i][0] = "X"
        Map[i][N-1] = "X"
    for w in Map:
        print(w)


    #Generate the solution path.
    Movimientos = []
    print("La senalizacion de los movimientos: 🢘 🢛 🢚 🢙")
    X = 1
    Y = 1
    Map[X][Y] = "▀"
    #contador = (N*N)/2 - ((N*N)/2)%1
    contador = 10000
    print("Contador inicial = ", contador, "♡")
    print("\n\n\n\n")
    while((Map[N-1][N-2] == "◯")and(contador>0)):
        contador -= 1
        Aleatorio1 = random.randint(1, 4) #Left=1, Down=2, Right=3, UP=4.
        Movimientos.append(Aleatorio1)
        #Aleatorio2 = random.randint(1, 3) #Move the snake.

        if((X==(N-2))and(Y==(N-2))):
            Map[X][Y] = "🢛"
            X += 1
            Map[X][Y] = "♡"
            contador=0
            print("Fin.")
        
        elif(Aleatorio1==1):
            if((((Y-1)!=0)and((Y-1)!=(N-1)))):
                Map[X][Y] = "🢘"
                Y -= 1  

        elif(Aleatorio1==2):
            if((((X+1)!=0)and(X+1)!=(N-1))):
                Map[X][Y] = "🢛"
                X += 1

        elif(Aleatorio1==3):
            if(((Y+1)!=0)and((Y+1)!=(N-1))):
                Map[X][Y] = "🢚"
                Y += 1

        elif(Aleatorio1==4):
            if((((X-1)!=0)and((X-1)!=(N-1)))):
                Map[X][Y] = "🢙"
                X -= 1
        
        else:
            pass
        
        
    for i in Map:
        print(i)
    
    print("WIN!")
    print(Movimientos, "\n", len(Movimientos))
    return Map
    
Generar_mapa()