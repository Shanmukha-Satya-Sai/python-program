from q11 import is_prime
def next_prime(n):
    p=n+1
    while True:
        if is_prime(p):
            return p
        p+=1

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l2=[]
for i in l:
    l2.append(next_prime(i))
print(l)
print(l2)


