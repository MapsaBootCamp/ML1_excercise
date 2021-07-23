no_test=int(input())
res=[]
for i in range(no_test):
    inputt=input()
    dimension=(int(inputt.split()[0]), int(inputt.split()[1]))
    pos=(int(inputt.split()[2])-1, int(inputt.split()[3])-1)
    
    if pos[0]<(dimension[0]/2):
        if pos[1]<(dimension[1]/2):
            r1=(int(inputt.split()[0]), int(inputt.split()[1]))
            r2=(1, 1)
        else:
            r1=(int(inputt.split()[0]), int(inputt.split()[1]))
            r2=(int(inputt.split()[0]),1)
    else:
        if pos[1]<(dimension[1]/2):
            r1=(int(inputt.split()[0]), 1)
            r2=(1,int(inputt.split()[1]))
        else:
            r1=(1, 1)
            r2=(int(inputt.split()[0]), int(inputt.split()[1]))
    res.append(str(r1[0])+' '+str(r1[1])+' '+str(r2[0])+' '+str(r2[1]))

for item in res:
    print(*item, sep='')