def is_palindrome(n):
    a=str(n)
    if a[::-1]==a:
        return True
    return False

l=list(map(int,input().split()))
pc=0
for i in range(0,len(l)):
    for j in range(i,len(l)):
        su=0
        res=[]
        for n in range(i,j+1):
            res.append(l[n])
            su+=l[n]
        print(res,su)
        if is_palindrome(su):
            print(res)
