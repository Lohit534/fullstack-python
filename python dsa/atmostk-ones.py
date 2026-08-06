# You are given an array and You should
# Find the maximum length of the
# subarray which has atmost k ones

# Example:
nums=[0,1,3,1,1,6,7,1,0,1] 
k =2
# Ans: 5
l=0
temp=0
ans=0
for r in range(len(nums)):
    if nums[r]==1:
        temp+=1
    while temp > k:
        if nums[l]==1:
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)
