# 1. Climbing Stairs
# Sample

# Input

# 5

# Output

# 8
# Code
n = int(input())

if n <= 2:
    print(n)
else:
    first = 1
    second = 2

    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    print(second)


# 2. House Robber


# Sample

# Input

# 4
# 1 2 3 1

# Output

# 4
# Code
n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0])
else:
    previous_two = 0
    previous_one = 0

    for i in range(n):
        current = max(previous_one, previous_two + arr[i])
        previous_two = previous_one
        previous_one = current

    print(previous_one)


# 3. House Robber II


# Sample

# Input

# 3
# 2 3 2

# Output

# 3
# Code
def rob_range(arr, start, end):
    previous_two = 0
    previous_one = 0

    for i in range(start, end + 1):
        current = max(previous_one, previous_two + arr[i])
        previous_two = previous_one
        previous_one = current

    return previous_one


n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0])
else:
    option_one = rob_range(arr, 0, n - 2)
    option_two = rob_range(arr, 1, n - 1)

    print(max(option_one, option_two))


# 4. Coin Change



# Sample

# Input

# 3 11
# 1 2 5

# Output

# 3

# Because:

# 5 + 5 + 1 = 11
# Code
n, amount = map(int, input().split())
coins = list(map(int, input().split()))

dp = [amount + 1] * (amount + 1)
dp[0] = 0

for current_amount in range(1, amount + 1):
    for coin_index in range(n):
        coin = coins[coin_index]

        if coin <= current_amount:
            dp[current_amount] = min(
                dp[current_amount],
                dp[current_amount - coin] + 1
            )

if dp[amount] == amount + 1:
    print(-1)
else:
    print(dp[amount])

# 5. Longest Common Subsequence


# Sample

# Input

# abcde
# ace

# Output

# 3

# LCS:

# ace
# Code
s1 = input().strip()
s2 = input().strip()

if len(s1) < len(s2):
    short_string = s1
    long_string = s2
else:
    short_string = s2
    long_string = s1

previous = [0] * (len(short_string) + 1)

for i in range(1, len(long_string) + 1):
    current = [0] * (len(short_string) + 1)

    for j in range(1, len(short_string) + 1):
        if long_string[i - 1] == short_string[j - 1]:
            current[j] = previous[j - 1] + 1
        else:
            current[j] = max(previous[j], current[j - 1])

    previous = current

print(previous[-1])


# 6. Longest Increasing Subsequence

# Sample

# Input

# 8
# 10 9 2 5 3 7 101 18

# Output

# 4

# One LIS is:

# 2 3 7 101
# Code
n = int(input())
arr = list(map(int, input().split()))

tails = []

for i in range(n):
    value = arr[i]

    left = 0
    right = len(tails)

    while left < right:
        mid = (left + right) // 2

        if tails[mid] < value:
            left = mid + 1
        else:
            right = mid

    if left == len(tails):
        tails.append(value)
    else:
        tails[left] = value

print(len(tails))


# 7. Subset Sum

# Sample

# Input

# 4 9
# 3 34 4 12

# Output

# YES

# Because:

# 3 + 4 + 2

# is not valid for this input, but 3 + 12 exceeds 9. So let's use the correct subset:

# 4 9
# 3 34 4 5

# Output:

# YES

# because:

# 4 + 5 = 9
# Code
n, target = map(int, input().split())
arr = list(map(int, input().split()))

dp = [False] * (target + 1)
dp[0] = True

for i in range(n):
    value = arr[i]

    for current_sum in range(target, value - 1, -1):
        if dp[current_sum - value]:
            dp[current_sum] = True

if dp[target]:
    print("YES")
else:
    print("NO")


# 8. Unique Paths


# Sample

# Input

# 3 7

# Output

# 28
# Code
m, n = map(int, input().split())

dp = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])
print(dp[m - 1][n - 1])

# 9. Longest Palindromic Substring

# Sample

# Input

# babad

# Output

# bab

# aba is also a valid answer.

# Code
s = input().strip()

n = len(s)

if n == 0:
    print("")
else:
    best_start = 0
    best_length = 1

    dp = [[False] * n for i in range(n)]

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1

            if s[start] == s[end]:
                if length == 2 or dp[start + 1][end - 1]:
                    dp[start][end] = True

                    if length > best_length:
                        best_length = length
                        best_start = start

    print(s[best_start:best_start + best_length])


# 10. Palindromic Substrings


# Sample

# Input

# aaa

# Output

# 6

# The palindromic substrings are:

# a
# a
# a
# aa
# aa
# aaa
# Code
s = input().strip()

n = len(s)
def expand(self, s, left, right):
    count = 0
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        count += 1
        left -= 1
        right += 1
    return count
def countSubstrings(self, s):
    ans = 0
    for i in range(len(s)):
        ans += self.expand(s, i, i)
        
        ans += self.expand(s, i, i + 1)
    return ans

# 11. Decode Ways
# Sample

# Input

# 226

# Output

# 3

# Possible:

# 2 2 6
# 22 6
# 2 26
# Code
s = input().strip()

n = len(s)

if n == 0 or s[0] == '0':
    print(0)
else:
    previous_two = 1
    previous_one = 1

    for i in range(1, n):
        current = 0

        if s[i] != '0':
            current += previous_one

        number = (ord(s[i - 1]) - ord('0')) * 10 + (ord(s[i]) - ord('0'))

        if 10 <= number <= 26:
            current += previous_two

        previous_two = previous_one
        previous_one = current

    print(previous_one)


# 12. Word Break
# Sample

# Input

# leetcode
# 2
# leet code

# Output

