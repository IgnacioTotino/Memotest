import random

def tablero_chico()-> list:
    ''' PRE:------

        POST:retorna un tablero de 4x4 ordenado con simbolos'''

    chico = [['♥','♦','♣','♠'],     
             ['♫','♪','♂','♀'],
             ['♥','♦','♣','♠'],
             ['♫','♪','♂','♀'],] #4x4

             #[['1','2','3','4'],       #si no funciona aca esta el original
             #['5','6','7','8'],
             #['1','2','3','4'],
             #['5','6','7','8'],]
    return chico 

def tablero_mediano()-> list:
    ''' PRE: ----

        POST: retorna una lista ordenada = tablero mediano '''
    mediano = [['1','2','3','4','5','6','7','8'        ],
               ['9','10','11','12','13','14','15','16' ],
               ['17','18','19','20','21','22','23','24'],
               ['25','26','27','28','29','30','31','32'],
               ['1','2','3','4','5','6','7','8'        ],
               ['9','10','11','12','13','14','15','16' ],
               ['17','18','19','20','21','22','23','24'],
               ['25','26','27','28','29','30','31','32'],] #8x8
    return mediano

def tablero_grande()-> list:
    ''' PRE: ----

        POST: retorna una lista ordenada = tablero grande'''
    grande= [['1','2','3','4','5','6','7','8','9','10','11','12'         ],
             ['13','14','15','16','17','18','19','20','21','22','23','24'],
             ['25','26','27','28','29','30','31','32','33','34','35','36'],
             ['37','38','39','40','41','42','43','44','45','46','47','48'],
             ['49','50','51','52','53','54','55','56','57','58','59','60'],
             ['61','62','63','64','65','66','67','68','69','70','71','72'],
             ['1','2','3','4','5','6','7','8','9','10','11','12'         ],
             ['13','14','15','16','17','18','19','20','21','22','23','24'],
             ['25','26','27','28','29','30','31','32','33','34','35','36'],
             ['37','38','39','40','41','42','43','44','45','46','47','48'],
             ['49','50','51','52','53','54','55','56','57','58','59','60'],
             ['61','62','63','64','65','66','67','68','69','70','71','72'],] #12x12
    return grande

def tablero_oculto(tam_tablero : int)-> list:
    ''' PRE: recibe un numero int de acorde al tamaño del tablero seleccionado

        POST: retorna ese tablero completo de ceros  '''

    tablero= list()
    for i in range(tam_tablero):
        tablero.append(['0']*tam_tablero)
    return tablero

def mostrar_tablero(tablero: list,tam_tablero: int)-> list:
    ''' PRE: recibe una tablero y un numero int de acorde a su tamaño

        POST: imprime ese tablero '''

    for i in range(tam_tablero):
        for j in range(tam_tablero):
           print(tablero[i][j], end=" ")
        print("\n")

def validar_tamagnio()-> int:
    ''' PRE: -----

        POST: devuelve un numero int y lo retorna. Que solo pueden ser 3 opcciones y ese es el tamaño del tablero '''

    print("Con que tamaño de tablero van a querer jugar? \n4)  Chico   \n8)  Mediano\n12) Grande ")
    numero = input("=> ")
    while not numero.isnumeric() or (int(numero)!= 4) and (int(numero)!= 8) and (int(numero)!= 12):
        print("ERROR! intente nuevamente")
        numero = input("Ingrese una opccion valida: ")
    
    return int(numero)

def seleccionar_tablero(tam_tablero: int)-> list:  #EL ERROR COMIENZA DE ACA  
    ''' PRE: recibe un int equivalente al tamaño del tablero

        POST: lo retorna un tablero '''
    
    if tam_tablero == 4:
        return tablero_chico()
    elif tam_tablero == 8:
        return tablero_mediano()
    elif tam_tablero == 12:
        return tablero_grande()
     
