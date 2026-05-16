l=list(map(int,input().split()))
min=10^6
for i in range(0,len(l)):
    if l[i]<min:
        min=l[i]
print(min)