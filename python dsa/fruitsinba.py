#904 fruits into baskets
fruits = [1,2,1]
dic={}
l=0
ans=0
for i in range(len(fruits)):
    val=fruits[i]
    if val in dic:
        dic[val]+=1
    else:
        dic[val]=1
    while len(dic) > 2:
        al=fruits[l]
        dic[al]-=1
        if dic[al]==0:
            dic.pop(al)
        l+=1
    ans=max(ans,i-l+1)   
print(ans)

