# 1. Sort Colors
# Sample

# Input

# 6
# 2 0 2 1 1 0

# Output

# 0 0 1 1 2 2
# Code
n = int(input())
arr = list(map(int, input().split()))

left = 0
mid = 0
right = n - 1

while mid <= right:
    if arr[mid] == 0:
        arr[left], arr[mid] = arr[mid], arr[left]
        left += 1
        mid += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[right] = arr[right], arr[mid]
        right -= 1

print(*arr)


# 2. Merge Sort
# Sample

# Input

# 6
# 5 2 8 1 3 7

# Output

# 1 2 3 5 7 8
# Code
def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    temp = []
    first = left
    second = mid + 1

    while first <= mid and second <= right:
        if arr[first] <= arr[second]:
            temp.append(arr[first])
            first += 1
        else:
            temp.append(arr[second])
            second += 1

    while first <= mid:
        temp.append(arr[first])
        first += 1

    while second <= right:
        temp.append(arr[second])
        second += 1

    for position in range(len(temp)):
        arr[left + position] = temp[position]


n = int(input())
arr = list(map(int, input().split()))

merge_sort(arr, 0, n - 1)

print(*arr)


# 3. Quick Sort

# Sample

# Input

# 6
# 5 2 8 1 3 7

# Output

# 1 2 3 5 7 8
# Code
def partition(arr, left, right):
    pivot = arr[right]
    position = left

    for i in range(left, right):
        if arr[i] <= pivot:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1

    arr[position], arr[right] = arr[right], arr[position]

    return position


def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot_position = partition(arr, left, right)

    quick_sort(arr, left, pivot_position - 1)
    quick_sort(arr, pivot_position + 1, right)


n = int(input())
arr = list(map(int, input().split()))

quick_sort(arr, 0, n - 1)

print(*arr)