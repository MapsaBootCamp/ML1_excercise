class sudoku(object):
    def __init__(self,table=None):
        self._sudoku=table

    # getter method
    def get_sudoku(self):
        return self._sudoku

    # setter method
    def set_sudoku(self, table):
        self._sudoku = table

    def printing(self):
        for i in range(len(self._sudoku)):
            for j in range(len(self._sudoku)):
                print(self._sudoku[i][j], end=" ")
            print()

    def isSafe(self, row, column, num):

        for x in range(len(self._sudoku)):
            if self._sudoku[row][x] == num:
                return False

        for x in range(len(self._sudoku)):
            if self._sudoku[x][column] == num:
                return False

        startRow = row - row % 3
        startCol = column - column % 3
        for i in range(3):
            for j in range(3):
                if self._sudoku[i + startRow][j + startCol] == num:
                    return False
        return True

    def solve_sudoku(self, row, column):
        dimension = len(self._sudoku)
        if (row == dimension - 1 and column == dimension):
            return True

        if column == dimension:
            row += 1
            column = 0

        if sudo[row][column] > 0:
            return self.solve_sudoku(row, column + 1)

        for num in range(1, dimension + 1, 1):
            if self.isSafe(row, column, num):
                self._sudoku[row][column] = num
                if self.solve_sudoku(row, column + 1):
                    return sudo
            self._sudoku[row][column] = 0


sudo = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

my_sudoku=sudoku()
my_sudoku.set_sudoku(sudo)
sudo_solved=my_sudoku.solve_sudoku(0,0)
my_sudoku.printing()