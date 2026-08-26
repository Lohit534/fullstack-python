#1. maximum subarray sum - kadens' alogorithm
n = int(input())
arr = list(map(int, input().split()))

current = arr[0]
maximum = arr[0]

for i in range(1, n):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print(maximum)

#2. next greater element
n = int(input())
arr = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(arr[i])

print(*result)

#3. rotate array by k positions
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k = k % n

if k != 0:
    arr = arr[-k:] + arr[:-k]

print(*arr)

#4. reverse integer
x=int(input())
sign = -1 if x < 0 else 1
x = abs(x)
rev = 0
while x:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10
rev *= sign

#5. second largest element in an array
n = int(input())
arr = list(map(int, input().split()))

largest = float('-inf')
second_largest = float('-inf')

for x in arr:
    if x > largest:
        second_largest = largest
        largest = x
    elif largest > x > second_largest:
        second_largest = x

if second_largest == float('-inf'):
    print(-1)
else:
    print(second_largest)

#6. missing number in an array
n = int(input())
arr = list(map(int, input().split()))

missing = n

for i in range(n):
    missing ^= i ^ arr[i]

print(missing)

#7. check prime number 
n = int(input())

if n < 2:
    print("NO")
else:
    is_prime = True
    i = 2

    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    print("YES" if is_prime else "NO")

#8. two sum
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

seen = {}

for i in range(n):
    complement = target - arr[i]

    if complement in seen:
        print(seen[complement], i)
        break

    seen[arr[i]] = i
else:
    print(-1, -1)


#9. contains duplicate
n = int(input())
arr = list(map(int, input().split()))

seen = set()

for x in arr:
    if x in seen:
        print("YES")
        break
    seen.add(x)
else:
    print("NO")

#10. product of array expect self
n = int(input())
arr = list(map(int, input().split()))

result = [1] * n

prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= arr[i]

suffix = 1
for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= arr[i]

print(*result)

#11. maximum product subarray
n = int(input())
arr = list(map(int, input().split()))

max_prod = arr[0]
min_prod = arr[0]
answer = arr[0]

for x in arr[1:]:
    if x < 0:
        max_prod, min_prod = min_prod, max_prod

    max_prod = max(x, max_prod * x)
    min_prod = min(x, min_prod * x)

    answer = max(answer, max_prod)

print(answer)

#12. find minimum in rotated sorted array
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

#13. search in rotated sorted array
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

#14. 3sum
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = []

for i in range(n - 2):
    if i > 0 and arr[i] == arr[i - 1]:
        continue

    if arr[i] > 0:
        break

    left = i + 1
    right = n - 1

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if total == 0:
            result.append((arr[i], arr[left], arr[right]))

            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1

            left += 1
            right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

if result:
    for triplet in result:
        print(*triplet)
else:
    print(-1)

#15. container with most water
n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1
answer = 0

while left < right:
    width = right - left
    area = width * min(height[left], height[right])
    answer = max(answer, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(answer)