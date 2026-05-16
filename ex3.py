"""Special Palindrome

ma@la&ya*la!m
Palindrome

abc*,De.&dc@BA
Palindrome

ab@bc%c
Not Palindrome"""

s=input()
res=""
for i in range(0,len(s)):
    asi=ord(s[i])
    if 65<=asi<=90:
        res+=s[i]
    elif 97<=asi<=122:
        res+=s[i]
# print(res)
si=0
e=len(res)-1
while si<e:
    if res[si].lower()!=res[e].lower():
        print("Not Palindrome")
        break
    si+=1
    e-=1
else:
    print("palindrome")
