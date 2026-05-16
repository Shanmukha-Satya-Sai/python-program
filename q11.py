import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

l=[2,3,4,5,6,7,8,9,10,11,12,13,15]
l2=[]
for i in l:
    if is_prime(i):
        l2.append(i)
print(l2)


