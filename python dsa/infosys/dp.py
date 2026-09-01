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