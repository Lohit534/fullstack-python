# major element

nums=[2,2,1,1,1,2,2]
n=len(nums)
dic={}
major=nums[0]
for i in nums:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
ans=-1
for i in dic:
    temp=n//2
    val=dic[i]
    if val > temp:
        ans=i
        break
print(ans)

 #Another approah
nums=[2,2,1,1,1,2,2]
nums.sort()
temp=len(nums)//2
print(nums[temp])


#Best space approach
nums=[2,2,1,1,1,2,2]
count=0
major=0
for num in nums:
    if count==0:
        major=num
    if num==major:
        count+=1
    else:
        count-=1
print(major)