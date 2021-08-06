# Love Song
# 1539B
# codeforces.com
import string
alphabet={}
code=0
for char in list(string.ascii_lowercase):
    repeat_char=char
    for num in range(code):
        repeat_char+=char
    alphabet.update({char:repeat_char})
    code+=1
print(alphabet)
limit=[]
length_song=input("The length of the song:")
num_questions=input("The number of questions:")
song=input("The song, consisting of n lowercase letters of English letters:")
if len(song)==int(length_song):
    for question in range(int(num_questions)):
        l, r = input("The bounds of the question (l and r):").split(' ')
        limit.append([int(l), int(r)])
    result = []
    for row in limit:
        temp_str = song[row[0] - 1:row[1]]
        temp=''
        for char_temp in temp_str:
            temp=temp+alphabet[char_temp]
        result.append([temp_str, len(temp)])
    print(result)
else:
    print("<length of the song> is not equal <len(song string)>")
    raise Exception
