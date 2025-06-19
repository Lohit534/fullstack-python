#dominant same as freq_map

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = {}
    for i in range(n):
        if a[i] in freq:
            freq[a[i]] += 1
        else:
            freq[a[i]] = 1

    max_freq = 0
    second_max_freq = 0

    for key in freq:
        if freq[key] > max_freq:
            second_max_freq = max_freq
            max_freq = freq[key]
        elif freq[key] > second_max_freq:
            second_max_freq = freq[key]

    if max_freq > second_max_freq:
        print("YES")
    else:
        print("NO")