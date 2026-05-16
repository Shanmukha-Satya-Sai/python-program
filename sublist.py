l=list(map(int,input().split()))
key=3
for i in range(0,len(l)):
    for j in range(i,len(l)):
        sub_list=l[i:j+1]
        print(sub_list)
    print()
        # if len(sub_list)==key:
        #     print(sub_list)