# 1. Top K Frequent Elements
# Sample

# Input

# 6 2
# 1 1 1 2 2 3

# Output

# 1 2
# Code
n, k = map(int, input().split())
arr = list(map(int, input().split()))

frequency = {}

for i in range(n):
    value = arr[i]

    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

items = []

for value in frequency:
    items.append([frequency[value], value])

items.sort(key=lambda x: (-x[0], x[1]))

answer = []

for i in range(k):
    answer.append(items[i][1])

print(*answer)


# 2. Merge K Sorted Lists
# Sample

# Input

# 3
# 3
# 1 4 5
# 3
# 1 3 4
# 2
# 2 6
# Output
# 1 1 2 3 4 4 5 6
# Code
k = int(input())

lists = []

for i in range(k):
    size = int(input())
    values = list(map(int, input().split()))
    lists.append(values)

heap = []

for i in range(k):
    if len(lists[i]) > 0:
        heap.append([lists[i][0], i, 0])

for i in range(len(heap) // 2 - 1, -1, -1):
    position = i

    while True:
        smallest = position
        left = 2 * position + 1
        right = 2 * position + 2

        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left

        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right

        if smallest == position:
            break

        heap[position], heap[smallest] = heap[smallest], heap[position]
        position = smallest

answer = []

while heap:
    value = heap[0][0]
    list_index = heap[0][1]
    element_index = heap[0][2]

    answer.append(value)

    if element_index + 1 < len(lists[list_index]):
        next_value = lists[list_index][element_index + 1]
        heap[0] = [next_value, list_index, element_index + 1]

        position = 0

        while True:
            smallest = position
            left = 2 * position + 1
            right = 2 * position + 2

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left

            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right

            if smallest == position:
                break

            heap[position], heap[smallest] = heap[smallest], heap[position]
            position = smallest
    else:
        heap[0] = heap[-1]
        heap.pop()

        position = 0

        while True:
            smallest = position
            left = 2 * position + 1
            right = 2 * position + 2

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left

            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right

            if smallest == position:
                break

            heap[position], heap[smallest] = heap[smallest], heap[position]
            position = smallest

print(*answer)