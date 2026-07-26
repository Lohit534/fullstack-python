#decode the message

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
dic={}
temp=97
for i in key:
    if i!=" " and i not in dic:
        dic[i]=chr(temp)
        temp+=1
ans=""
for i in message:
    if i==" ":
        ans+=" "
    else:
        ans+=dic[i]
print(ans)