l=list(map(int,input().split()))
t=3
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==t:
            print(l[i],l[j])
