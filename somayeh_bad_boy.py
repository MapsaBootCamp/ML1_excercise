# Bad Boy
# 1537B
# codeforces.com
def yoyo1(n, m, i, j, cost:list):
    if i<n and j<m:
        if i + 1<n:
            cost[i + 1][j] = min (cost[i][j]+ 1, cost[i+1][j])
            yoyo1(n, m, i + 1, j, cost)
        if j+1<m:
            cost[i][j+1] = min (cost[i][j]+ 1, cost[i][j+1])
            yoyo1(n, m, i, j + 1, cost)
    return cost

def yoyo2(n, m, i, j, cost:list):
    if i<n and j>=0:
        if i + 1<n:
            cost[i + 1][j] = min (cost[i][j]+ 1, cost[i+1][j])
            yoyo2(n, m, i + 1, j, cost)
        if j-1>=0:
            cost[i][j-1] = min (cost[i][j]+ 1, cost[i][j-1])
            yoyo2(n, m, i, j - 1, cost)
    return cost

def yoyo3(n, m, i, j, cost:list):
    if i>=0 and j>=0:
        if i - 1>=0:
            cost[i - 1][j] = min (cost[i][j]+ 1, cost[i-1][j])
            yoyo3(n, m, i - 1, j, cost)
        if j-1>=0:
            cost[i][j-1] = min (cost[i][j]+ 1, cost[i][j-1])
            yoyo3(n, m, i, j - 1, cost)
    return cost
def yoyo4(n, m, i, j, cost:list):
    if i>=0 and j<m:
        if i - 1>=0:
            cost[i - 1][j] = min (cost[i][j]+ 1, cost[i-1][j])
            yoyo4(n, m, i - 1, j, cost)
        if j+1<m:
            cost[i][j+1] = min (cost[i][j]+ 1, cost[i][j+1])
            yoyo4(n, m, i, j + 1, cost)
    return cost

testcase=input("The number of test cases:")
for item in range(int(testcase)):
    n , m =input('The dimensions of the room (n and m):').split(' ')
    n=int(n)
    m=int(m)
    i, j = input('The cell at which Anton is currently standing (i and j):').split(' ')
    i=int(i)
    j=int(j)
    cost = []
    for row in range(n):
        room = []
        for column in range(m):
            room.append(n * m + 1)
        cost.append(room)
    i -= 1
    j -= 1
    cost[i][j] = 0
    cost = yoyo1(n, m, i, j, cost)
    cost = yoyo2(n, m, i, j, cost)
    cost = yoyo3(n, m, i, j, cost)
    cost = yoyo4(n, m, i, j, cost)
    print(cost)
    max1, max2 = 0, 0
    option1 = []
    temp = cost
    for i in range(n):
        for j in range(m):
            if cost[i][j] > max1:
                max1 = cost[i][j]
    for i in range(n):
        for j in range(m):
            if cost[i][j] == max1:
                option1.append((i + 1, j + 1))
    option2 = []
    for element in option1:
        temp[element[0] - 1][element[1] - 1] = -1
        for i in range(n):
            for j in range(m):
                if temp[i][j] > max2:
                    max2 = cost[i][j]
        for i in range(n):
            for j in range(m):
                if cost[i][j] == max2:
                    option2.append((i + 1, j + 1))
    result = []
    for element1 in option1:
        for element2 in option2:
            result.append([element1, element2])
    print(result)