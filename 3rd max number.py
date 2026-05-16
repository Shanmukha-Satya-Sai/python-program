l=[65,89,65,99,89,99]
max1=max2=max3=-(10^6)
for i in range(0,len(l)):
    if l[i]>max1:
        max3=max2
        max2=max1
        max1=l[i]
    elif l[i]>max3 and max1<l[i]<max2:
        max3=l[i]
print(max3)
