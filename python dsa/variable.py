#Fixed Sized Sliding Window Code Python
arr = [9,3,4,8,1]
l=0
temp=0
k=3
ans=0
for r in range(len(arr)):
    temp += arr[r]
    if(r-l==k):
        temp-=arr[l] 
        l+=1
    if (r-l+1==k):
        ans=max(ans, temp)
print(ans)

#Variable Size Sliding Window Code Python
arr = [9,3,4,8,1]
l=0
temp=0
k=10
ans =0
for r in range(len(arr)):
    temp += arr[r]
    while temp > k:
        temp -= arr[l] 
        l+=1
    ans = max(ans, r-l+1)
print(ans)