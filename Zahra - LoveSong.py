import string


n, q = [int(x) for x in input().split()]
song = str(input())

q_length = []

while q > 0:
    a, b = [int(x) for x in input().split()]
    q_length.append((a, b))
    q -= 1

alphabets = []
sum_new_song = 0

for gamut in q_length:
    for char in song[gamut[0]-1:gamut[1]]:
        index = string.ascii_lowercase.index(char) + 1
        alphabets.append(char*index)
    new_song = ''.join(alphabets)
    print(len(new_song))
    alphabets = []