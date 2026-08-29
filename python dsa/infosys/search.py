# 1. Binary Search
# Sample

# Input

# 6
# 1 3 5 7 9 11
# 7

# Output

# 3
# Code
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)


# 2. Search in Rotated Sorted Array
# Sample

# Input

# 7
# 4 5 6 7 0 1 2
# 0

# Output

# 4
# Code
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break

    if arr[left] <= arr[mid]:
        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1
else:
    print(-1)


#3. Find Minimum in Rotated Sorted Array
# Sample

# Input

# 5
# 4 5 1 2 3

# Output

# 1
# Code
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2

    if arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid

print(arr[left])


# 4. Find Peak Element
# Sample

# Input

# 5
# 1 2 3 1 2

# Output

# 2

# Index 2 contains 3, which is a peak.

# Code
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2

    if arr[mid] < arr[mid + 1]:
        left = mid + 1
    else:
        right = mid

print(left)

# 5. Trapping Rain Water
# Sample

# Input

# 12
# 0 1 0 2 1 0 1 3 2 1 2 1

# Output

# 6
# Code
n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1

left_max = 0
right_max = 0
water = 0

while left < right:
    if height[left] <= height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]

        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]

        right -= 1

print(water)

# 6. Search a 2D Matrix

# Sample

# Input

# 3 4
# 1 3 5 7
# 10 11 16 20
# 23 30 34 60
# 3

# Output

# YES
# Code
rows, columns = map(int, input().split())

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

target = int(input())

left = 0
right = rows * columns - 1

found = False

while left <= right:
    mid = (left + right) // 2

    row = mid // columns
    column = mid % columns

    if matrix[row][column] == target:
        found = True
        break
    elif matrix[row][column] < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print("YES")
else:
    print("NO")