def carta_layout(tablero: list )-> list:
    ''' PRE: recibe un tablero

        POST: redistribuye todas las fulas del tablero de manera aleatoria '''
    random.shuffle(tablero)
    return tablero

def carta_toti(tablero: list)-> list:
    ''' PRE: recibe un tablero = lista 

        POST: puede o no espejar esetablero verticalmente '''
    espejada = []
    dado = random.randint(0,1)
    if dado == 0:
        espejada = list(reversed(tablero)) # espeja el tablero verticalmente
    else:
        espejada = tablero                 #devuelve lo mismo
    return espejada

def carta_fatality(tablero: list)->list:
    ''' PRE: recibe un tablero

        POST: traspone todo el tablero '''
    
    traspuesta = [] 
    for i in range(len(tablero)):
        traspuesta.append([])
        for j in range(len(tablero)):
            traspuesta[i].append(tablero[j][i]) #cambio el orden de la fila con la columna 
    return traspuesta
 
def pedir_probabilidad()-> int:
    ''' PRE: ----

        POST: retorna las probabilidades de cada carta, no tiene validaciones ''' 

    print("Del 0 al 100 defini la probabilidad de que salga esa carta, ¡Equivale a su porcentaje!.")
    prob_replay = int(input("Probavilidad de la carta Replay: "))
    prob_layout = int(input("Probavilidad de la carta Layout: "))
    prob_toti = int(input("Probavilidad de la carta Toti: "))
    prob_fatality = int(input("Probavilidad de la carta Fatality: "))
    
    return prob_replay, prob_layout, prob_toti, prob_fatality

def carta_por_sorteo(prob_replay:int, prob_layout:int, prob_toti:int, prob_fatality:int)-> None:
    ''' PRE: recibe probabilidades de cada una de las cartas

        POST: puede o no retornar el nombre de la carta en forma de un string '''
    
    sorteada = ""
    primer_sorteo = random.randint(1,4)

    if primer_sorteo == 1:                                #Si es elejida retorna el nombre carta replay
        segundo_sorteo = random.randint(0,100)
        if segundo_sorteo <= len(range(prob_replay)):
            print("Obtuviste una carta Replay \n")
            carta_sorteada_replay = "replay"
            sorteada += carta_sorteada_replay
        else:
            print("No obtuviste una carta este turno \n")

    elif primer_sorteo == 2:                              #Si es elejida retorna el nombre carta layout
        segundo_sorteo = random.randint(0,100)
        if segundo_sorteo <= len(range(prob_layout)):
            print("Obtuviste una carta Layout \n")
            carta_sorteada_layout = "layout"
            sorteada += carta_sorteada_layout
        else:
            print("No obtuviste una carta este turno \n")

    elif primer_sorteo == 3:                              #Si es elejida retorna el nombre carta toti
        segundo_sorteo = random.randint(0,100)
        if segundo_sorteo <= len(range(prob_toti)):
            print("Obtuviste una carta Toti \n")
            carta_sorteada_toti = "toti"
            sorteada += carta_sorteada_toti
        else:
            print("No obtuviste una carta este turno \n")

    else:                                                 #Si es elejida retorna el nombre carta fatality
        segundo_sorteo = random.randint(0,100)
        if segundo_sorteo <= len(range(prob_fatality)):
            print("Obtuviste una carta Fatality \n")
            carta_sorteada_fatality = "fatality"
            sorteada += carta_sorteada_fatality
        else:
            print("No obtuviste una carta este turno \n")

    return sorteada

