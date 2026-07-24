#number of good pairs
nums = [1,2,3,1,1,3]
dic={}
count=0
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i]==nums[j] and i<j:
            count+=1
print(count)


#optimal approach
nums=[1,2,3,1,1,3]
dic={}
count=0
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in dic:
    n=dic[i]
    temp=n*(n-1)//2
    count+=temp
print(count)
