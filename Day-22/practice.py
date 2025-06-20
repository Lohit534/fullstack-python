#minimum no.of coins

T = int(input())
for _ in range(T):
    X = int(input())
    remainder = X % 10
    print(remainder)

#bob at the bank

T = int(input())
for _ in range(T):
    W, X, Y, Z = map(int, input().split())
    final_balance = W + (X - Y) * ZT = int(input())
    print(final_balance)

#first and last digit

T = int(input())
for _ in range(T):
    N = input().strip()
    first_digit = int(N[0])
    last_digit = int(N[-1])
    print(first_digit + last_digit)

#bin
T = int(input())
for _ in range(T):
    N = int(input())
    binary_sum = bin(N).count('1')
    if binary_sum % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

#super_reduced_string
def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack) if stack else "Empty String"

#strongest password

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    has_digit = any(c in numbers for c in password)
    has_lower = any(c in lower_case for c in password)
    has_upper = any(c in upper_case for c in password)
    has_special = any(c in special_characters for c in password)
    
    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1
    
    return max(missing_types, 6 - n)


#missing numbers
def missingNumbers(arr, brr):
    from collections import Counter
    
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    
    missing = []
    for num in count_brr:
        if count_brr[num] > count_arr.get(num, 0):
            missing.append(num)
    
    return sorted(missing)

#number of pairs of array
def pairs(k, arr):
    nums = set(arr)
    count = 0
    for num in arr:
        if num + k in nums:
            count += 1
    return count

#arrays and strings practice problems
# 1. Minimum Cost to Move Chips to The Same Position
def minCostToMoveChips(position):
    even = sum(p % 2 == 0 for p in position)
    return min(even, len(position) - even)

# 2. Check If It Is a Straight Line
def checkStraightLine(coordinates):
    (x0, y0), (x1, y1) = coordinates[:2]
    for x, y in coordinates[2:]:
        if (x1 - x0)*(y - y0) != (x - x0)*(y1 - y0):
            return False
    return True

# 3. Average Value of Even Numbers That Are Divisible by Three
def averageValue(nums):
    values = [n for n in nums if n % 6 == 0]
    return sum(values) // len(values) if values else 0

# 4. Difference Between Element Sum and Digit Sum of an Array
def differenceOfSum(nums):
    return sum(nums) - sum(int(d) for n in nums for d in str(n))

# 5. Number of Good Pairs
def numIdenticalPairs(nums):
    from collections import Counter
    count = Counter(nums)
    return sum(v * (v - 1) // 2 for v in count.values())

# 6. Single Number
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# 7. Missing Number
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

# 8. Sign of the Product of an Array
def arraySign(nums):
    sign = 1
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            sign *= -1
    return sign

# 9. Convert the Temperature
def convertTemperature(celsius):
    return [celsius + 273.15, celsius * 1.80 + 32.00]

# 10. Two Sum
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# 11. Excel Sheet Column Number
def titleToNumber(columnTitle):
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

# 12. Excel Sheet Column Title
def convertToTitle(columnNumber):
    result = []
    while columnNumber:
        columnNumber -= 1
        result.append(chr(columnNumber % 26 + 65))
        columnNumber //= 26
    return ''.join(reversed(result))

# 13. Convert a Number to Hexadecimal
def toHex(num):
    if num == 0:
        return "0"
    hex_chars = '0123456789abcdef'
    result = []
    num &= 0xFFFFFFFF
    while num:
        result.append(hex_chars[num % 16])
        num //= 16
    return ''.join(reversed(result))

# 14. Add Strings
def addStrings(num1, num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        carry, digit = divmod(n1 + n2 + carry, 10)
        result.append(str(digit))
        i -= 1
        j -= 1
    return ''.join(reversed(result))

# 15. Alternating Digit Sum
def alternateDigitSum(n):
    s = str(n)
    return sum(int(d) if i % 2 == 0 else -int(d) for i, d in enumerate(s))

# 16. Find the K-th Character in String Game I
def kthCharacter(s, k):
    return s[(k - 1) % len(s)]

# 17. Type of Triangle
def triangleType(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not A Triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

# 18. Find the Difference
def findTheDifference(s, t):
    from collections import Counter
    return (Counter(t) - Counter(s)).most_common(1)[0][0]

# 19. Maximum Odd Binary Number
def maximumOddBinaryNumber(s):
    ones = s.count('1')
    zeros = len(s) - ones
    return '1' * (ones - 1) + '0' * zeros + '1'

# 20. Count the Number of Consistent Strings
def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)
    return sum(set(word).issubset(allowed_set) for word in words)

# 21. Categorize Box According to Criteria
def categorizeBox(length, width, height, mass):
    bulky = (length * width * height >= 10**9 or 
             max(length, width, height) >= 10**4)
    heavy = mass >= 100
    if bulky and heavy:
        return "Both"
    if bulky:
        return "Bulky"
    if heavy:
        return "Heavy"
    return "Neither"

# 22. First Letter to Appear Twice
def repeatedCharacter(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)

# 23. Determine Color of a Chessboard Square
def squareIsWhite(coordinates):
    return (ord(coordinates[0]) + int(coordinates[1])) % 2 != 0

# 24. Check if Two Chessboard Squares Have the Same Color
def sameColor(c1, c2):
    def parity(c): return (ord(c[0]) + int(c[1])) % 2
    return parity(c1) == parity(c2)

# 25. Largest Odd Number in String
def largestOddNumber(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2:
            return num[:i+1]
    return ""

# 26. Find the Winning Player in Coin Game
def findWinner(coins):
    return "Player1" if sum(coins) % 2 else "Player2"