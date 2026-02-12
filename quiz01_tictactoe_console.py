import random

a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '

def resetBoard():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    a1 = a2 = a3 = ' '
    b1 = b2 = b3 = ' '
    c1 = c2 = c3 = ' '

def printBoard():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    board = f'  _______\n'\
    f'a |{a1}|{a2}|{a3}|\n'\
    f'b |{b1}|{b2}|{b3}|\n'\
    f'c |{c1}|{c2}|{c3}|\n'\
     '   1 2 3'
    print(board)


def checkWin(player):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    if a1 == a2 == a3 == player: return True
    if b1 == b2 == b3 == player: return True
    if c1 == c2 == c3 == player: return True

    if a1 == b1 == c1 == player: return True
    if a2 == b2 == c2 == player: return True
    if a3 == b3 == c3 == player: return True

    if a1 == b2 == c3 == player: return True
    if a3 == b2 == c1 == player: return True

    return False


def checkDraw():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    spaces = [a1,a2,a3,b1,b2,b3,c1,c2,c3]
    return ' ' not in spaces


def computerMove():
    spots = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
    empty = [s for s in spots if globals()[s] == ' ']
    move = random.choice(empty)
    globals()[move] = 'O'
    print(f"Computer chose {move}")

#____________________"GAME STARTS HERE :D!!!"____________________

print("|                                              |")
print("|______________________________________________|")
print(f'|                                              |'"\n"\
    f'\033[1m'"| WELCOME TO A SIMPLE GAME OF TIC-TAC-TOE! >:3 |"'\033[0m'"\n"\
      f"|        made by yours truly, lori <3!         |")
print("+______________________________________________+")
print()

playAgain = True

while playAgain:
    resetBoard()
    gameWin = False
    currentPlayer = 'X'

    while True:
        mode = input(
            "\nType '1' for Player vs Player Game Mode.\n"
            "Type '2' for Player vs Computer Game Mode.\n\n"
            "Input your Choice: "
        )
        if mode in ['1', '2']:
            break
        else:
            print("\nInvalid input. Please type only '1' or '2' >:(.\n")
            
    while not gameWin:
        printBoard()

        if mode == '2' and currentPlayer == 'O':
            computerMove()
        else:
            move = input(f"Player {currentPlayer}, Please enter a move (choose from 'a1 - c3'): ")

            if move in ['a1','a2','a3','b1','b2','b3','c1','c2','c3']:
                if globals()[move] == ' ':
                    globals()[move] = currentPlayer
                else:
                    print("\nThat spot is taken! >:P")
                    continue
            else:
                print("\nInvalid input.")
                continue

        if checkWin(currentPlayer):
            printBoard()
            if mode == '2' and currentPlayer == 'O':
                print('\n+__________________________________________+\n'
                      '| Computer Wins! Better luck next time! :] |\n'
                      '+__________________________________________+')
            else:
                print(f'\n+____________________________+\n'
                      f"| Player {currentPlayer} Wins, Congrats!!! |\n"
                      f'+____________________________+')
            gameWin = True
        elif checkDraw():
            printBoard()
            print(f'\n+______________________________+\n'
                f"| It's a draw, no one Wins >:[ | \n"
                f'+______________________________+')
            gameWin = True
        else:
            currentPlayer = 'O' if currentPlayer == 'X' else 'X'

    while True:
        again = input("\n>>> Do you want to play again? (y/n): ").lower()
        if again == 'y':
            break 
        elif again == 'n':
            playAgain = False
            print("\nThank you for playing!")
            break
        else:
            print("Please type 'y' or 'n'!!!")

# I genuinely hope this works, or else im gonna be breaking down for the nth time. :D