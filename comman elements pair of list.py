l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
        l2.remove(i)
print(l3)
