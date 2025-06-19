#min to max

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    x = a[0]
    for i in range(1, n):
        if a[i] < x:
            x = a[i]
            
    count = 0
    for i in range(n):
        if a[i]> x:
            count += 1
            
    print(count)