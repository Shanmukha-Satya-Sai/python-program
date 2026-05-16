# 3
# r
#     r 1
#   s 4 t 7
# u 10 v 13 w 16
#   x 19 y 20
#     z 21



n=int(input())
s=input()
c=1
z=ord(s)

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i*2+1):
        if k%2==1:
            print(chr(z),end=" ")
            z+=1
        else:
            print(c,end=" ")
            c+=3
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(1,(n-i)*2+1):
        if k%2==1:
            print(chr(z),end=" ")
            z+=1
        else:
            print(c,end=" ")
            c+=1
    print()