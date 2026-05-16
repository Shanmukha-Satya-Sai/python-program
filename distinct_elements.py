l=list(map(int,input().split()))
# l2=list(map(int,input().split()))
for i in range(0,len(l)):
    ec=0
    bc=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            ec+=1
    for k in range(i,-1,-1):
        if l[i]==l[k]:
            bc+=1
    if bc==1:
        print(l[i],ec)
