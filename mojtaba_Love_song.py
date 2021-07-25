num_str, num_question = input().split()
song = input()
if len(song) != int(num_str):
    raise ValueError

output = []
for row in range(int(num_question)):
    result = 0
    qustion = input().split()
    segment = song[int(qustion[0])-1:int(qustion[1])].lower()
    for elem in segment:
        result += ord(elem) - 96
    output.append(result)

for print_elem in output:
    print(print_elem)
