#Minimum Difference Between Highest and Lowest of K Scores
nums = [9,4,1,7]
k=2
nums.sort()
n=len(nums)
ans=float("inf")
for i in range(n):
    for j in range(i,n):
        temp=[]
        for m in range(i,j+1):
            temp.append(nums[m])
        if len(temp)==k:
            last=temp[-1]
            first=temp[0]
            ans=min(ans,last-first)
print(ans)

#optimal approach
nums=[9,4,1,7]
nums.sort()
n=len(nums)
k = 2
l=0
ans=float("inf")
for i in range(n):
    if i-l==k:
        l+=1
    if i-l+1==k:
        ans=min(ans,nums[i]-nums[l])
print(ans)