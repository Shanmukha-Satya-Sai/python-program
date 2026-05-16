l=list(map(int,input().split()))
for i in range(0,len(l)):
    c=0
    b=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            c+=1
    for k in range(0,i+1):
        if l[i]==l[j]:
            b+=1

    if c==1:
        print(l[i])
