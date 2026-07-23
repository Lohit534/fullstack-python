li=[2,5,1,9,0,3]
n=len(li)
for i in range(n):
    isswapped=False
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            isswapped=True
    print(li)
    if isswapped == False:
        break
print(li)