def jugar_carta(mazo_jugador: list,tablero: list)-> list:
    ''' PRE: recibe un mazo de cartas = lista y un tablero

        POST: si el mazo esta vacio no hace nada, si no le pregunta al jugador si quiere jugar su carta
            retorna la funcion de dicha carta, menos la REPLAY '''
      
    if mazo_jugador == ['']:
        mazo_jugador.remove('')
        print("Tu mazo esta vacio\n")
    else:
        print("Queres usar una carta en este turno? si/no")
        print("              !!!!!!              ")
        print("SI TE OBTUVISTES UNA CARTA REPLAY PONE QUE NO")
        print("              !!!!!!              ")

        opcion = input("=> ")
        if opcion == "si":
            print("Que carta queres jugar?\n l: layout, t: toti, f: fatality")
            eleccion = input("=>")
            if eleccion == "l":            
                for elemnto in mazo_jugador:
                    mazo_jugador.remove("layout")
                return carta_layout(tablero)
            elif eleccion == "t":
                for elemnto in mazo_jugador:
                    mazo_jugador.remove("toti")
                return carta_toti(tablero)                 
            elif eleccion == "f":
                for elemnto in mazo_jugador:
                    mazo_jugador.remove("fatality")
                return carta_fatality(tablero)
                
            else:
                print("Error :(") # si no pone lo que pido             
        else:
            print("OK, la carta quedo guardada para un proximos turno") # ARREGLAR NO LAS GUARDA

def nombre_jugador1()-> None:
    ''' PRE: ---- 

        POST: retorna el nombre del jugador 1'''

    nombre = input("Ingrese el nombre del jugador (1) : ")
    while nombre.isnumeric()  or not nombre != "":    
        nombre = input("ERROR! Ingrese el nombre del jugador (1): ")
    return nombre

def nombre_jugador2()-> None:
    ''' PRE: ----

        POST: retorna el nombre del jugador 2 '''

    nombre = input("Ingrese el nombre del jugador (2) : ")
    while nombre.isnumeric() or not nombre != "":
        nombre = input("ERROR! Ingrese el nombre del jugador (2) : ")
    return nombre

def posicion_ficha_x1(tam_tablero: int)-> int:
    ''' PRE: recibe un numero int relacionado al tamaño del tablero

        POST: retorna un numero int equivalente a la posicion fila del tablero, ficha1 '''

    print("Para la Ficha 1 =>")
    ficha_x1= input("Eleji la fila: ")
    while not ficha_x1.isnumeric() or ficha_x1 != "" and int(ficha_x1)>=tam_tablero or int(ficha_x1)<0:
        print("ERROR! intente nuevamente")
        ficha_x1= input("Eleji la fila: ")
    return int(ficha_x1)

def posicion_ficha_y1(tam_tablero: int)-> int:
    ''' PRE: recibe un numero int relacionado al tamaño del tablero

        POST: retorna un numero int equivalente a la posicion columna del tablero, ficha1'''

    ficha_y1= input("Eleji la columna: ")
    while not ficha_y1.isnumeric() or ficha_y1!= "" and int(ficha_y1)>=tam_tablero or int(ficha_y1)<0:
        print("ERROR! intente nuevamente")
        ficha_y1=input("Eleji la columna: ")
    return int(ficha_y1)

def posicion_ficha_x2(tam_tablero: int)-> int:
    ''' PRE: recibe un numero int relacionado al tamaño del tablero

        POST: retorna un numero int equivalente a la posicion fila del tablero, ficha2'''

    print("Para la Ficha 2 =>")
    ficha_x2= input("Eleji la fila: ")
    while not ficha_x2.isnumeric() or ficha_x2!="" and int(ficha_x2)>=tam_tablero or int(ficha_x2)<0:
        print("ERROR! intente nuevamente")
        ficha_x2= input("Eleji la fila: ")
    return int(ficha_x2)

def posicion_ficha_y2(tam_tablero: int)-> int:
    ''' PRE: recibe un numero int relacionado al tamaño del tablero

        POST: retorna un numero int equivalente a la posicion columna del tablero, ficha2'''
    
    ficha_y2= input("Eleji la columna: ")
    while not ficha_y2.isnumeric() or ficha_y2 != "" and int(ficha_y2)>=tam_tablero or int(ficha_y2)<0:
        print("ERROR! intente nuevamente")
        ficha_y2=input("Eleji la columna: ")
    return int(ficha_y2)

