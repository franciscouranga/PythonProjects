# Funcion para el uso interno del tablero. Devuelve X, O, ""
def out(numero):
    if numero == 0:
        return " "
    elif numero == 1:
        return "X"
    elif numero == 2:
        return "O"
    else:
        return "-"

# Funcion para imprimir el tablero. Le entra posiciones una list de largo 9 con valores 0, 1 y 2
def printBoard(pos):

    '''
        |   |
      X | X |
    ____|___|____
        |   |
        |   |
    ____|___|____
        |   |
        |   |
        |   |
    '''
    if len(pos) != 9:
        print("Error length")
        return
    for i in range(3):
        print("    |   |")
        print(" ", out(pos[0+i*3]), "|", out(pos[1+i*3]), "|", out(pos[2+i*3]))
        if i < 2:
            print("____|___|____")
        else:
            print("    |   |")

# Funcion para ver si un lugar esta en blanco. Le entra un numero
def spaceIsFree(pos):
    return posiciones[pos] == 0

# Funcion para ver si el tablero esta lleno
def isBoardFull(posiciones):
    if posiciones.count(0) > 0:
        return False
    else:
        return True
    '''
    for i in posiciones:
        if i == 0:
            return False
    '''

# Funcion que revisa si hay un ganador (b es posiciones)
def checkWinner(b):
    if len(b) != 9:
        return print("Error")
    if b[0] == b[4] and b[4] == b[8] and b[0] != 0:
        return b[0]
    elif b[2] == b[4] and b[4] == b[6] and b[2] != 0:
        return b[2]
    else:
        for i in range(3):
            if b[0+3*i] == b[1+3*i] and b[0+3*i] == b[2+3*i] and b[0+3*i] != 0:
                return b[0+3*i]
            elif b[0+i] == b[3+i] and b[0+i] == b[6+i] and b[0+i] != 0:
                return b[0+i]
        return False

# Funcion para obtener el input del usuario y updatear posiciones. Le entra posiciones para updatearla
def userInput(posiciones):
    while True:
        try:
            x = int(input("Select a space!\n 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9 :  "))
            if x in range(1,10):
                x = x-1
                if spaceIsFree(x) == True:
                    posiciones[x] = 1
                    break
                else:
                    print("Space is already occupied.")
            else:
                print("Please enter number from 1 to 9.")
        except ValueError:
            print("That is not a valid number.")

# Funcion que procesa la respuesta del AI
def computerMove(posiciones, dif):
    availablePlaces = [x for x in range(9) if posiciones[x] == 0]
    move = 0

    # Marca la primer opción si hay alguno por ganar, ya sea la PC o el jugador
    for pc in [2, 1]:
        for i in availablePlaces:
            poscopia = posiciones[:]
            poscopia[i] = pc
            if checkWinner(poscopia) != False:
                move = i
                return move

    # Miro que dificultad puso el usuario
    if dif == "P":
        # Funcion interna para buscar en las esquinas
        availableCorners = [x for x in availablePlaces if x in [0, 2, 6, 8]]
        if availableCorners != []:
            move = randomCorner(availableCorners)
            return move

        # Funcion interna para buscar en el centro
        if 4 in availablePlaces:
            move = 4
            return move

        # Funcion interna para buscar en los bordes
        availableEdges = [x for x in availablePlaces if x in [1, 3, 5, 7]]
        move = randomCorner(availableEdges)
        return move
    elif dif == "R":
        availableSpots1 = [x for x in availablePlaces if x in [0, 1, 2, 3, 6]]
        if availableSpots1 != []:
            move = randomCorner(availableSpots1)
            return move

        availableSpots2 = [x for x in availablePlaces if x in [4, 5, 7, 8]]
        if availableSpots2 != []:
            move = randomCorner(availableSpots2)
            return move
    elif dif == "E":
        availableSpots = [x for x in availablePlaces]
        if availableSpots != []:
            move = randomCorner(availableSpots)
            return move
    else:
        print("Error in user input")

# Funcion que randomiza las esquinas y los bordes (para funcionamiento de computerMove)
def randomCorner(available):
    import random
    ln = len(available)-1
    return available[random.randint(0,ln)]

# Funcion que establece el tipo de dificultad
def difficulty():
    while True:
        print("Select level of difficulty.")
        x = str(input("Press E for easy, R for regular and P for Pro: ")).upper()
        if x not in ["E", "R" , "P"]:
            print("Invalid entry.")
        else:
            return x

# Asks if user wants to play again
def playAgain():
    while True:
        x = str(input("Do you want to play again? (Y/N) ")).upper()
        if x in ['Y', 'YES']:
            return "Y"
        elif x in ['N', 'NO']:
            return "N"
        else:
            print("Invalid input")

# Initial message
def initialMessage():
    # Crea lista de posiciones en blanco
    posiciones = [0 for i in range(9)]

    # First message to user
    print("Welcome to  tic tac toe!")
    print('You will be playing against the computer')
    dificultad = difficulty()
    if choosePlayer() == "N":
        posiciones[computerMove(posiciones, dificultad)] = 2
    return dificultad, posiciones

# Choose Player
def choosePlayer():
    while True:
        x = str(input("Do you want to go first?: (Y/N) ")).upper()
        if x in ['Y', 'YES']:
            return "Y"
        elif x in ['N', 'NO']:
            return "N"
        else:
            print("Invalid input")

# PROGRAM
dificultad, posiciones = initialMessage()
while True:
    printBoard(posiciones)
    userInput(posiciones)
    if isBoardFull(posiciones) == True:
        printBoard(posiciones)
        print("There is no winner!")
        if playAgain() == "Y":
            dificultad, posiciones = initialMessage()
        else:
            break
    move = computerMove(posiciones, dificultad)
    posiciones[move] = 2
    print('\n\n')
    if checkWinner(posiciones) != False:
        printBoard(posiciones)
        print("The winner is Player ",checkWinner(posiciones))
        if playAgain() == "Y":
            dificultad, posiciones = initialMessage()
        else:
            break
    if isBoardFull(posiciones) == True:
        printBoard(posiciones)
        print("There is no winner!")
        if playAgain() == "Y":
            dificultad, posiciones = initialMessage()
        else:
            break


#REVISAR ERROR EN DIFICULTAD R CUANDO EL USUARIO VA SEGUNDO QUE APARECIERON DOS CIRCULOS EN DOS CASILLEROS
#CAMBIAR PLAYER 1 A X | O
