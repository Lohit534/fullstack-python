#find unique elements

list=list(map(int,input().split(",")))
fixed=1                            
for i in range(1,len(list)):
    if list[i-1]!=list[i]:
        list[fixed]=list[i]
        fixed+=1
    print(list)
print(fixed)