def comenzar_juego(jugador1:str ,jugador2:str, tablero1:list,tablero2:list, tablero_oculto1:list, tablero_oculto2: list, tam_tablero: int)-> None:
    ''' PRE: recibe el nombre del jugador1, jugador2 sus respectivos tableros y tableros ocultos con un numero int equivalente a su tamaño

        POST: COMIENZA EL JUEGO y retorna un (1) si gano el jugador1 o un (2) si gano el jugador2'''
    turno = 0
    gano_j1 = 1
    gano_j2 = 2
    mazo_jugador1 = list()
    mazo_jugador2 = list()
    terminar_juego = False
    

    #desempaqueto los valores pasados por el usuario
    prob_replay, prob_layout, prob_toti, prob_fatality = pedir_probabilidad()

    while not terminar_juego:

        turno_jugador1 = False
        turno_jugador2 = False  
     #///////////////////////////////////// TURNO JUGADOR 1 ////////////////////////////////////////#
        while not turno_jugador1: 
            turno += 1
            print("")
            print(f"Turno N°{turno} del Jugador(1): {jugador1}")
            print("")
            
            #se guardan las cartas sorteadas en una lista = mazo
            carta_seleccionada1 = carta_por_sorteo(prob_replay, prob_layout, prob_toti, prob_fatality) 
            mazo_jugador1.append(carta_seleccionada1)
            print(f"Mazo del {jugador1}: {mazo_jugador1}\n")

            #para jugar una carta si esta es sorteada
            jugar_carta0 = jugar_carta(mazo_jugador1,tablero2)
            if jugar_carta0 == None:
                print("UWU")
                #tablero2 = tablero2
            else:
                tablero2 = jugar_carta0
        
            #pido el ingreso de las posiciones de las fichas para el jugador 1
            ficha_x1 = posicion_ficha_x1(tam_tablero)
            ficha_y1 = posicion_ficha_y1(tam_tablero)
            #segundo par de fichas
            ficha_x2 = posicion_ficha_x2(tam_tablero)
            ficha_y2 = posicion_ficha_y2(tam_tablero)

            #se fija que no se repitan las coordenadas de ficha1 y ficha2
            if (ficha_x1 == ficha_x2) and (ficha_y1 == ficha_y2):
                print("No podes elegir 2 posiciones iguales!, Intenta de nuevo")
        
            #se fija si las coordenadas pasadas de ficha1 y ficha2 han sido volteadas
            elif (tablero_oculto1[ficha_x1][ficha_y1]!='0' and tablero_oculto1[ficha_x2][ficha_y2]!='0'):
                print("Ese par de fichas ya han sido volteadas! \n")
                
	        #Si encontro un par entonces, las casillas seleccionadas del tablero_oculto1 se hacen iguales al tablero1
            elif (tablero1[ficha_x1][ficha_y1] == tablero1[ficha_x2][ficha_y2]):
                tablero_oculto1[ficha_x1][ficha_y1] = tablero1[ficha_x1][ficha_y1]
                tablero_oculto1[ficha_x2][ficha_y2] = tablero1[ficha_x2][ficha_y2]
                print("")
                print("Encontro un Par! \n")
                mostrar_tablero(tablero_oculto1,tam_tablero)
             
            #Si las fichas tienen diferente simbolo entonces, se muestran las fichas elegidas y luego se vuelven a voltear
            else:
                
                print("")
                print("No son pares \n")
                tablero_oculto1[ficha_x1][ficha_y1] = tablero1[ficha_x1][ficha_y1]
                tablero_oculto1[ficha_x2][ficha_y2] = tablero1[ficha_x2][ficha_y2]
                mostrar_tablero(tablero_oculto1,tam_tablero)

                print("Volteo las fichas \n")
                tablero_oculto1[ficha_x1][ficha_y1] ='0'
                tablero_oculto1[ficha_x2][ficha_y2] ='0'

                #en caso de que tenga guardada en el mazo del jugador1 una CARTA REPLAY
                if "replay" in mazo_jugador1:
                    print("Tenes guardada una carta replay, queres usarla? si/no")
                    opcion1 = input("=> ")
                    if opcion1 == "si":
                        turno_jugador1 = False
                    else:
                        print("queda guardada para un siguiente turno")
                else:
                    turno_jugador2 = False
                    turno_jugador1 = True  
            
            #condicion de corte para que termine el juego !!!!!! debe ser una funcion !!!!
            if (tablero_oculto1 == tablero1):
                print(f"Gano el jugador: {jugador1} en un total de {turno} turnos\n")
                mostrar_tablero(tablero_oculto1,tam_tablero)
                terminar_juego = True
                return gano_j1
        
                  
     #////////////////////////////////// TURNO JUGADOR 2 ///////////////////////////////////////////#
        while not turno_jugador2 :
            turno += 1
            print("")
            print(f"Turno N°{turno} del Jugador(2): {jugador2}")
            print("")

            #se hace el sorteo si obtengo una carta
            carta_seleccionada2 = carta_por_sorteo(prob_replay, prob_layout, prob_toti, prob_fatality) #ARREGLAR perjudica al tablero del jugador
            
            #guarda un str en una lista equivalente a la carta sorteada 
            mazo_jugador2.append(carta_seleccionada2)
            print(f"Mazo de jugador 2: {mazo_jugador2}\n")

            #para jugar una carta si esta es sorteada
            jugar_carta0 = jugar_carta(mazo_jugador2, tablero1)
            if jugar_carta0 == None:
                print("XD")
                #tablero1 = tablero1
            else:
                tablero1 = jugar_carta0

            #pido el ingreso de las posiciones de las fichas para el jugador 2 
            ficha2_x1 = posicion_ficha_x1(tam_tablero)
            ficha2_y1 = posicion_ficha_y1(tam_tablero)
            #segundo par de fichas
            ficha2_x2 = posicion_ficha_x2(tam_tablero)
            ficha2_y2 = posicion_ficha_y2(tam_tablero)

            #se fija que no se repitan las coordenadas de ficha1 y ficha2
            if (ficha2_x1 == ficha2_x2) and (ficha2_y1 == ficha2_y2):
                print("No podes elegir 2 posiciones iguales!, Intenta de nuevo")
        
            #se fija si las coordenadas pasadas de ficha1 y ficha2 han sido volteadas
            elif (tablero_oculto2[ficha2_x1][ficha2_y1]!='0' and tablero_oculto2[ficha2_x2][ficha2_y2]!='0'):
                print("Ese par de fichas ya han sido volteadas! \n")
        
	        #Si encontro un par entonces, las casillas seleccionadas del tablero_oculto se hacen iguales al tablero2
            elif(tablero2[ficha2_x1][ficha2_y1] == tablero2[ficha2_x2][ficha2_y2]):
                tablero_oculto2[ficha2_x1][ficha2_y1] = tablero2[ficha2_x1][ficha2_y1]
                tablero_oculto2[ficha2_x2][ficha2_y2] = tablero2[ficha2_x2][ficha2_y2]
                print("")
                print("Encontro un Par! \n")
                mostrar_tablero(tablero_oculto2,tam_tablero)

            #Si las fichas tienen diferente simbolo entonces, se muestran las fichas elegidas y luego se vuelven a voltear
            else:

                print("")
                print("No son pares \n")
                tablero_oculto2[ficha2_x1][ficha2_y1] = tablero2[ficha2_x1][ficha2_y1]
                tablero_oculto2[ficha2_x2][ficha2_y2] = tablero2[ficha2_x2][ficha2_y2]
                mostrar_tablero(tablero_oculto2,tam_tablero)
        
                print("Volteo las fichas \n")
                tablero_oculto2[ficha2_x1][ficha2_y1] ='0'
                tablero_oculto2[ficha2_x2][ficha2_y2] ='0'

                #en caso de que tenga guardada en el mazo del jugador2 una CARTA REPLAY
                if "replay" in mazo_jugador2:
                    print("Tenes guardada una carta replay, queres usarla? si/no")
                    opcion2 = input("=> ")
                    if opcion2 == "si":
                        turno_jugador2 = False
                    else:
                        print("queda guardada para un siguiente turno")
                else:
                    turno_jugador1 = False
                    turno_jugador2 = True

            #condicion de corte para que termine el juego   
            if (tablero_oculto2 == tablero2):

                print(f"Gano el jugador: {jugador2} en un total de {turno} turnos\n")
                mostrar_tablero(tablero_oculto2,tam_tablero)
                terminar_juego = True
                return gano_j2

   #si se llego aca termina el juego

