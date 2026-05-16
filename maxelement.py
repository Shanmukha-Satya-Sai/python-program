l=list(map(int,input().split()))
max=-(10)^6
for i in range(0,len(l)):
    if l[i]>max:
        max=l[i]
print(max)