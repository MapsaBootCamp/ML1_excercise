num_str, num_question = input().split()
song = input()
if len(song) != int(num_str):
    raise ValueError
song.lower()
char_point = [0]
point = 0
for char in song:
    point += ord(char) - 96
    char_point.append(point)

output = []
for n in range(int(num_question)):
    qustion = input().split()
    start_index = int(qustion[0])
    end_index = int(qustion[1])
    result = char_point[end_index] - char_point[start_index-1]
    output.append(result)

for print_elem in output:
    print(print_elem)
