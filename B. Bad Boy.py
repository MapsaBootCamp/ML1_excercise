def find_furthest_point(row, column, d, k):
    global i
    global j
    point = [d, k]

    if (row - d) >= d:
        point[0] += (row - d)
    else:
        point[0] -= d - 1
    if (m - k) >= k:
        point[1] += (column - k)
    else:
        point[1] -= k - 1

    i, j = point[0], point[1]
    result.extend(point)


test_num = int(input())
result = []

for number_of_test in range(test_num):
    [n, m, i, j] = input().split()
    n = int(n)
    m = int(m)
    i = int(i)
    j = int(j)

    find_furthest_point(n, m, i, j)
    find_furthest_point(n, m, i, j)

for elem_print in result:
    print(elem_print, end=" ")