# YES
# Code
s = input().strip()
n = int(input())
words = input().split()

word_set = set(words)
length = len(s)

dp = [False] * (length + 1)
dp[0] = True

max_word_length = 0

for i in range(n):
    if len(words[i]) > max_word_length:
        max_word_length = len(words[i])

for end in range(1, length + 1):
    start = max(0, end - max_word_length)

    for position in range(start, end):
        if dp[position] and s[position:end] in word_set:
            dp[end] = True
            break

if dp[length]:
    print("YES")
else:
    print("NO")


# 13. Maximum Product Subarray
# Sample

# Input

# 4
# 2 3 -2 4

# Output

# 6
# Code
n = int(input())
arr = list(map(int, input().split()))

maximum = arr[0]
minimum = arr[0]
answer = arr[0]

for i in range(1, n):
    value = arr[i]

    if value < 0:
        maximum, minimum = minimum, maximum

    maximum = max(value, maximum * value)
    minimum = min(value, minimum * value)

    answer = max(answer, maximum)

print(answer)


# 14. Longest Increasing Path in a Matrix
# Sample

# Input

# 3 3
# 9 9 4
# 6 6 8
# 2 1 1

# Output

# 4

# One path is:

# 1 → 2 → 6 → 9
# Code
rows, columns = map(int, input().split())

matrix = []

for row in range(rows):
    matrix.append(list(map(int, input().split())))

cells = []

for row in range(rows):
    for column in range(columns):
        cells.append([matrix[row][column], row, column])

cells.sort()

dp = [[1] * columns for row in range(rows)]

answer = 1

for cell_index in range(len(cells)):
    value = cells[cell_index][0]
    row = cells[cell_index][1]
    column = cells[cell_index][2]

    if row > 0 and matrix[row - 1][column] < value:
        dp[row][column] = max(dp[row][column], dp[row - 1][column] + 1)

    if row + 1 < rows and matrix[row + 1][column] < value:
        dp[row][column] = max(dp[row][column], dp[row + 1][column] + 1)

    if column > 0 and matrix[row][column - 1] < value:
        dp[row][column] = max(dp[row][column], dp[row][column - 1] + 1)

    if column + 1 < columns and matrix[row][column + 1] < value:
        dp[row][column] = max(dp[row][column], dp[row][column + 1] + 1)

    answer = max(answer, dp[row][column])

print(answer)


# 15. Packing Items into K Boxes

# Sample

# Input

# 5 3
# 10 20 30 40 50

# Output

# 60

# One optimal partition:

# 10 20 30
# 40
# 50

# Maximum load = 60.

# Code
n, k = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)

while low < high:
    mid = (low + high) // 2

    boxes = 1
    current_sum = 0

    for i in range(n):
        if current_sum + arr[i] <= mid:
            current_sum += arr[i]
        else:
            boxes += 1
            current_sum = arr[i]

    if boxes <= k:
        high = mid
    else:
        low = mid + 1

print(low)

# 16. Edit Distance
# Sample

# Input

# horse
# ros

# Output

# 3
# Code
s1 = input().strip()
s2 = input().strip()

if len(s1) < len(s2):
    short_string = s1
    long_string = s2
else:
    short_string = s2
    long_string = s1

previous = list(range(len(short_string) + 1))

for i in range(1, len(long_string) + 1):
    current = [i] + [0] * len(short_string)

    for j in range(1, len(short_string) + 1):
        if long_string[i - 1] == short_string[j - 1]:
            current[j] = previous[j - 1]
        else:
            insert_cost = current[j - 1] + 1
            delete_cost = previous[j] + 1
            replace_cost = previous[j - 1] + 1

            current[j] = min(insert_cost, delete_cost, replace_cost)

    previous = current

print(previous[-1])

# 17. Burst Balloons
# Sample

# Input

# 4
# 3 1 5 8

# Output

# 167
# Code
n = int(input())
arr = list(map(int, input().split()))

nums = [1] + arr + [1]
size = n + 2

dp = [[0] * size for row in range(size)]

for length in range(2, n + 2):
    for left in range(0, n + 2 - length):
        right = left + length

        for last in range(left + 1, right):
            coins = nums[left] * nums[last] * nums[right]
            coins += dp[left][last] + dp[last][right]

            dp[left][right] = max(dp[left][right], coins)

print(dp[0][n + 1])


# 18. Regular Expression Matching
# Sample

# Input

# aab
# c*a*b

# Output

# YES
# Code
s = input().strip()
p = input().strip()

n = len(s)
m = len(p)

dp = [[False] * (m + 1) for row in range(n + 1)]
dp[0][0] = True

for j in range(2, m + 1):
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        elif p[j - 1] == '*':
            dp[i][j] = dp[i][j - 2]

            if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]

if dp[n][m]:
    print("YES")
else:
    print("NO")


#19. LCS — Re-solve From Scratch
# Sample

# Input

# AGGTAB
# GXTXAYB

# Output

# 4

# One LCS is:

# GTAB
# Code
s1 = input().strip()
s2 = input().strip()

n = len(s1)
m = len(s2)

dp = [[0] * (m + 1) for row in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])

# 20. LIS — Re-solve From Scratch
# Sample

# Input

# 8
# 10 9 2 5 3 7 101 18

# Output

# 4
# Code
n = int(input())
arr = list(map(int, input().split()))

tails = []

for i in range(n):
    value = arr[i]

    left = 0
    right = len(tails)

    while left < right:
        mid = (left + right) // 2

        if tails[mid] < value:
            left = mid + 1
        else:
            right = mid

    if left == len(tails):
        tails.append(value)
    else:
        tails[left] = value

print(len(tails))