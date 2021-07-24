import time
board = [
        [3, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 2, 5, 0],
        [5, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 7, 9],
        [0, 0, 0, 0, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 7, 0, 0, 4, 5],
        [0, 0, 1, 3, 0, 0, 0, 0, 6]
    ]


def solve(given_board):
    find_valid = find_empty(given_board)

    if not find_valid:
        return True
    else:
        row, column = find_valid

    for i in range(1, 10):
        if find_valid_number(given_board, i, (row, column)):
            given_board[row][column] = i

            if solve(given_board):
                return True

        given_board[row][column] = 0

    return False


def find_valid_number(given_board, number, position):
    # check row
    for i in range(len(given_board)):
        if given_board[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(given_board)):
        if given_board[i][position[1]] == number and position[0] != i:
            return False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if given_board[i][j] == number and (i, j) != position:
                return False

    return True


def print_board(given_board: list[list]):
    for i in range(len(given_board)):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(given_board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(given_board[i][j])
            else:
                print(str(given_board[i][j]) + " ", end="")


def find_empty(given_board: list[list]):
    for i in range(len(given_board)):
        for j in range(len(given_board[0])):
            if given_board[i][j] == 0:
                return i, j

    return None


print("Not solved Sudoku Table: ")
print_board(board)
print()
print()
print("solved sudoku table:")
start_time = time.time()
solve(board)
print("--- %s seconds ---" % (time.time() - start_time))
print_board(board)
