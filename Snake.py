#Modulo time para tiempos entre impresiones y dar la ilusion de frames.
import time

#Modulo os para eliminar consola y reescribirla en cada impresion. 
import os

#Para recibir entradas de datos en tiempo real sin detener el programa.
import msvcrt

def visualizar_tablero(c):
    #Se limpia la consola antes de cada impresion
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""+---------+---------+---------+---------+---------+---------+
|{c[0][0]}|{c[0][1]}|{c[0][2]}|{c[0][3]}|{c[0][4]}|{c[0][5]}|
+---------+---------+---------+---------+---------+---------+
|{c[1][0]}|{c[1][1]}|{c[1][2]}|{c[1][3]}|{c[1][4]}|{c[1][5]}|
+---------+---------+---------+---------+---------+---------+
|{c[2][0]}|{c[2][1]}|{c[2][2]}|{c[2][3]}|{c[2][4]}|{c[2][5]}|
+---------+---------+---------+---------+---------+---------+
|{c[3][0]}|{c[3][1]}|{c[3][2]}|{c[3][3]}|{c[3][4]}|{c[3][5]}|
+---------+---------+---------+---------+---------+---------+
|{c[4][0]}|{c[4][1]}|{c[4][2]}|{c[4][3]}|{c[4][4]}|{c[4][5]}|
+---------+---------+---------+---------+---------+---------+
|{c[5][0]}|{c[5][1]}|{c[5][2]}|{c[5][3]}|{c[5][4]}|{c[5][5]}|
+---------+---------+---------+---------+---------+---------+
""")


def desplazamiento(tablero,movimiento,posicion):
    posicion_en_i = posicion[0]
    posicion_en_j = posicion[1]
    
    #Movimiento hacia la derecha
    if movimiento == "d":
        if posicion_en_j < 5:
            tablero[posicion_en_i][posicion_en_j] = "         "
            posicion_en_j += 1
            tablero[posicion_en_i][posicion_en_j] = "    0    "

    posicion = [posicion_en_i,posicion_en_j]
    datos = [tablero,posicion]


    

    return datos



def juego():
    muerte = False
    #Movimiento y posicion inicial del gusano.
    movimiento = "d"    
    posicion = [2,2]

    tablero = [["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","    0    ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "]]
    contador = 0

    while muerte == False:
        visualizar_tablero(tablero)
        time.sleep(0.6)
        
        datos = desplazamiento(tablero,movimiento,posicion)
        tablero = datos[0]
        posicion = datos[1]

        if msvcrt.kbhit():           
            movimiento = msvcrt.getch() 
            movimiento = movimiento.decode()

        
        contador = contador + 1
        if contador == 5:
            muerte = True


        


juego()