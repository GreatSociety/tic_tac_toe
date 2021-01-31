
def field_print(massive):

    print(f"---------\n"
          f"| {massive[0][0]} {massive[0][1]} {massive[0][2]} |\n"
          f"| {massive[1][0]} {massive[1][1]} {massive[1][2]} |\n"
          f"| {massive[2][0]} {massive[2][1]} {massive[2][2]} |\n"
          f"---------")


def massive_checker(list_of_two, massive):
    if massive[list_of_two[0]-1][list_of_two[1]-1] == 'X' or massive[list_of_two[0]-1][list_of_two[1]-1] == 'O':
        print("This cell is occupied!")
        return False
    else:
        return True


def input_checker():

    flag = True

    while flag:

        coordinates = input().replace(',', ' ')

        coordinates = [int(coord) for coord in coordinates.split() if coord.isdigit()]

        if len(coordinates) < 2:
            print("You should enter numbers!")
            continue
        elif len(coordinates) > 2:
            print("You should enter two numbers!")
            continue
        elif (coordinates[0] > 3) or (coordinates[0] < 1) or (coordinates[1] > 3) or (coordinates[1] < 1):
            print("Coordinates should be from 1 to 3!")
            continue
        elif not massive_checker(coordinates, tic_toe):
            continue
        else:
            flag = False

    return coordinates


def winner_checker(char_n, num_mas, massive):
    row = True
    colm = True
    diag = False

    for ind in range(3):
        if massive[num_mas[0]-1][ind] != char_n:
            row = False

        if massive[ind][num_mas[1]-1] != char_n:
            colm = False

    if massive[1][1] == char_n:

        if sum(num_mas)-2 != 2:
            for ind in range(0, 3, 2):
                if massive[ind][ind] != char_n:
                    break
            else:
                diag = True
        else:
            if massive[0][2] == char_n and massive[2][0] == char_n:
                diag = True

    if row or colm or diag:
        return True
    else:
        return False


answer = 1
while answer:
    tic_toe = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    field_print(tic_toe)

    for num in range(9):

        char = 0

        if num % 2 == 0:
            char = 'X'
        else:
            char = 'O'

        print(f"Now is {char} turn:")
        coord_num = input_checker()

        tic_toe[coord_num[0] - 1][coord_num[1] - 1] = char

        if num > 3:
            if winner_checker(char, coord_num, tic_toe):
                field_print(tic_toe)
                print(f"{char} wins")
                break
            else:
                if num == 8:
                    field_print(tic_toe)
                    print('Draw')
                else:
                    field_print(tic_toe)
        else:
            field_print(tic_toe)

    quest_answer = input("You wanna new game? If not write a zero:")

    if "no" in quest_answer:
        answer = 0
    else:
        answer = 1
