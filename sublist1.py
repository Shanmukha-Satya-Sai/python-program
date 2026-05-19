s="abcde"
k=3
l=[]
for i in range(0,k):
    l.append(s[i])
print(l)
for i in range(k,len(s)):
    l.pop(0)
    l.append(s[i])
    print(l)
