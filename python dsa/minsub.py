#209. Minimum Size Subarray Sum
target = 7
# nums = [2,3,1,2,4,3]
nums = [1,1,1,1,1,1,1,1]
l = 0 
ans = float("inf") 
temp = 0 
for i in range(len(nums)): 
    temp += nums[i] 
    
    while temp >= target: 
        ans = min(ans, i - l + 1) 
        temp -= nums[l] 
        l += 1 
if ans == float("inf"): 
    print() 
print(ans)