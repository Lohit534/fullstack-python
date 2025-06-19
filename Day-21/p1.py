# seaech the element

n,x=map(int,input().split())
a=list(map(int,input().split()))
array=False
for i in range(n):
    if a[i]==x:
        array=True
        break
if array:
    print("YES")
else:
    print("NO")