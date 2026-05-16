#Write a program to convert a list of digits into a number.
l=list(map(int,input().split()))
num=0
for i in l:
    num=num*10+i
print(num)

#Write a program to convert a number into a list of digits
n = int(input())

digits = list(map(int, str(n)))

print(digits)

# Write a program to reverse a list and also reverse each element in the list.
l = list(map(int, input().split()))

res = []

for i in l[::-1]:          # reverse list
    rev = int(str(i)[::-1])  # reverse each element
    res.append(rev)

print(res)