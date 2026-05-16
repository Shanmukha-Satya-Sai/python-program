#reversing a list without using the predefine and slicing
l=list(map(int,input().split()))
s,e=0,len(l)-1
while s<e:
    l[s],l[e]=l[e],l[s]
    s+=1
    e-=1
print(l)

