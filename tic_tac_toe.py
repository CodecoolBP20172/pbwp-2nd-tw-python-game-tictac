import sys
from random import randint


def del_win():
    print("\033c")


def name_inputs():
    name1 = name('first')
    name_not_ok = True
    while name_not_ok:
        name2 = name('second')
        if name1 != name2:
            name_not_ok = False
        else:
            print("Names have to be different!")
    return name1, name2


def table_gen():
    row_grater = True
    while row_grater:
        row = read_num("Please add the size of the table (3-30): ")
        if row < 30 and row > 2:
            row_grater = False
    Matrix = [[" " for x in range(row)] for y in range(row)]
    print_board(Matrix)
    return Matrix, row


def comp_steps(Matrix, ch, player, row):
    AutoGenNum = True
    while AutoGenNum:
        target = []
        target.append(randint(1, row-1))
        target.append(randint(1, row-1))
        AutoGenNum = empty_steps(target, Matrix, "")
    check_step(target, Matrix, ch)
    print_board(Matrix)
    gameIsOngoing2 = check_hits(Matrix, target, ch, player)
    return gameIsOngoing2, target


def write_label(leng):
    print("   ", end="")
    for i in range(leng):
        if i > 7:
            print(" " + str(i+1), end="")
        else:
            print(" " + str(i+1), end=" ")
    print('')


def print_board(Matrix):
    del_win()
    write_label(len(Matrix[0]))
    for i in range(0, len(Matrix[0])):
        if i > 8:
            print(" " + str(i+1), end="")
        else:
            print(" " + str(i+1), end=" ")
        for element in Matrix[i]:
            sys.stdout.write("[{}]".format(*element))
        print(i+1)
    write_label(len(Matrix[0]))


def name(who):
    name = input('Type the name of the {0} player: '.format(who))
    return name


def read_num(question):
    cycle_bool = True
    while cycle_bool:
        try:
            number = int(input(question))
        except (ValueError, UnboundLocalError):
            print("Please give numbers!")
            continue
        cycle_bool = False
    return number


def read_coords(player, Matrix, ch):
    my_bool = True
    while my_bool:
        coords = []
        coords.append(read_num(player + ', add the coordinate \n x: ')-1)
        coords.append(read_num(' y: ')-1)
        try:
            if not empty_steps(coords, Matrix, "The location you chose is not empty!!!"):
                check_step(coords, Matrix, ch)
            else:
                continue
        except:
            print('Given coordinates are wrong. Try again')
            continue
        my_bool = False
    print_board(Matrix)
    return coords


def player_change(name1, name2, player, ch):
    if player == name1:
        player = name2
        ch = "O"
    else:
        player = name1
        ch = "X"
    return player, ch


def empty_steps(choice, Matrix, message):
    if Matrix[choice[0]][choice[1]] != " ":
        print(message)
        return True


def check_step(choice, Matrix, ch):
    Matrix[choice[0]][choice[1]] = ch


def compare(Ma, a, b, c, d, ch, player):
    if a < 0 or b < 0 or c < 0 or d < 0:
        return False
    try:
        if Ma[a][b] == ch and Ma[c][d] == ch:
            print(player, end="")
            print(" wins!\n")
            return True
    except IndexError:
        return False
    return False


def check_hits(Ma, ind, ch, player):
    x = ind[0]
    y = ind[1]
    tab = [[x, y+1, x, y-1], [x, y+1, x, y+2], [x, y-1, x, y-2],
           [x+1, y, x-1, y], [x+1, y, x+2, y], [x-1, y, x-2, y],
           [x-1, y-1, x+1, y+1], [x-1, y-1, x-2, y-2], [x+1, y+1, x+2, y+2],
           [x-1, y+1, x+1, y-1], [x-1, y+1, x-2, y+2], [x+1, y-1, x+2, y-2]]
    winner = False
    for row in tab:
        if not winner:
            winner = compare(Ma, row[0], row[1], row[2], row[3], ch, player)
    if winner:
        return False
    else:
        return table_check(Ma)


def table_check(Matrix):
    spaceHasFound = 0
    for i in range(0, len(Matrix[0])):
        for j in range(0, len(Matrix[i])):
            if Matrix[i][j] == " ":
                spaceHasFound = spaceHasFound+1
    gameIsOngoing = True
    if spaceHasFound == 0:
        gameIsOngoing = False
        print("Draw!")
    return gameIsOngoing


def gameAuto():
    name1 = name('first')
    name2 = 'Computer'
    Matrix, row = table_gen()
    gameIsOngoing = True
    gameIsOngoing2 = True
    draw = False
    while gameIsOngoing and gameIsOngoing2:
        player = name2
        ch = 'C'
        gameIsOngoing2, target = comp_steps(Matrix, ch, player, row)
        player = name1
        ch = 'X'
        if gameIsOngoing2:
            coords = read_coords(player, Matrix, ch)
            gameIsOngoing = check_hits(Matrix, coords, ch, player)


def game():
    name1, name2 = name_inputs()
    player = name1
    ch = 'X'
    Matrix, row = table_gen()
    gameIsOngoing = True
    while gameIsOngoing:
        coords = read_coords(player, Matrix, ch)
        gameIsOngoing = check_hits(Matrix, coords, ch, player)
        player, ch = player_change(name1, name2, player, ch)


def main():
    try:
        ansYes = {'y', 'Yes', 'Y', 'yes'}
        ansNo = {'n', 'No', 'N', 'no'}
        ansAuto = {'a', 'A', 'auto', 'Auto'}
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
    except KeyboardInterrupt:
        print("\nYou stopped the program with entering Ctrl+C. Bye!")

if __name__ == '__main__':
    main()

