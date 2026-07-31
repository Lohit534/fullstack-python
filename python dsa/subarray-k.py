nums = [1,1,1]
k = 2
n=len(nums)
l=0
temp=0
ans=0
for r in range(n):
    temp+=nums[r]
    if r-l==k:
        temp-=nums[l]
        break
    if temp==k:
        ans=max(ans,temp)
print(ans)