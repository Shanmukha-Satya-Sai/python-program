#print all sublist whose size is k
l=list(map(int,input().split()))
k=int(input())
for i in range(0,len(l)):
    for j in range(i,len(l)):
        res=[]
        for n in range(i,j+1):
            res.append(l[n])
        if len(res)==k:
            print(res)
        elif len(res)>k:
            break


