#Array Partition
nums = [1,4,3,2]     
nums.sort()
n=len(nums)
ans=0
for i in range(0,n,2):
        ans+=nums[i]
print(ans)

#Minimum Cost of Buying Candies With Discount
cost = [1,2,3]
cost.sort()
ans=0
purchase=0
for i in range(len(cost)-1,-1,-1):
    if purchase==2:
        purchase=0
    else:
        ans+=cost[i]
        purchase+=1
print(ans)