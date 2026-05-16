n = int(input())
a,b=0,1
fc=0
fl=[]
while a<=n:
    fl.append(a)
    c=a+b
    a=b
    b=c
for i in range(1,n+1):
    if i not in fl:
        print(i,end=" ")