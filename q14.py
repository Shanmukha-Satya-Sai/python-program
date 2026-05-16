l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ec,oc=0,0
for i in l:
    if i%2==0:
        ec+=1
    elif i%2==1:
        oc+=1
print(f'even count={ec},odd count={oc}')
