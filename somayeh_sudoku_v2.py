class sudoku(object):
    def __init__(self,table=None):
        self._sudoku=table

    # getter method
    def get_sudoku(self):
        return self._sudoku

    # setter method
    def set_sudoku(self, table):
        self._sudoku = table

    # A utility method to print
    def printing(self,sudo:list):
        for row in sudo:
            for element in row:
                print(element, end=" ")
            print()

    # solver sudoku
    def solve_sudoku(self):
        index=len(self._sudoku)
        num_arry=[]
        for element in range(index):
            num_arry.append(element + 1)
        for row in range(index):
            for column in range(index):
                temp_arry = []
                if self._sudoku[row][column] == 0:
                    for temp in range(index):
                        if self._sudoku[row][temp] != 0:
                            if self._sudoku[row][temp] not in temp_arry:
                                temp_arry.append(self._sudoku[row][temp])
                        if self._sudoku[temp][column] != 0:
                            if self._sudoku[temp][column] not in temp_arry:
                                temp_arry.append(self._sudoku[temp][column])
                    startRow = row - row % 3
                    startCol = column - column % 3
                    for i in range(3):
                        for j in range(3):
                            if self._sudoku[i + startRow][j + startCol] != 0:
                                if self._sudoku[i + startRow][j + startCol] not in temp_arry:
                                    temp_arry.append(self._sudoku[i + startRow][j + startCol])
                    # print((row, column),temp_arry)
                    for num in num_arry:
                        if num not in temp_arry:
                            self._sudoku[row][column] = num
                            break
        return self._sudoku

sudo=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]

my_sudoku=sudoku()
my_sudoku.set_sudoku(sudo)
sudo_solved=my_sudoku.solve_sudoku()
my_sudoku.printing(sudo_solved)


