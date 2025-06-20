#chef and dolls

t=int(input())
for _ in range(t):
    n=int(input())
    dolls=0
    for _ in range(n):
        a=int(input())
        dolls^=a
    print(dolls)