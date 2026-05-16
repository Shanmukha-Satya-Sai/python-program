"""Valid paranthesis or not
{[()]}
Valid
{[(})}
Not valid
[]{}()
Valid"""
s=input()
si=0
e=len(s)-1
c=0
while si<e:
    if s[si]=="{" and (s[si+1]=="}" or s[e]=="}"):
        c+=1
    elif s[si]=="[" and (s[si+1]=="]" or s[e]=="]"):
        c+=1
    elif s[si] == "(" and (s[si + 1] == ")" or s[e] == ")"):
        c+=1
    si += 1
    e -= 1
if c==len(s)//2:
    print("valid paranthesi")
else:
    print("False")


