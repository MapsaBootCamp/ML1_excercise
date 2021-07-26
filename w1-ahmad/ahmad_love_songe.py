def find_sub_string(sher, start, end):
    y = sher[start - 1: end]
    a = sum(map(lambda x: (ord(x) - 96), y))
    return a

length_poem, number_question = map(int, input().split())

poem = input()

list_solu = []

for i in range(number_question):
    startt, endd = map(int, input().split())
    fi = find_sub_string(poem, startt, endd)
    list_solu.append(fi)



print(*list_solu, sep='\n', end='')