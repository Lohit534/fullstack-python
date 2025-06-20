#cost of groceries

t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    count = 0
    for i in range(n):
        if a[i] >= x:
            count+=b[i]

    print(count)
    t -= 1