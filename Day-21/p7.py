#roundup return the change

t = int(input())

for _ in range(t):
    x = int(input())
    rem = x % 10
    if rem < 5:
        rounded = x - rem
    else:
        rounded = x + (10 - rem)
    print(100 - rounded)