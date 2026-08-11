#3. Longest Substring Without Repeating Characters

s= "abcabcbb"
l=0
ans=0
uni=set()
for i in range(len(s)):
    ch=s[i]
    if ch not in uni:
        uni.add(ch)
    else:
        while ch in uni:
            uni.remove(s[l])
            l+=1
        uni.add(ch)
    ans=max(ans,i-l+1)
print(ans)