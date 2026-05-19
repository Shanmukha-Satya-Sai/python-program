l=[4,6,0,1,2,0,3,7,0]
i=0
j=0
while j<len(l):
    if l[j]!=0:
        l[i],l[j]=l[j],l[i]
        i+=1
    j+=1
# for k in range(i,len(l)):
#     l[k]=0
print(l)