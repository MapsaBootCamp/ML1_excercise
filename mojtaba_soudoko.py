import numpy as np

global sample_space
sample_space = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
        print('')


def find_ranked_empty_locations(arr):
    global sample_space
    priority_empties = []
    arr = np.array(arr)
    for row in range(9):
        for col in range(9):
            l = [0, 0, 0, 0]
            if arr[row][col] == 0:
                ban_num_row = np.intersect1d(arr[row], sample_space)
                ban_num_col = np.intersect1d(arr[:, col], sample_space)
                box_arr = arr[3*(row//3):3*(row//3)+3, 3*(col//3):3*(col//3)+3]
                ban_num_box = np.intersect1d(box_arr, sample_space)
                allow_nums = np.setxor1d(np.union1d(np.union1d(ban_num_row, ban_num_col), ban_num_box), sample_space)
                try:
                    probability = 1/len(allow_nums)
                except ZeroDivisionError:
                    probability = 0
                l[0] = row
                l[1] = col
                l[2] = probability
                l[3] = allow_nums
                priority_empties.append(l)
    priority_empties.sort(key=lambda x: -x[2])
    if priority_empties != []:
        return priority_empties[0]
    else:
        return []


def solve_sudoku(arr):
    elem = find_ranked_empty_locations(arr)
    if elem == []:
        return True

    row = elem[0]
    col = elem[1]
    prob = elem[2]
    allow_nums = elem[3]
    if prob == 1:
        arr[row][col] = allow_nums[0]
        if solve_sudoku(arr):
            return True
        else:
            arr[row][col] = 0
            return False
    elif len(allow_nums) == 0:
        return False
    else:
        for num in allow_nums:
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            arr[row][col] = 0
        return False


if __name__ == "__main__":

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists")