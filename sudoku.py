from typing import Sequence
def creat_sudoku():
    print("\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)
    print("\n")

def empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return  (i,j)
    return (-1,-1)

def check(sudoku,i,j,num):
    valid_row=[]
    valid_colom=[]
    for elm in range(9):
        if sudoku[i][elm]!=num:
            valid_row.append(True)
        else:
            valid_row.append(False)
    if all(valid_row):
        for elm in range(9):
            if sudoku[elm][j]!=num:
                valid_colom.append(True)
            else:
                valid_colom.append(False)    
        if all(valid_colom):
            x=3*(i//3)
            y=3*(j//3)
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if sudoku[i][j] == num:
                        return False
            return True
    return False

def Solve(sudoku,i=0,j=0):
    i, j=empty(sudoku)
    if i == -1:
        return True
    for num in range(1, 10):
        if check(sudoku, i, j, num):
            sudoku[i][j] = num
            if Solve(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False
                    


sudoku =[[8, 1, 0, 0, 3, 0, 0, 2, 7], 
         [0, 6, 2, 0, 5, 0, 0, 9, 0], 
         [0, 7, 0, 0, 0, 0, 0, 0, 0], 
         [0, 9, 0, 6, 0, 0, 1, 0, 0], 
         [1, 0, 0, 0, 2, 0, 0, 0, 4], 
         [0, 0, 8, 0, 0, 5, 0, 7, 0], 
         [0, 0, 0, 0, 0, 0, 0, 8, 0], 
         [0, 2, 0, 0, 1, 0, 7, 5, 0], 
         [3, 8, 0, 0, 7, 0, 0, 4, 2]]
    
Solve(sudoku)
creat_sudoku()
# print(type(empty(sudoku)))
