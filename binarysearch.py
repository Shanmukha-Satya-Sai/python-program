l=list(map(int,input().split()))
key=int(input())
l.sort()
s=0
e=len(l)-1
while s<=e:
    mid=(s+e)//2
    if key==l[mid]:
        print('found')
        break
    elif key<l[mid]:
        e=mid-1
    else:
        s=mid+1
if s>e:
    print('not found')
