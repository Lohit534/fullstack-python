#438. Find All Anagrams in a String
s = "abab"
p = "ab"
def fun(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in s1:
        if i not in s2 or s1[i]!=s2[i]:
            return False
    return True 
    
d1={}
d2={}
for i in p:
    if i in d2:
        d2[i]+=1
    else:
        d2[i]=1
l=0
ans=[]
k=len(p)
for i in range(len(s)):
    al=s[i]
    if al in d1:
        d1[al]+=1
    else:
        d1[al]=1
    if i-l==k:
        val=s[l]
        d1[val]-=1
        if d1[val]==0:
            d1.pop(val)
        l+=1
    if i-l+1==k and fun(d1,d2):
        ans.append(l)      
print(ans)