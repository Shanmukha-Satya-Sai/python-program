l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l1:
    if  i not in l2:
        print(i,end=" ")
