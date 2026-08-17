# 930. Binary Subarrays With Sum
def Bsub(arr,k):
    if k < 0:
        return 0
    l=0
    temp=0
    ans=0
    for i in range(len(arr)):
        if arr[i]==1:
            temp+=1
        while temp > k:
            if arr[l]==1:
                temp-=1
            l+=1
        ans+=i-l+1
    return ans

nums = [1,0,1,0,1] 
goal = 2
print (Bsub(nums,goal)-Bsub(nums,goal-1))