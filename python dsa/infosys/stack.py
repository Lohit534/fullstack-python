#1. next greater element 1Input

# 3 4
# 4 1 2
# 1 3 4 2

# Output

# -1 3 -1

n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

stack = []
next_greater = {}

for i in range(m):
    value = nums2[i]

    while stack and stack[-1] < value:
        previous = stack.pop()
        next_greater[previous] = value

    stack.append(value)

for i in range(len(stack)):
    next_greater[stack[i]] = -1

answer = []

for i in range(n):
    answer.append(next_greater[nums1[i]])

print(*answer)

#2. valid paranthesis
# Input

# {[()]}

# Output

# YES
s = input().strip()

stack = []
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

valid = True

for i in range(len(s)):
    ch = s[i]

    if ch == '(' or ch == '[' or ch == '{':
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs.get(ch):
            valid = False
            break
        stack.pop()

if stack:
    valid = False

if valid:
    print("YES")
else:
    print("NO")

#3. min stack
# Input

# 7
# push 5
# push 2
# push 3
# getMin
# pop
# getMin
# top

# Output

# 2
# 2
# 2
q = int(input())

stack = []
minimum = []

for i in range(q):
    operation = input().split()

    if operation[0] == "push":
        value = int(operation[1])
        stack.append(value)

        if not minimum or value <= minimum[-1]:
            minimum.append(value)
        else:
            minimum.append(minimum[-1])

    elif operation[0] == "pop":
        stack.pop()
        minimum.pop()

    elif operation[0] == "top":
        print(stack[-1])

    elif operation[0] == "getMin":
        print(minimum[-1])


#4. daily temperatures
# Input

# 8
# 73 74 75 71 69 72 76 73

# Output

# 1 1 4 2 1 1 0 0

n = int(input())
temperatures = list(map(int, input().split()))

answer = [0] * n
stack = []

for i in range(n):
    while stack and temperatures[stack[-1]] < temperatures[i]:
        previous = stack.pop()
        answer[previous] = i - previous

    stack.append(i)

print(*answer)

#5 evaluate reverse polish notation
# Input

# 5
# 2 1 + 3 *

# Output

# 9

# Because:

# (2 + 1) * 3 = 9
n = int(input())
tokens = input().split()

stack = []

for i in range(n):
    token = tokens[i]

    if token == "+":
        second = stack.pop()
        first = stack.pop()
        stack.append(first + second)

    elif token == "-":
        second = stack.pop()
        first = stack.pop()
        stack.append(first - second)

    elif token == "*":
        second = stack.pop()
        first = stack.pop()
        stack.append(first * second)

    elif token == "/":
        second = stack.pop()
        first = stack.pop()

        value = abs(first) // abs(second)

        if (first < 0) != (second < 0):
            value = -value

        stack.append(value)

    else:
        stack.append(int(token))

print(stack[-1])