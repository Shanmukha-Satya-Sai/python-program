l=list(map(int,input().split()))
# s=0
# e=len(l)-1
# while s<e:
#     l[s],l[e]=l[e],l[s]
#     s+=1
#     e-=1
# print(l)

for i in range(len(l),0,-1):
    print(i,end=" ")