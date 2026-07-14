a=[5,8,10,11,15,50,20,25]
max=0
for i in range(len(a)):
    val=a[i]
    if val>max:
        max=val
print(max)

sentences=["hello macha how are you","hi","you are my"]
ans=0
for i in range(len(sentences)):
    s=sentences[i]
    count=1
    for j in range(len(s)):
        ch = s[j]
        if ch == " ":
            count+=1
    ans = max(ans , count)
print(ans)