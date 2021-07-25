
# sudoko= [[0, 0, 0, 0, 1, 0, 5, 0, 0],
# [0, 4, 0, 9, 6, 0, 0, 2, 7],
# [0, 0, 0, 0, 0, 0, 0, 9, 0],
# [0, 0, 0, 0, 0, 0, 7, 0, 0],
# [0, 6, 4, 8, 0, 0, 0, 0, 0],
# [0, 8, 7, 0, 0, 0, 2, 0, 4],
# [0, 0, 0, 0, 4, 0, 0, 0, 3],
# [0, 9, 0, 2, 0, 1, 0, 0, 6],
# [6, 0, 0, 7, 0, 0, 0, 0, 0]]
sudoko = []
for i in range(9):
    arr=[int(x) for x in input().split()]
    sudoko.append(arr)
'Separate with Space: '
def guess(row, col, num):
    for i in range(9):
        if sudoko[row][i] == num:
            return False
    for j in range(9):
        if sudoko[j][col] == num:
            return False
    row0=(row//3)*3
    col0=(col//3)*3
    for m in range(3):
        for n in range(3):
            if sudoko[row0+m][col0+n] == num:
                return False
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if not sudoko[i][j]: 
                for n in range(1,10):
                    if guess(i, j, n):
                        sudoko[i][j] = n
                        solve()
                        sudoko[i][j] = 0
                return

    print(sudoko)
    input('More!')

solve()