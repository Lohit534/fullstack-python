# 1. Activity Selection
# Sample

# Input

# 6
# 1 2
# 3 4
# 0 6
# 5 7
# 8 9
# 5 9

# Output

# 4
# Code
n = int(input())

activities = []

for i in range(n):
    start, end = map(int, input().split())
    activities.append([start, end])

activities.sort(key=lambda x: x[1])

count = 0
last_end = -1

for i in range(n):
    start = activities[i][0]
    end = activities[i][1]

    if start >= last_end:
        count += 1
        last_end = end

print(count)


# 2. Fractional Knapsack
# Sample

# Input

# 3 50
# 60 10
# 100 20
# 120 30

# Output

# 240.00
# Code
n, capacity = map(int, input().split())

items = []

for i in range(n):
    value, weight = map(int, input().split())
    ratio = value / weight
    items.append([ratio, value, weight])

items.sort(reverse=True)

total = 0.0
remaining = capacity

for i in range(n):
    if remaining == 0:
        break

    ratio = items[i][0]
    value = items[i][1]
    weight = items[i][2]

    if weight <= remaining:
        total += value
        remaining -= weight
    else:
        total += ratio * remaining
        remaining = 0

print(f"{total:.2f}")


# 3. Jump Game
# Sample

# Input

# 5
# 2 3 1 1 4

# Output

# YES
# Code
n = int(input())
arr = list(map(int, input().split()))

farthest = 0

for i in range(n):
    if i > farthest:
        print("NO")
        break

    farthest = max(farthest, i + arr[i])

    if farthest >= n - 1:
        print("YES")
        break
else:
    print("NO")


# 4. Minimum Platforms
# Sample

# Input

# 6
# 900 940 950 1100 1500 1800
# 910 1200 1120 1130 1900 2000

# Output

# 3
# Code
n = int(input())
arrivals = list(map(int, input().split()))
departures = list(map(int, input().split()))

arrivals.sort()
departures.sort()

arrival_index = 0
departure_index = 0
platforms = 0
answer = 0

while arrival_index < n and departure_index < n:
    if arrivals[arrival_index] <= departures[departure_index]:
        platforms += 1
        answer = max(answer, platforms)
        arrival_index += 1
    else:
        platforms -= 1
        departure_index += 1

print(answer)


# 5. Job Sequencing
# Sample

# Input

# 4
# 1 4 20
# 2 1 10
# 3 1 40
# 4 1 30

# Output

# 2 60
# Code
n = int(input())

jobs = []
max_deadline = 0

for i in range(n):
    job_id, deadline, profit = map(int, input().split())
    jobs.append([profit, deadline, job_id])
    max_deadline = max(max_deadline, deadline)

jobs.sort(reverse=True)

slots = [-1] * (max_deadline + 1)

count = 0
total_profit = 0

for i in range(n):
    profit = jobs[i][0]
    deadline = jobs[i][1]

    slot = min(deadline, max_deadline)

    while slot > 0 and slots[slot] != -1:
        slot -= 1

    if slot > 0:
        slots[slot] = jobs[i][2]
        count += 1
        total_profit += profit

print(count, total_profit)


# 6. Assign Cookies
# Sample

# Input

# 3 2
# 1 2 3
# 1 1

# Output

# 1
# Code
n, m = map(int, input().split())

children = list(map(int, input().split()))
cookies = list(map(int, input().split()))

children.sort()
cookies.sort()

child_index = 0
cookie_index = 0
satisfied = 0

while child_index < n and cookie_index < m:
    if cookies[cookie_index] >= children[child_index]:
        satisfied += 1
        child_index += 1
        cookie_index += 1
    else:
        cookie_index += 1

print(satisfied)

# 7. Task Scheduler
# Sample

# Input

# 6 2
# A A A B B B

# Output

# 8

# One valid schedule:

# A B idle A B idle A B
# Code
task_count, cooldown = map(int, input().split())
tasks = input().split()

frequency = {}

for i in range(task_count):
    task = tasks[i]

    if task in frequency:
        frequency[task] += 1
    else:
        frequency[task] = 1

max_frequency = 0
same_max = 0

for task in frequency:
    if frequency[task] > max_frequency:
        max_frequency = frequency[task]
        same_max = 1
    elif frequency[task] == max_frequency:
        same_max += 1

part_count = max_frequency - 1
part_length = cooldown + 1

minimum_intervals = part_count * part_length + same_max

if minimum_intervals < task_count:
    minimum_intervals = task_count

print(minimum_intervals)