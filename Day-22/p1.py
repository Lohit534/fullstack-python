#devu and friends

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = set()
    for i in a:
        x.add(i)
    print(len(x))