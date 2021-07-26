length_input = int(input())


def place_of_person(arr_data):
    arr_of_pos = []
    for j in range(0 ,len(arr_data)):
        if arr_data[j]['place_r'] <= arr_data[j]['row'] / 2 and arr_data[j]['place_c'] <= arr_data[j]['col'] / 2:
            arr_of_pos.append(1)
        elif arr_data[j]['place_r'] <= arr_data[j]['row'] / 2 and arr_data[j]['place_c'] >= arr_data[j]['col'] / 2:
            arr_of_pos.append(2)
        elif arr_data[j]['place_r'] >= arr_data[j]['row'] / 2 and arr_data[j]['place_c'] <= arr_data[j]['col'] / 2:
            arr_of_pos.append(3)
        elif arr_data[j]['place_r'] >= arr_data[j]['row'] / 2 and arr_data[j]['place_c'] >= arr_data[j]['col'] / 2:
            arr_of_pos.append(4)

    return arr_of_pos


def complements_of_pos(arr_of_possition, dic_of_data):
    arr = []
    for i in range(len(arr_of_possition)):
        if arr_of_possition[i] == 1:
            pos1 = [1, dic_of_data[i]['col']]
            pos2 = [dic_of_data[i]['row'], 1]
            arr.append({ 'pos1': pos1, 'pos2': pos2})


        elif arr_of_possition[i] == 2:
            pos1 = [1, 1]
            pos2 = [dic_of_data[i]['row'], dic_of_data[i]['col']]
            arr.append({'pos1': pos1, 'pos2': pos2})

        elif arr_of_possition[i] == 3:
            pos1 = [1, 1]
            pos2 = [dic_of_data[i]['row'], dic_of_data[i]['col']]
            arr.append({'pos1': pos1, 'pos2': pos2})

        elif arr_of_possition[i] == 1:
            pos1 = [1, dic_of_data[i]['col']]
            pos2 = [dic_of_data[i]['row'], 1]
            arr.append({'pos1': pos1, 'pos2': pos2})

    return arr

def display_data(output_data):
    for i in range(len(output_data)):
        print(output_data[i]['pos1'][0], output_data[i]['pos1'][1], output_data[i]['pos2'][0], output_data[i]['pos2'][1])

arr = []

for i in range(length_input):
    row, col, place_r, place_c = map(int, input().split())
    dic = {'row': row, 'col': col, 'place_r': place_r, 'place_c': place_c}
    arr.append(dic)

x = place_of_person(arr)
# print(x)
display_data(complements_of_pos(x, arr))

