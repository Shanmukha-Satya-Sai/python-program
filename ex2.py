"""Input 1 : 1/2

               6/5

Output : 17/10

Input 2 :  1/3
                1/4

Output 2 :  7/12

Input 3 : 5/2

               10/3

Output  3 : 35/6"""

a=input().split("/")
b=input().split("/")
m,x=a
n,y=b
m=int(m)
n=int(n)
x=int(x)
y=int(y)
if x==y:
    n=str(m+n)
    d=str(x)
    res=n+"/"+d
    print(res)
else:
    n=str((m*y)+(n*x))
    d=str(x*y)
    res=n+"/"+d
    print(res)
