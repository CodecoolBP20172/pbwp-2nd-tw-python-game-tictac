import sys
from random import randint

def del_win():
    print("\033c")


def print_board (Matrix):
    del_win()
    for i in range (0, len (Matrix[0])):
        for element in Matrix[i]:
            sys.stdout.write("[{}]".format(*element))
        print("")


def player_change():
    global player
    global ch
    if player == 1:
        player = 2
        ch = "O"
    else:
        player = 1
        ch = "X"


def empty_steps (choice):
    global Matrix
    if choice ==1: 
        if Matrix[2][0] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==2:
        if Matrix[2][1] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==3:
        if Matrix[2][2] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==4:
        if Matrix[1][0] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==5:
        if Matrix[1][1] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==6:
        if Matrix[1][2] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==7:
        if Matrix[0][0] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==8:
        if Matrix[0][1] != " ":
            print("The location you chose is not empty!!!")
            return True
    elif choice ==9:
        if Matrix[0][2] != " ":
            print("The location you chose is not empty!!!")
            return True
def empty_stepsAuto (choice):
    global Matrix
    if choice == 1: 
        if Matrix[2][0] != " ":
            return True
    elif choice ==2:
        if Matrix[2][1] != " ":
            return True
    elif choice ==3:
        if Matrix[2][2] != " ":
            return True
    elif choice ==4:
        if Matrix[1][0] != " ":
            return True
    elif choice ==5:
        if Matrix[1][1] != " ":
            return True
    elif choice ==6:
        if Matrix[1][2] != " ":
            return True
    elif choice ==7:
        if Matrix[0][0] != " ":
            return True
    elif choice ==8:
        if Matrix[0][1] != " ":
            return True
    elif choice ==9:
        if Matrix[0][2] != " ":
            return True

def check_step (choice):
    if choice ==1: 
        Matrix[2][0] = ch 
        print_board(Matrix)
        
    elif choice ==2:
        Matrix[2][1] = ch
        print_board(Matrix)

    elif choice ==3:
        Matrix[2][2] = ch
        print_board(Matrix)

    elif choice ==4:
        Matrix[1][0] = ch
        print_board(Matrix)

    elif choice ==5:
        Matrix[1][1] = ch
        print_board(Matrix)

    elif choice ==6:
        Matrix[1][2] = ch
        print_board(Matrix)

    elif choice ==7:
        Matrix[0][0] = ch
        print_board(Matrix)

    elif choice ==8:
        Matrix[0][1] = ch
        print_board(Matrix)

    elif choice ==9:
        Matrix[0][2] = ch
        print_board(Matrix)


def check_hits(Matrix):
    winner = False
    gameIsOngoing = True
    for i in range (0, len (Matrix[0])):
        if Matrix [i][0] == ch and Matrix [i][1] ==ch and Matrix [i][2] == ch:
            print (player, end="")
            print(". player wins!\n")
            winner = True
            gameIsOngoing = False

    for i in range (0, len (Matrix[0])):
        if Matrix [0][i] == ch and Matrix [1][i] == ch and Matrix [2][i] == ch:
            print (player, end="")
            print(". player wins!\n")
            winner = True
            gameIsOngoing = False

    if Matrix [0][0] ==ch and Matrix [1][1] == ch and Matrix [2][2] == ch:
            print (player, end="")
            print(". player wins!\n")
            winner = True
            gameIsOngoing = False

    if Matrix [0][2] == ch and Matrix [2][0] == ch and Matrix [1][1] == ch:
            print (player, end="")
            print(". player wins!\n")
            winner = True
            gameIsOngoing = False
    if winner == False:
        gameIsOngoing = table_check(Matrix)
    return gameIsOngoing
