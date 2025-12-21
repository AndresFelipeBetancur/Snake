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
    muerte = False

    #Movimiento hacia la derecha
    if movimiento == "d":
        if posicion_en_j <= 5:
            #muerte = detectar_muerte(posicion,movimiento)
            #if muerte == False:
            tablero[posicion_en_i][posicion_en_j] = "         "
            posicion_en_j += 1

            if posicion_en_j > 5:
                muerte = True
            else:
                tablero[posicion_en_i][posicion_en_j] = "    0    "




    #Movimiento hacia la izquierda
    if movimiento == "a":
        if posicion_en_j >= 0:
            #muerte = detectar_muerte(posicion,movimiento)
            #if muerte == False:
            tablero[posicion_en_i][posicion_en_j] = "         "
            posicion_en_j -= 1

            if posicion_en_j < 0:
                muerte = True
            else:
                tablero[posicion_en_i][posicion_en_j] = "    0    "
    
    

    #Movimiento hacia arriba
    if movimiento == "w":
        if posicion_en_i >= 0:
            #muerte = detectar_muerte(posicion,movimiento)
            #if muerte == False:
            tablero[posicion_en_i][posicion_en_j] = "         "
            posicion_en_i -= 1

            if posicion_en_i < 0:
                muerte = True
            else:
                tablero[posicion_en_i][posicion_en_j] = "    0    "

   

    #Movimiento hacia abajo
    if movimiento == "s":
        if posicion_en_i <= 5:
            #muerte = detectar_muerte(posicion,movimiento)
            #if muerte == False:
            tablero[posicion_en_i][posicion_en_j] = "         "
            posicion_en_i += 1

            if posicion_en_i >= 6:
                muerte = True
            else:
                tablero[posicion_en_i][posicion_en_j] = "    0    "

    

    posicion = [posicion_en_i,posicion_en_j]
    datos = [tablero,posicion,muerte]
    
    return datos

"""
def detectar_muerte(posicion,movimiento):
    posicion_en_i = posicion[0]
    posicion_en_j = posicion[1]

    muerte = False

    if posicion_en_j == 6 and movimiento == "d":
        muerte = True

    if posicion_en_j == -1 and movimiento == "a":
        muerte = True
    
    if posicion_en_i == -1 and movimiento == "w":
        muerte = True

    if posicion_en_i == 5 and movimiento == "s":
        muerte = True

    return muerte
"""

def juego():
    muerte = False
    #Movimiento y posicion inicial del gusano.
    movimiento = "d"    
    posicion = [2,2]
    muerte = False
    tablero = [["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","    0    ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "]]
    

    while muerte == False:
        visualizar_tablero(tablero)
        time.sleep(0.6)
        
        datos = desplazamiento(tablero,movimiento,posicion)
        tablero = datos[0]
        posicion = datos[1]

        muerte = datos[2] 
        

        if msvcrt.kbhit():           
            movimiento = msvcrt.getch() 
            movimiento = movimiento.decode()

   
def introduccion():
    opc = 0
    while opc != 3:
        os.system("cls" if os.name == "nt" else "clear")
        print("""Bienvenido a Snake, elige una opcion:
    1. Jugar.
    2. Ver mejor puntuacion.
    3. Salir""")
        opc = int(input("Ingrese una opcion: >"))
        if opc == 1:
            juego()

introduccion()