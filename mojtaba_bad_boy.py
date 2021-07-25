test_num = input()
result = []
for iters in range(int(test_num)):
    [n, m, i, j] = input().split()
    n = int(n)
    m = int(m)
    i = int(i)
    j = int(j)
    dot1 = [i, j]   # initial point
    # take away from initial point
    if (n-i) >= i:
        dot1[0] += (n-i)
    else:
        dot1[0] -= i-1
    if (m-j) >= j:
        dot1[1] += (m-j)
    else:
        dot1[1] -= j-1

    i, j = dot1[0], dot1[1]    # new initial point
    dot2 = [i, j]
    # take away from second initial point
    if (n-i) >= i:
        dot2[0] += (n-i)
    else:
        dot2[0] -= i-1
    if (m-j) >= j:
        dot2[1] += (m-j)
    else:
        dot2[1] -= j-1
    dot1.extend(dot2)
    result.extend([dot1])

for elem_print in result:
    print(*elem_print)
