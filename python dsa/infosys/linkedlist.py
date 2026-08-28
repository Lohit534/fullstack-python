#1. reverse linked list
# Input

# 5
# 1 2 3 4 5

# Output

# 5 4 3 2 1
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n = int(input())
values = list(map(int, input().split()))

head = None
tail = None

for i in range(n):
    node = Node(values[i])

    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

previous = None
current = head

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

head = previous

answer = []
current = head

while current is not None:
    answer.append(current.value)
    current = current.next

print(*answer)

#2. linked list cycle
# Input

# 4
# 3 2 0 -4
# 1

# Output

# YES
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n = int(input())
values = list(map(int, input().split()))
pos = int(input())

nodes = []

for i in range(n):
    nodes.append(Node(values[i]))

for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

if pos >= 0:
    nodes[n - 1].next = nodes[pos]

slow = nodes[0]
fast = nodes[0]

has_cycle = False

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow is fast:
        has_cycle = True
        break

if has_cycle:
    print("YES")
else:
    print("NO")

# 3. remove nth node from end in linked list
# Input

# 5
# 1 2 3 4 5
# 2

# Output

# 1 2 3 5

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

size = int(input())
values = list(map(int, input().split()))
n = int(input())

dummy = Node(0)
tail = dummy

for i in range(size):
    tail.next = Node(values[i])
    tail = tail.next

fast = dummy
slow = dummy

for i in range(n):
    fast = fast.next

while fast.next is not None:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next

answer = []
current = dummy.next

while current is not None:
    answer.append(current.value)
    current = current.next

print(*answer)

#4. merge two sorted list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n, m = map(int, input().split())
values1 = list(map(int, input().split()))
values2 = list(map(int, input().split()))

dummy = Node(0)
tail = dummy

first = None
first_tail = None

for i in range(n):
    node = Node(values1[i])

    if first is None:
        first = node
        first_tail = node
    else:
        first_tail.next = node
        first_tail = node

second = None
second_tail = None

for i in range(m):
    node = Node(values2[i])

    if second is None:
        second = node
        second_tail = node
    else:
        second_tail.next = node
        second_tail = node

left = first
right = second

while left is not None and right is not None:
    if left.value <= right.value:
        tail.next = left
        left = left.next
    else:
        tail.next = right
        right = right.next

    tail = tail.next

if left is not None:
    tail.next = left
else:
    tail.next = right

answer = []
current = dummy.next

while current is not None:
    answer.append(current.value)
    current = current.next

print(*answer)

#5. reorder list 
# Input

# 5
# 1 2 3 4 5

# Output

# 1 5 2 4 3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n = int(input())
values = list(map(int, input().split()))

head = None
tail = None

for i in range(n):
    node = Node(values[i])

    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

slow = head
fast = head

while fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next

second = slow.next
slow.next = None

previous = None
current = second

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

second = previous
first = head

while second is not None:
    first_next = first.next
    second_next = second.next

    first.next = second
    second.next = first_next

    first = first_next
    second = second_next

answer = []
current = head

while current is not None:
    answer.append(current.value)
    current = current.next

print(*answer)

