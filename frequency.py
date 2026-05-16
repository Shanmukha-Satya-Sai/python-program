l=list(map(int,input().split()))
for i in range(0,len(l)):
    c=0
    bc=0
    for j in range(i,len(l)):
        if l[i]==l[j]:
            c+=1
    for k in range(0,i+1):
        if l[i]==l[k]:
            bc+=1
    if bc==1:
        print(l[i],c)