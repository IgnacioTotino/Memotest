from random import randint, shuffle

def tablero_chico()-> list:
    ''' PRE: ----

        POST: retorna una lista de listas ordenada del tamaño 4x4'''

    chico =[['1','2','3','4'],       
            ['5','6','7','8'],
            ['1','2','3','4'],
            ['5','6','7','8'],]
    return chico

def tablero_chico_iconos()-> list:
    ''' PRE:------

        POST:retorna un tablero de 4x4 ordenado con simbolos'''

    chico_ic = [['♥','♦','♣','♠'],     
                ['♫','♪','♂','♀'],
                ['♥','♦','♣','♠'],
                ['♫','♪','♂','♀'],] #4x4

    return chico_ic

def tablero_mediano()-> list:
    ''' PRE: ----

        POST: retorna una lista de listas ordenada del tamaño 8x8 '''
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

        POST: retorna una lista de listas ordenada del tamaño 12x12'''
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

def seleccionar_tablero(tam_tablero: int)-> list: 
    ''' PRE: recibe un int equivalente al tamaño del tablero

        POST: lo retorna un tablero '''
    
    if tam_tablero == 4:
        print("Te gustaria usar iconos en vez de numeros? si/no")
        opcion = input("=>")
        if opcion.lower() == "si":
            return tablero_chico_iconos()
        else:
            return tablero_chico()
    elif tam_tablero == 8:
        return tablero_mediano()
    elif tam_tablero == 12:
        return tablero_grande()

def tablero_oculto(tam_tablero : int)-> list:
    ''' PRE: recibe un numero int de acorde al tamaño del tablero seleccionado

        POST: retorna ese tablero completo de ceros  '''

    tablero= []
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

def validar_tamaño()-> int:
    ''' PRE: -----

        POST: devuelve un numero int y lo retorna. Que solo pueden ser 3 opcciones y ese es el tamaño del tablero '''

    print("Con que tamaño de tablero van a querer jugar? \n4)  Chico   \n8)  Mediano\n12) Grande ")
    numero = input("=> ")
    while not (numero.isnumeric() and int(numero) in [4,8,12]):
        print("ERROR! intente nuevamente")
        numero = input("Ingrese una opccion valida: ")
    
    return int(numero)


     
def carta_layout(tablero: list )-> list:
    ''' PRE: recibe un tablero

        POST: redistribuye todas las fulas del tablero de manera aleatoria '''
    shuffle(tablero)
    return tablero

def carta_toti(tablero: list)-> list:
    ''' PRE: recibe un tablero = lista 

        POST: puede o no espejar esetablero verticalmente '''
    espejada = []
    dado = randint(0,1)
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

    print("Del 0 al 100 defini la probabilidad de que salga esa carta, Equivale a su porcentaje.")

    prob_replay = int(input("Probavilidad de la carta Replay: "))   
    prob_layout = int(input("Probavilidad de la carta Layout: "))
    prob_toti = int(input("Probavilidad de la carta Toti: "))
    prob_fatality = int(input("Probavilidad de la carta Fatality: "))
    
    return prob_replay, prob_layout, prob_toti, prob_fatality

def carta_por_sorteo(prob_replay:int, prob_layout:int, prob_toti:int, prob_fatality:int)-> str:
    ''' PRE: recibe probabilidades de cada una de las cartas

        POST: puede o no retornar el nombre de la carta en forma de un string '''
    
    sorteada = ""
    primer_sorteo = randint(1,4)
    segundo_sorteo = randint(0,100)

    if primer_sorteo == 1:                                #Si es elejida retorna el nombre carta replay 
        if segundo_sorteo <= len(range(prob_replay)):
            print("Obtuviste una carta Replay \n")
            carta_sorteada_replay = "replay"
            sorteada = carta_sorteada_replay
        else:
            print("No obtuviste una carta este turno \n")

    elif primer_sorteo == 2:                              #Si es elejida retorna el nombre carta layout
        if segundo_sorteo <= len(range(prob_layout)):
            print("Obtuviste una carta Layout \n")
            carta_sorteada_layout = "layout"
            sorteada = carta_sorteada_layout
        else:
            print("No obtuviste una carta este turno \n")

    elif primer_sorteo == 3:                              #Si es elejida retorna el nombre carta toti
        if segundo_sorteo <= len(range(prob_toti)):
            print("Obtuviste una carta Toti \n")
            carta_sorteada_toti = "toti"
            sorteada = carta_sorteada_toti
        else:
            print("No obtuviste una carta este turno \n")
            
    else:                                                 #Si es elejida retorna el nombre carta fatality
        if segundo_sorteo <= len(range(prob_fatality)):
            print("Obtuviste una carta Fatality \n")
            carta_sorteada_fatality = "fatality"
            sorteada = carta_sorteada_fatality
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
        print("¡SI TE OBTUVISTES UNA CARTA REPLAY PONE QUE NO!")

        opcion = input("=> ")
        if opcion == "si":
            print("Que carta queres jugar?\n l: layout, t: toti, f: fatality")
            eleccion = input("=>")
            if eleccion.lower() == "l" and ("layout") in mazo_jugador:            
                mazo_jugador.remove("layout")
                return carta_layout(tablero)

            elif eleccion.lower() == "t" and ("toti") in mazo_jugador:
                mazo_jugador.remove("toti")
                return carta_toti(tablero)   

            elif eleccion.lower() == "f" and ("fatality") in mazo_jugador:
                mazo_jugador.remove("fatality")
                return carta_fatality(tablero)
                
            else:
                print("Error :(") # si no pone lo que pido             
        else:
            print("OK, la carta quedo guardada para un proximos turno") # ARREGLAR NO LAS GUARDA

def nombre_jugador()-> None:
    ''' PRE: ---- 

        POST: retorna el nombre del jugador 1'''

    nombre = input("=> ")
    while nombre.isnumeric()  or not nombre != "":    
        nombre = input("ERROR! Ingrese un nombre valido: ")
    return nombre


def posicion_ficha(tam_tablero: int)-> int:
    ''' PRE: recibe un numero int relacionado al tamaño del tablero

        POST: retorna un numero int equivalente a la posicion fila del tablero, ficha1 '''

    print("Para la Ficha 1 =>")
    ficha= input("Eleji la fila: ")
    while not ficha.isnumeric() or ficha != "" and int(ficha)>=tam_tablero or int(ficha)<0:
        print("ERROR! intente nuevamente")
        ficha= input("Eleji la fila: ")
    return int(ficha)

def comenzar_juego(jugador1:str ,jugador2:str, tablero1:list,tablero2:list, tablero_oculto1:list, tablero_oculto2: list, tam_tablero: int)-> None:
    ''' PRE: recibe el nombre del jugador1, jugador2 sus respectivos tableros y tableros ocultos con un numero int equivalente a su tamaño

        POST: COMIENZA EL JUEGO y retorna un (1) si gano el jugador1 o un (2) si gano el jugador2'''
    turno = 0
    gano_j1 = 1
    gano_j2 = 2
    mazo_jugador1 = []
    mazo_jugador2 = []
    terminar_juego = False
    

    #desempaqueto los valores pasados por el usuario
    prob_replay, prob_layout, prob_toti, prob_fatality = pedir_probabilidad()

    while not terminar_juego:

        turno_jugador = 1

     #///////////////////////////////////// TURNO JUGADOR 1 ////////////////////////////////////////#
        while turno_jugador == 1 : 
            turno += 1
            print("")
            print(f"Turno N°{turno} del Jugador(1): {jugador1}")
            print("")
                   
            #pido el ingreso de las posiciones de las fichas para el jugador 1
            ficha_x1 = posicion_ficha(tam_tablero)
            ficha_y1 = posicion_ficha(tam_tablero)
            #segundo par de fichas
            ficha_x2 = posicion_ficha(tam_tablero)
            ficha_y2 = posicion_ficha(tam_tablero)

            #verificar_jugada(ficha_x1, ficha_y1,ficha_x2,ficha_y2,tablero1,tablero_oculto1,tam_tablero) ANDA PERO NO ME GUSTA
            
            if (ficha_x1 == ficha_x2) and (ficha_y1 == ficha_y2):
                #se fija que no se repitan las coordenadas de ficha1 y ficha2
                print("No podes elegir 2 posiciones iguales!, Intenta de nuevo")
                   
            elif (tablero_oculto1[ficha_x1][ficha_y1]!='0' and tablero_oculto1[ficha_x2][ficha_y2]!='0'):
                #se fija si las coordenadas pasadas de ficha1 y ficha2 han sido volteadas
                print("Ese par de fichas ya han sido volteadas! \n")
            	        
            elif (tablero1[ficha_x1][ficha_y1] == tablero1[ficha_x2][ficha_y2]):
                #Si encontro un par entonces, las casillas seleccionadas del tablero_oculto1 se hacen iguales al tablero1  
                tablero_oculto1[ficha_x1][ficha_y1] = tablero1[ficha_x1][ficha_y1]
                tablero_oculto1[ficha_x2][ficha_y2] = tablero1[ficha_x2][ficha_y2]
                print("")
                print("Encontro un Par! \n")
                mostrar_tablero(tablero_oculto1,tam_tablero)
                        
            else:
                #Si las fichas tienen diferente simbolo entonces, se muestran las fichas elegidas y luego se vuelven a voltear
                print("")
                print("No son pares \n")
                tablero_oculto1[ficha_x1][ficha_y1] = tablero1[ficha_x1][ficha_y1]
                tablero_oculto1[ficha_x2][ficha_y2] = tablero1[ficha_x2][ficha_y2]
                mostrar_tablero(tablero_oculto1,tam_tablero)

                print("Volteo las fichas \n")
                tablero_oculto1[ficha_x1][ficha_y1] ='0'
                tablero_oculto1[ficha_x2][ficha_y2] ='0'

            #--------------------- Para jugar las cartas al final del turno -------------------------#
                #se guardan las cartas sorteadas en una lista = mazo
                carta_seleccionada1 = carta_por_sorteo(prob_replay, prob_layout, prob_toti, prob_fatality) 
                mazo_jugador1.append(carta_seleccionada1)
                print(f"Mazo del Jugador(1) - {jugador1}: {mazo_jugador1}\n")

                #para jugar una carta si esta es sorteada
                jugar_carta0 = jugar_carta(mazo_jugador1,tablero2)
                if jugar_carta0 == None:
                    tablero2 = tablero2
                else:
                    tablero2 = jugar_carta0
                
            #--------------------------- Caso de carta replay -----------------------------------#
                if "replay" in mazo_jugador1:
                    #en caso de que tenga guardada en el mazo del jugador1 una CARTA REPLAY
                    print("Tenes guardada una carta replay, queres usarla? si/no")
                    opcion1 = input("=> ")
                    if opcion1.lower() == "si":
                        mazo_jugador1.remove("replay")
                        turno_jugador = 1
                    else:
                        print("queda guardada para un siguiente turno")
                        turno_jugador = 2               
                else:
                    #cambio de jugador, si no esta replay en mazo
                    
                    turno_jugador = 2

            #------------------- condicion de corte para que termine el juego  -------------------#
            if (tablero_oculto1 == tablero1):
                
                print(f"Gano el jugador: {jugador1} en un total de {turno} turnos\n")
                mostrar_tablero(tablero_oculto1,tam_tablero)
                terminar_juego = True
                return gano_j1

                      
     #////////////////////////////////// TURNO JUGADOR 2 ///////////////////////////////////////////#
        while turno_jugador == 2 :
            turno += 1
            print("")
            print(f"Turno N°{turno} del Jugador(2): {jugador2}")
            print("")

            #pido el ingreso de las posiciones de las fichas para el jugador 2 
            ficha2_x1 = posicion_ficha(tam_tablero)
            ficha2_y1 = posicion_ficha(tam_tablero)
            #segundo par de fichas
            ficha2_x2 = posicion_ficha(tam_tablero)
            ficha2_y2 = posicion_ficha(tam_tablero)
          
            if (ficha2_x1 == ficha2_x2) and (ficha2_y1 == ficha2_y2):
                #se fija que no se repitan las coordenadas de ficha1 y ficha2
                print("No podes elegir 2 posiciones iguales!, Intenta de nuevo")
                   
            elif (tablero_oculto2[ficha2_x1][ficha2_y1]!='0' and tablero_oculto2[ficha2_x2][ficha2_y2]!='0'):
                #se fija si las coordenadas pasadas de ficha1 y ficha2 han sido volteadas
                print("Ese par de fichas ya han sido volteadas! \n")
        	        
            elif(tablero2[ficha2_x1][ficha2_y1] == tablero2[ficha2_x2][ficha2_y2]):
                #Si encontro un par entonces, las casillas seleccionadas del tablero_oculto se hacen iguales al tablero2
                tablero_oculto2[ficha2_x1][ficha2_y1] = tablero2[ficha2_x1][ficha2_y1]
                tablero_oculto2[ficha2_x2][ficha2_y2] = tablero2[ficha2_x2][ficha2_y2]
                print("")
                print("Encontro un Par! \n")
                mostrar_tablero(tablero_oculto2,tam_tablero)
           
            else:
                #Si las fichas tienen diferente simbolo entonces, se muestran las fichas elegidas y luego se vuelven a voltear
                print("")
                print("No son pares \n")
                tablero_oculto2[ficha2_x1][ficha2_y1] = tablero2[ficha2_x1][ficha2_y1]
                tablero_oculto2[ficha2_x2][ficha2_y2] = tablero2[ficha2_x2][ficha2_y2]
                mostrar_tablero(tablero_oculto2,tam_tablero)
        
                print("Volteo las fichas \n")
                tablero_oculto2[ficha2_x1][ficha2_y1] ='0'
                tablero_oculto2[ficha2_x2][ficha2_y2] ='0'


            #-------------------- Para jugar las cartas al final del turno ----------------------------#
                #se hace el sorteo si obtengo una carta
                carta_seleccionada2 = carta_por_sorteo(prob_replay, prob_layout, prob_toti, prob_fatality)
                #guarda un str en una lista equivalente a la carta sorteada 
                mazo_jugador2.append(carta_seleccionada2)
                print(f"Mazo de jugador(2) - {jugador2}: {mazo_jugador2}\n")

                #para jugar una carta si esta es sorteada
                jugar_carta0 = jugar_carta(mazo_jugador2, tablero1)
                if jugar_carta0 == None:
                    tablero1 = tablero1
                else:
                    tablero1 = jugar_carta0

            #--------------------------- Caso de carta replay -----------------------------------#
                if "replay" in mazo_jugador2:
                    #en caso de que tenga guardada en el mazo del jugador2 una CARTA REPLAY
                    print("Tenes guardada una carta replay, queres usarla? si/no")
                    opcion2 = input("=> ")
                    if opcion2.lower() == "si":
                        mazo_jugador2.remove("replay")
                        turno_jugador = 2
                    else:
                        print("queda guardada para un siguiente turno")
                        turno_jugador = 1         
                else:
                    #cambio de jugador, si no esta replay en mazo
                    turno_jugador = 1

            #------------------- condicion de corte para que termine el juego  -------------------#
            if (tablero_oculto2 == tablero2):
                #condicion de corte para que termine el juego   
                print(f"Gano el jugador: {jugador2} en un total de {turno} turnos\n")
                mostrar_tablero(tablero_oculto2,tam_tablero)
                terminar_juego = True
                return gano_j2

   #si se llego aca termina el juego

def mezclar_tablero(tablero:list):
    ''' PRE: recibe un tablero

        POST: retorna el tablero mezclado'''

    for i in range(len(tablero)):
        shuffle(tablero[i])
    shuffle(tablero)
    return tablero 

def menu():
    print("Hola! Te gustaria jugar al memotest?\n 1) Si.\n 2) No.")
    x = input("=>")
    while not (x.isnumeric() and int(x) in [1,2]):
        print("Elegi una opcion valida")
        x = input("=>")
    return x

def main()-> None:

    while menu() == "1":
        '''main'''   
        print("¡¡¡ BIENVENIDO AL MEMOTEST !!!\n")  
        
        #nombres de los jugadores
        print("Ingrese el nombre del jugador (1): ")
        jugador1 = nombre_jugador()
        print("Ingrese el nombre del jugador (2): ")
        jugador2 = nombre_jugador()

        #para seleccionar el tablero
        tam_tablero = validar_tamaño()   
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
    else:
        print("Ok. Chau.")

main()