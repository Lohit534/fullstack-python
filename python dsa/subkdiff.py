#992. Subarrays with K Different Integers
def DiffK(arr,k):
    l=0
    dic={}
    ans=0
    for r in range(len(arr)):
        if arr[r] in dic:
            dic[arr[r]]+=1
        else:
            dic[arr[r]]=1
        while len(dic) > k:
            val=arr[l]
            dic[val]-=1
            if dic[val]==0:
                dic.pop(val)
            l+=1
        ans+=r-l+1
    return ans
nums = [1,2,1,2,3]
k = 2
print(DiffK(nums,k)-DiffK(nums,k-1))