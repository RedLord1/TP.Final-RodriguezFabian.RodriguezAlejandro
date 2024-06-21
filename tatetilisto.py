#TA-TE-TI JUGADOR VS JUGADOR versión Correa

def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo = 'X'
    else:
        simbolo = 'O'
    
    if posicion == 1:
        if tablero [0] == ' ':
            tablero[0] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 2:
        if tablero [1] == ' ':
            tablero[1] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 3:
        if tablero [2] == ' ':
            tablero[2] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 4:
        if tablero [3] == ' ':
            tablero[3] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 5:
        if tablero [4] == ' ':
            tablero[4] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 6:
        if tablero [5] == ' ':
            tablero[5] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 7:
        if tablero [6] == ' ':
            tablero[6] = simbolo
            return 0 
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 8:
        if tablero [7] == ' ':
            tablero[7] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'
    if posicion == 9:
        if tablero [8] == ' ':
            tablero[8] = simbolo
            return 0
        else:
            return 'Esa posición ya está ocupada'


def verificar_victoria(tablero):
    for simbolo in ['X', 'O']:
            #combinaciones_ganadoras = [
                #[0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
                #[0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
                #[0, 4, 8], [2, 4, 6]              # diagonales
            #]
            

        fila_0 = tablero [0] == simbolo and tablero [1] == simbolo and tablero [2] == simbolo
        fila_1 = tablero [3] == simbolo and tablero [4] == simbolo and tablero [5] == simbolo
        fila_2 = tablero [6] == simbolo and tablero [7] == simbolo and tablero [8] == simbolo
        columna_0 = tablero [0] == simbolo and tablero [3] == simbolo and tablero [6] == simbolo
        columna_1 = tablero [1] == simbolo and tablero [4] == simbolo and tablero [7] == simbolo
        columna_2 = tablero [2] == simbolo and tablero [5] == simbolo and tablero [8] == simbolo
        diagonal_abajo = tablero [0] == simbolo and tablero [4] == simbolo and tablero [8] == simbolo
        diagonal_arriba = tablero [2] == simbolo and tablero [4] == simbolo and tablero [6] == simbolo

        if fila_0 or fila_1 or fila_2 or columna_0 or columna_1 or columna_2 or diagonal_abajo or diagonal_arriba:
          
            if simbolo == 'X':
                return 1
            elif simbolo == 'O':
                return 2
            break

tablero = [' '] * 9
def imprimir_tablero(tablero):
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ") #1 FILA
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ") #2
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ") #3
    #COLUMNA       0           1               2 



turno_1 = True
#jugador1 = 'x'
#jugador2 = 'o'
turno = 0
imprimir_tablero(tablero)
while turno < 9:
    if turno_1:
        print("Turno del jugador 1 (1-9): ")
    else:
        print("Turno del jugador 2 (1-9): ")
    
    jugada = int(input())

    valor = cambiar_tablero(tablero, jugada, turno_1)
    if valor == 0:
        turno_1 = not turno_1
        turno += 1
        imprimir_tablero(tablero)

        if verificar_victoria(tablero) == 1:
            print("El jugador 1 es el ganador")
            break
            
        elif verificar_victoria(tablero,) == 2:
            print("El jugador 2 es el ganador")
            break

    else:
        print(valor)
        
    if turno == 9:
        print("Empate")
        break    