l=[1,1,1,2,2,3,4,5,6,1,2,3,4,5,6,7,8]
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)
print(d.items())
for i in sorted(d.items(),key=lambda x:x[1],reverse=True):
     print(i[0],end=" ")
