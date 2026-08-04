#Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
n=len(arr)
avg=0
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for m in range(i,j+1):
            temp.append(arr[m])
            tsum+=arr[m]
        if len(temp)==k:
            avg=tsum//k
            if avg >= threshold:
                ans+=1
print(ans)

#optimal approach
n=len(arr)
l=0
ans=0
avg=0
tsum=0
for r in range(n):
    tsum+=arr[r]
    if r-l==k:
        tsum-=arr[l]
        l+=1
    if r-l+1==k:
        avg=tsum//k
        if avg >= threshold:
            ans+=1
print(ans)