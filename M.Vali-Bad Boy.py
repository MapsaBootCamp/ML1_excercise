a = int(input())
result=[]
for i in range(a):
    [n, m, i, j] = input().split()
    n = int(n)
    m = int(m)
    i = int(i)
    j = int(j)
    d0=[i,j]
    if (n-i)>=i:
        i+=(n-i)
    else:
        i = i - (i-1)
    if (m-j)>=j:
        j+=(m-j)
    else:
        j-=(j-1)
    d1=[i,j]
    if (n-i)>=i:
        i+=(n-i)
    else:
        i = i - (i-1)
    if (m-j)>=j:
        j+=(m-j)
    else:
        j-=(j-1)
    d2=[i,j]
    d1.extend(d2)
    result.append(d1)

for i in result:
    print(*i)

# print(d1, d2)
