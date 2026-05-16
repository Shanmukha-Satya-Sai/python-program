l=list(map(int,input().split()))
se=int(input())
if se in l:
    for i in range(0,len(l)):
        if se==l[i]:
            print(f"element found and it's index is {i}")
            break
else:
    print("element not in list")