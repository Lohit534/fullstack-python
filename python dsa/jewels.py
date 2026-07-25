#jewels and stones
# jewels = "aA"
# stones = "aAAbbbb"
# ans=0
# for i in stones:
#     if i in jewels:
#         ans+=1
# print(ans)

#optimal approach

jewels = "aA"
stones = "aAAbbbb"
dic={}
for i in stones:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
ans=0
for i in range(len(jewels)):
    ch=jewels[i]
    if ch in dic:
        ans+=dic[ch]
print(ans)