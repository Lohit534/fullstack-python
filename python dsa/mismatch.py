#set mismatch

# nums = [1,2,2,4]
# n=len(nums)
# ans=0
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]==nums[j]:
#             temp=nums[j]+1
#             ans=nums[j],temp

# print(list(ans))

#optimal approach
nums = [1,2,2,4]
duplicate=-1
missing=-1
s=set()
for i in range(len(nums)):
    val=nums[i]
    if val not in s:
        s.add(val)
    else:
        duplicate=val
for i in range(1,len(nums)+1):
    if i not in s:
        missing=i
print([duplicate,missing])
