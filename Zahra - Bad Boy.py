t = int(input())
input_list = []

while t > 0:
    n, m, i, j = [int(x) for x in input().split()]
    input_list.append([n, m, i, j])
    t -= 1


def max_distance(length, sit):  # sit = initial situation
    if abs(length - sit) > sit:
        position = length
        sec_position = 1
    else:
        position = 1
        sec_position = length
    return position, sec_position


for item in input_list:
    x1, x2 = max_distance(item[0], item[2])
    y1, y2 = max_distance(item[1], item[3])
    print(x1, y1, x2, y2)