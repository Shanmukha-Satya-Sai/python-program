nums=[1,1,2,4,5]
for i in range(0,len(nums)):
    ec=0
    bc=0
    for j in range(0,len(nums)):
        if nums[i]==nums[j]:
            ec+=1
    for k in range(i,-1,-1):
        if nums[i]==nums[k]:
            bc+=1
    if bc==1:
        print(nums[i])