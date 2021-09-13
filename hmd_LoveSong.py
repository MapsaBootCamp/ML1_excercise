import string
alphabet_list = list(string.ascii_lowercase)

line1 = input()
# n = int(line1.split()[0])
q = int(line1.split()[1])

string = input()

res=[] 
for i in range(q):
    inputt=input()
    count=0 
    l = int(inputt.split()[0])
    r = int(inputt.split()[1])
    substring = string[l-1:r]
    for itemm in substring:
        count += alphabet_list.index(itemm)+1
    res.append(count)

# for item in res:
#     print(item)  
print(*res, sep='\n')

