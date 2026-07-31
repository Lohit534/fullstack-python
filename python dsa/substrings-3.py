#substrings of size three with distinct characters

s = "aababcabc"
n=len(s)
ans=0
l=3
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp+=(s[k])
        if len(temp)==l and len(set(temp))==l:
            # print(temp)
            ans+=1
print(ans)


#optimal approach
n=len(s)
l=0
k=3
dic={}
ans=0
for r in range(n):
    if s[r] in dic:
        dic[s[r]]+=1
    else:
        dic[s[r]]=1
    
    if r-l==k:
        dic[s[l]]-=1
        if dic[s[l]]==0:
            dic.pop(s[l])
        l+=1
    if len(dic)==k:
        ans+=1
print(ans)