def mezclar_tablero(tablero:list):
    ''' PRE: recibe un tablero

        POST: retorna el tablero mezclado'''

    for i in range(len(tablero)):
        random.shuffle(tablero[i])
    random.shuffle(tablero)
    return tablero 

def main()-> None:
    '''main'''   
    print("      !!!!!!!!!       ")
    print("BIENVENIDO AL MEMOTEST")  
    print("      !!!!!!!!!       ")
    #nombres de los jugadores
    jugador1 = nombre_jugador1()
    jugador2 = nombre_jugador2()

    #para seleccionar el tablero
    tam_tablero = validar_tamagnio()   
    tablero_seleccionado = seleccionar_tablero(tam_tablero)
    
    #creo 2 copias del tablero seleccionado 
    copia_seleccionado1 = tablero_seleccionado.copy()
    copia_seleccionado2 = tablero_seleccionado.copy()

    #tablero mezclados para cada jugador
    tablero1 = mezclar_tablero(copia_seleccionado1) 
    tablero2 = mezclar_tablero(copia_seleccionado2)   
                                                   
    #tableros ocultos correspondientes a cada jugador                                                
    tablero_oculto1 = tablero_oculto(tam_tablero) 
    tablero_oculto2 = tablero_oculto(tam_tablero)

    #variables
    partidas_jugadas = 1     #los jugadores pueden jugar hasta que se cansen
    partidas_ganadas_j1 = 0
    partidas_ganadas_j2 = 0

    #Comienza el juego con un condicional, "opcion" puede cambiar
    opcion = "si"
    while opcion == "si":
        partidas_jugadas += 1

        #lo unico que devuelve puntos es un 1 o un 2 depende que jugador halla ganado y luego lo comparo para que me sume un contador
        puntos = comenzar_juego(jugador1, jugador2, tablero1, tablero2, tablero_oculto1, tablero_oculto2, tam_tablero)
        if puntos == 1:
            partidas_ganadas_j1 +=1
        else:
            partidas_ganadas_j2 +=1

        print("Quieren seguir jugando? si/no")
        opcion = input("=> ")
    #si sale del while muestra los scores
    else:
        print(f"Total de partidas jugadas: {partidas_jugadas}\n")
        if partidas_ganadas_j1 > partidas_ganadas_j2:
            print(f"El jugador1: {jugador1} fue el que gano mas partidas, Total: {partidas_ganadas_j1}!!!")
            print(f"Y el jugador2: {jugador2} gano {partidas_ganadas_j2} partidas!!!\n")

        elif partidas_ganadas_j1 == partidas_ganadas_j2:
            print("Los 2 jugadores tienen la misma cantidad de partidas ganadas")
            print(f"El jugador1: {jugador1} gano {partidas_ganadas_j1} partidas!!!")
            print(f"El jugador2: {jugador2} gano {partidas_ganadas_j2} partidas!!!\n")
        else:
            print(f"El jugador2: {jugador2} fue el que gano mas partidas, Total: {partidas_ganadas_j2}!!!")
            print(f"Y el jugador1: {jugador1} gano {partidas_ganadas_j1} partidas!!!\n")
        print("Gracias vuelba prontos :D")

main()