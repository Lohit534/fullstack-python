#Discount

t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Your code goes here
    total1 = 0
    for i in range(n):
        total1 += a[i]

    total2 = 0
    for i in range(n):
        if a[i] <= y:
            total2 += 0
        else:
            total2 += a[i] - y

    total2 += x

    if total2 < total1:
        print("COUPON")
    else:
        print("NO COUPON")

    t -= 1
