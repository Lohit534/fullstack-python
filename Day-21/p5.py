#equal element

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = {}
    max_freq = 0

    for i in range(n):
        if a[i] in freq:
            freq[a[i]] += 1
        else:
            freq[a[i]] = 1

        if freq[a[i]] > max_freq:
            max_freq = freq[a[i]]

    print(n - max_freq)