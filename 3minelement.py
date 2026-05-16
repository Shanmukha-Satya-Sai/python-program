l=list(map(int,input().split()))
min1=min2=min3=(10**6)
for i in range(0,len(l)):
    if l[i]<min1:
        min3=min2
        min2=min1
        min1=l[i]
    elif l[i]< min2 and l[i]>min1:
        min3=min2
        min2=l[i]
    elif l[i]<min3 and l[i]>min1 and l[i]>min2:
        min3=l[i]
print(min1,min2,min3)
