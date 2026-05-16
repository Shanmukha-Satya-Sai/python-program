l=list(map(int,input().split()))
res=[]
for i in l:
    su=1
    for j in range(i,1,-1):
        su*=j
    res.append(su)
print(res)

