#subarray
li=[1,9,8]
n=len(li)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):       
            temp.append(li[k])
        ans.append(temp)
print(ans)

#substring
st="ram"
n=len(li)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):       
            temp+=st[k]
        ans.append(temp)
print(ans)

#subsequences are nothing but first element to last to take any elements like sub array