def check_hits_comp(Matrix):
    winner = False
    gameIsOngoing = True
    for i in range (0, len (Matrix[0])):
        if Matrix [i][0] == ch and Matrix [i][1] ==ch and Matrix [i][2] == ch:
            print("\n This really blonde computer could beat you :D\n")
            winner = True
            gameIsOngoing = False

    for i in range (0, len (Matrix[0])):
        if Matrix [0][i] == ch and Matrix [1][i] == ch and Matrix [2][i] == ch:
            print("\n This really blonde computer could beat you :D\n")
            winner = True
            gameIsOngoing = False

    if Matrix [0][0] ==ch and Matrix [1][1] == ch and Matrix [2][2] == ch:
            print("\n This really blonde computer could beat you :D\n")
            winner = True
            gameIsOngoing = False

    if Matrix [0][2] == ch and Matrix [2][0] == ch and Matrix [1][1] == ch:
            print("\n This really blonde computer could beat you :D\n")
            winner = True
            gameIsOngoing = False
    if winner == False:
        gameIsOngoing = table_check(Matrix)
    return gameIsOngoing

def table_check(Matrix):
    spaceHasFound = 0
    for i in range (0, len (Matrix[0])):
        for j in range(0,len(Matrix[i])):
            if Matrix[i][j]== " ":
                spaceHasFound = spaceHasFound+1
    gameIsOngoing = True
    if spaceHasFound == 0:
        gameIsOngoing = False
        print("Draw!")
    return gameIsOngoing

def gameAuto():
    global Matrix
    global ch
    global player
    global target
    signs = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    row = 3
    Matrix = [[" " for x in range(row)] for y in range(row)]
    print_board(Matrix)
    gameIsOngoing = True
    gameIsOngoing2 = True
    draw = False
    while gameIsOngoing and gameIsOngoing2:
        player = 2
        ch = 'C'
        AutoGenNum = True
        while AutoGenNum:
            target = (randint(1, 9))
            AutoGenNum = empty_stepsAuto(target)
        check_step(target)
        gameIsOngoing2 = check_hits_comp(Matrix)
        player = 1
        ch = 'X'
        myChar = gameIsOngoing2
        while myChar:
            try:
                choice= int(input("Add a number to put your character: "))
            except (ValueError, UnboundLocalError):
                q = input("Use the numerical part of your keypad (1-9) or press q if you want to quit")
                if q == 'q':
                    sys.exit()
                else:
                    continue
            if choice in signs:
                myChar = False
                myChar = empty_steps(choice) 
            else:
                print("Oops, undetectible character.")
        if gameIsOngoing2 == True:
            check_step(choice)
            gameIsOngoing = check_hits(Matrix)

def game():
    global Matrix
    global ch
    global player
    signs = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    player = 1
    ch = 'X'
    row = 3
    Matrix = [[" " for x in range(row)] for y in range(row)]
    print_board(Matrix)
    gameIsOngoing = True
    while gameIsOngoing: #True:
        myChar = True
        while myChar:
            try:
                choice= int(input("Add a number to put your character: "))
            except (ValueError, UnboundLocalError):
                q = input("Use the numerical part of your keypad (1-9) or press q if you want to quit")
                if q == 'q':
                    sys.exit()
                else:
                    continue
            if choice in signs:
                myChar = False
                myChar = empty_steps(choice) 
            else:
                print("Oops, undetectible character.")

        check_step(choice)
        gameIsOngoing = check_hits(Matrix)
        player_change()

ansYes = { 'y', 'Yes', 'Y', 'yes'}
ansNo = { 'n', 'No', 'N', 'no'}
ansAuto = { 'a', 'A', 'auto', 'Auto'}

del_win()
print("Hello User! This is a simple tic tac toe game. \n\nYou can play alone or in pair. \n\nThe first player play with the character X and the second one with O.\n")
answer = True
while answer:
    cho = input("Would you like to play a round? \n    -press a or A or type auto / Auto to play against the computer \n    -press y or Y / type yes or Yes to play\n    -press n or N / type no or No to close the program\n ")
    if cho in ansYes:
        game()
    elif cho in ansNo:
        sys.exit()
    elif cho in ansAuto:
        gameAuto()
    else:
        print("Oops, what???.")

#TODO:
#kezelni ctrl+C kilépést