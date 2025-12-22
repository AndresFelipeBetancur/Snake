#Modulo time para tiempos entre impresiones y dar la ilusion de frames.
import time

#Modulo os para eliminar consola y reescribirla en cada impresion. 
import os

#Para recibir entradas de datos en tiempo real sin detener el programa.
import msvcrt

#Para generar la posicion aleatoria de la comida
import random

#Para reproducir los sonidos del juego
import winsound

def visualizar_tablero(c,puntuacion):
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


Tu puntuacion actual: {puntuacion}""")

 

def desplazamiento(tablero,movimiento,posicion,puntuacion,cola):
    posicion_en_i = posicion[0]
    posicion_en_j = posicion[1]
    comio = False
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
                if tablero[posicion_en_i][posicion_en_j] == "    #    ":
                    puntuacion = puntuacion + 1
                    comio = True
                    
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
                if tablero[posicion_en_i][posicion_en_j] == "    #    ":
                    puntuacion = puntuacion + 1
                    comio = True
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
                if tablero[posicion_en_i][posicion_en_j] == "    #    ":
                    puntuacion = puntuacion + 1
                    comio = True
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
                if tablero[posicion_en_i][posicion_en_j] == "    #    ":
                    puntuacion = puntuacion + 1
                    comio = True
                tablero[posicion_en_i][posicion_en_j] = "    0    "

    
    if comio == True:
        if movimiento == "d":
            posicion_nueva = (posicion_en_i * 10) + (posicion_en_j + 1)
        elif movimiento == "a":
            posicion_nueva = (posicion_en_i * 10) + (posicion_en_j - 1)
        elif movimiento == "w":
            posicion_nueva = (posicion_en_i * 10 + 1) + (posicion_en_j)
        elif movimiento == "s":
            posicion_nueva = (posicion_en_i * 10 - 1) + (posicion_en_j)
        
        cola.append(posicion_nueva)
        

    posicion = [posicion_en_i,posicion_en_j]
    datos = [tablero,posicion,muerte,puntuacion,cola]
    
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

def generar_comida(tablero):
    posiciones_disponibles = []
    hay_comida = False

    for i in range(0,len(tablero)):
        for j in range(0,len(tablero[i])):
            if tablero[i][j] == "         ":   

                posicion_temporal = (i*10)+j
                posiciones_disponibles.append(posicion_temporal)

            if tablero[i][j] == "    #    ":
                    hay_comida = True
    if len(posiciones_disponibles) > 0:
        encontro = False
        while encontro == False:
            posicion_en_i = random.randint(0,4)
            posicion_en_j = random.randint(0,5)

            for i in range(0,len(posiciones_disponibles)):
                if posiciones_disponibles[i] == (posicion_en_i * 10) + posicion_en_j:
                    encontro = True
        
        
        
        if hay_comida == False:
            tablero[posicion_en_i][posicion_en_j] = "    #    "
            return tablero
        else:
            return True

    else:
        return False

def alargar_cola(tablero,cola,posicion,movimiento):
    if movimiento == "d":
        cordenada_cola = (posicion[0]) * 10 + (posicion[1] + 1)
    elif movimiento == "a":
        cordenada_cola = (posicion[0]) * 10 + (posicion[1] - 1)
    elif movimiento == "w":
        cordenada_cola = (posicion[0] * 10 + 1)  + (posicion[1])
    elif movimiento == "w":
        cordenada_cola = (posicion[0] * 10 - 1)  + (posicion[1])

    for i in range(0, len(cola) - 1):
        if i == 0:
            cola[i] = cordenada_cola
        else:
            cola[i] = cola[ i + 1 ]

    for i in range(0,len(tablero)):
        for j in range(0,len(tablero[i])):
            for h in range(0,len(cola)):
                if tablero[i][j] == cola[h]:
                    tablero[i][j] = "    $    "

    return tablero


def juego():
    winsound.PlaySound(None, winsound.SND_PURGE)

    cola = []

    muerte = False
    puntuacion = 0
    #Movimiento y posicion inicial del gusano.
    movimiento = "d"    
    posicion = [2,2]
    tablero = [["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","    0    ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "],["         ","         ","         ","         ","         ","         "]]
    

    while muerte == False:
        visualizar_tablero(tablero,puntuacion)
        time.sleep(0.6)
        
        datos = desplazamiento(tablero,movimiento,posicion,puntuacion,cola)

        tablero = datos[0]
        posicion = datos[1]

        if datos[3] > puntuacion:
            winsound.PlaySound(r"C:\Sonidos\comer.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            tablero = alargar_cola(tablero, cola, posicion,movimiento)

        puntuacion = datos[3]
        cola = datos[4]

        
        


        comida = generar_comida(tablero)

        if type(comida) == list:
            tablero = comida
        elif comida == False:
            muerte = True
        else:
            muerte = datos[2] 
            if msvcrt.kbhit():           
                movimiento = msvcrt.getch() 
                movimiento = movimiento.decode()

    winsound.PlaySound(r"C:\Sonidos\muerte.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    return puntuacion
   
def introduccion():
    opc = 0
    mejor_puntuacion = 0
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound(r"C:\Sonidos\intro.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    while opc != 3:
        
        winsound.PlaySound(r"C:\Sonidos\intro.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

        os.system("cls" if os.name == "nt" else "clear")
        print("""Bienvenido a Snake, elige una opcion:
    1. Jugar.
    2. Ver mejor puntuacion.
    3. Salir""")
        opc = int(input("Ingrese una opcion: >"))
        if opc == 1:
            puntuacion = juego()
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
        if opc == 2:
            if mejor_puntuacion == 0:
                print("Aun no tienes ningun registro.")
                time.sleep(2)
            else:
                print("Esta es tu mejor puntuacion: ", mejor_puntuacion)
                time.sleep(2)

introduccion()