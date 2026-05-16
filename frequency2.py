l=[1,2,3,4,5,1,2,3,4,5,8]
for i in range(0,len(l)):
    ec=0
    bc=0
    for j in range(i,len(l)):
        if l[i]==l[j]:
            ec+=1
    for k in range(0,i+1):
        if l[i]==l[k]:
            bc+=1
    if bc==1 and ec>1 :
        print(l[i],ec)