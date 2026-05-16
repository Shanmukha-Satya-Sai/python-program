l=list(map(int,input().split()))
for i in range(0,len(l)):
    ec=0
    bc=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            ec+=1
    for j in range(0,i+1):
        if l[i]==l[j]:
            bc+=1
    if bc==1 or ec==1:
        print(l[i],ec)
