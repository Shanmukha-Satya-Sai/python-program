l=list(map(int,input().split()))
m=min(l)
c=0
while c<4:
    if m+1 not in l:
        print(m+1)
        c+=1
    m+=1
