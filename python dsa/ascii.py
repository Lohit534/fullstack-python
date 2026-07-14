s="abcd"
ans=0

for i in range(len(s)-1):
    a=ord(s[i])
    b=ord(s[i+1])
    t=abs(a-b)
    ans+=t
print(ans)


li=["--X","X++","X++"]
x=0
for i in range(len(li)):
    temp=li[i]
    if temp=="X--" or temp=="--X":
        x-=1
    else:
        x+=1
print(x)



address = "1.1.1.1"
ans=""
for i in address:
    if i ==".":
        ans+="[.]"
    else:
        ans+=i
print(ans)
            

jewels="abB"
stones="abcBBA"
ans=0
for i in range(len(jewels)):
    for j in range(len(stones)):
        if jewels[i]==stones[j]:
            ans+=1
            
print(ans)
