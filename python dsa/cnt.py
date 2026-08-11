#Maximize the Confusion of an Exam
answerKey = "TTFF"
k = 2
n=len(answerKey)
cnt=0
cnf=0
l=0
ans=0
for i in range(n):
    if answerKey[i]=='T':
        cnt+=1
    else:
        cnf+=1
    while min(cnt,cnf) > k:
        if answerKey[l]=="T":
            cnt-=1
        else:
            cnf-=1
        l+=1
    ans=max(ans,i-l+1)
print(ans)

'''Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''
nums=[1,1,1,0,0,0,1,1,1,1,0]
k = 2
l=0
temp=0
ans=0
for i in range(len(nums)):
    if nums[i]==0:
        temp+=1
    while temp >k:
        if nums[l]==0:
            temp-=1
        l+=1
        
    ans=max(ans,i-l+1)
print(ans)