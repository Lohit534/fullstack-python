# 1. Merge Intervals
# Sample

# Input

# 4
# 1 3
# 2 6
# 8 10
# 9 12

# Output

# 1 6
# 8 12
# Code
n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

merged = []

for i in range(n):
    start = intervals[i][0]
    end = intervals[i][1]

    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        if end > merged[-1][1]:
            merged[-1][1] = end

for i in range(len(merged)):
    print(merged[i][0], merged[i][1])

