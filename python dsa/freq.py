li=[1,5,7,1,3,3,2,1,2]
dic={}
for i in li:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)