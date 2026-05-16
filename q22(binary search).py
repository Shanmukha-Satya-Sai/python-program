l=list(map(int,input().split()))
se=int(input())
l.sort()
#print(l)
s=0
e=len(l)-1
while s<=e:
    mid=(s+e)//2
    if se==l[mid]:
        print("element found")
        break
    elif se<l[mid]:
        e=mid-1
    else:
        s=mid+1
if s>e:
    print("element not found")



