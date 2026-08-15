#1248. Count Number of Nice Subarrays
def atmostL(arr,k):
    l=0
    temp=0
    ans=0
    for i in range(len(arr)):
        if arr[i]%2==1:
            temp+=1
            while temp > k:
                if arr[l]%2==1:
                    temp-=1
                l+=1       
            ans+=i-l+1
    return ans
arr =[1,1,2,1,1]
k = 3
print(atmostL(arr,k)-atmostL(arr,k-1))