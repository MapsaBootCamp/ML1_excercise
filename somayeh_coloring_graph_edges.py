# Blue and Red of Our Faculty!
# 1425B
# codeforces.com
import copy
# compute adjacency matrix for given graph
def adjacency_matrix(node_num,edges):
    start = []
    start_node = 1
    matrix = list()
    for row in range(node_num):
        row_arry = []
        for column in range(node_num):
            row_arry.append(0)
        matrix.append(row_arry)
    for node in range(node_num):
        for edge in edges:
            if node + 1 == edge[0]:
                matrix[node][edge[1] - 1] += 1
                if node + 1 == start_node:
                    start.append(edge[1])
            if node + 1 == edge[1]:
                matrix[node][edge[0] - 1] += 1
                if node + 1 == start_node:
                    start.append(edge[0])
            else:
                continue
    return matrix,start

# find all options for starting
def get_permutation(start):
    permutation_1 = []
    for count in range(len(start)):
        for i in range(count + 1, len(start)):
            permutation_1.append((start[count], start[i]))
    permutation = set(permutation_1)
    return permutation

# find path based on selected nodes
def find_path(start_node_b, start_node_r,matrix,element):
    color = "Blue"
    BULE = +10
    RED = -10
    blue = []
    red = []
    temp = copy.deepcopy(matrix)
    if color == "Blue":
        blue.append(start_node_b)
        temp[start_node_b - 1][element[0] - 1] = BULE
        temp[element[0] - 1][start_node_b - 1] -= 1
        color = "Red"
        start_node_b = element[0] - 1
        blue.append(start_node_b + 1)
    if color == "Red":
        red.append(start_node_r)
        temp[start_node_r - 1][element[1] - 1] = RED
        temp[element[1] - 1][start_node_r - 1] -= 1
        color = "Blue"
        start_node_r = element[1] - 1
        red.append(start_node_r + 1)
    while True:
        column = 0
        if color == "Blue":
            for item in temp[start_node_b]:
                if item == 1:
                    temp[start_node_b][column] = BULE
                    temp[column][start_node_b] -= 1
                    start_node_b = column
                    blue.append(start_node_b + 1)
                    color = "Red"
                    break
                else:
                    column += 1
            else:
                break
        column = 0
        if color == "Red":
            for item in temp[start_node_r]:
                if item == 1:
                    temp[start_node_r][column] = RED
                    temp[column][start_node_r] -= 1
                    start_node_r = column
                    red.append(start_node_r + 1)
                    color = "Blue"
                    break
                else:
                    column += 1
            else:
                break
    del temp
    return blue,red

# print result
def printing(result):
    print("--------------- Result --------------")
    for elm in result:
        print(elm, end="\n")
    print("-------------------------------------")

def main():
    node_num = int(input("nodes(N):"))
    edge_num = int(input("edges(M):"))
    print('****** Edges ******')
    edges = []
    for edge in range(edge_num):
        i, j = input().split()
        edges.append((int(i), int(j)))
    print('*******************')
    matrix, start = adjacency_matrix(node_num, edges)
    print("Adjacency Matrix:",matrix)
    permutation = get_permutation(start)

    result = [[['Blue'], ['Red']]]
    for element in permutation:
        start_node_b, start_node_r = 1, 1
        blue, red = find_path(start_node_b, start_node_r, matrix,element)
        result.append([blue, red])
        result.append([red, blue])
    # print(result)
    printing(result)
if __name__ == "__main__":
    main()