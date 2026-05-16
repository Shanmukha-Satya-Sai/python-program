n=int(input())
digits = list(map(int, str(n)))
#print(digits)
s=0
while s<=n:
    for i in digits:
        s+=i
    if s!=n:
        digits.pop(0)
        digits.append(s)
    if s==n:
        print('kth no')
        break
else:
    print("not a kth no")

"""t=n
s=0
while t>0:
    r=t%10
    s+=r
    t=t//10
if s==n:
    print("kth no:")"""
