from q11 import is_prime
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
c,s=0,0
for i in l:
    if is_prime(i):
        c+=1
        s+=i
print(f'{s/c:.2f}')