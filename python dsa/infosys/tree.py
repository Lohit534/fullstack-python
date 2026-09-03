# 1. Maximum Depth of Binary Tree
# Input

# 7
# 3 9 20 N N 15 7

# Output

# 3
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()

if not values or values[0] == "N":
    print(0)
else:
    root = Node(int(values[0]))
    queue = [root]
    index = 0
    value_index = 1

    while index < len(queue) and value_index < len(values):
        node = queue[index]
        index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.left = Node(int(values[value_index]))
            queue.append(node.left)
        value_index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.right = Node(int(values[value_index]))
            queue.append(node.right)
        value_index += 1

    queue = [(root, 1)]
    index = 0
    answer = 0

    while index < len(queue):
        node, depth = queue[index]
        index += 1
        answer = max(answer, depth)

        if node.left:
            queue.append((node.left, depth + 1))

        if node.right:
            queue.append((node.right, depth + 1))

    print(answer)



# 2. Binary Tree Level Order Traversal
# Input

# 7
# 3 9 20 N N 15 7

# Output

# 3
# 9 20
# 15 7
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()

if not values or values[0] == "N":
    print()
else:
    root = Node(int(values[0]))
    queue = [root]
    index = 0
    value_index = 1

    while index < len(queue) and value_index < len(values):
        node = queue[index]
        index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.left = Node(int(values[value_index]))
            queue.append(node.left)
        value_index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.right = Node(int(values[value_index]))
            queue.append(node.right)
        value_index += 1

    queue = [root]
    index = 0

    while index < len(queue):
        level_size = len(queue) - index
        level = []

        count = 0
        while count < level_size:
            node = queue[index]
            index += 1
            level.append(str(node.value))

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            count += 1

        print(" ".join(level))



# 3. Validate Binary Search Tree
# Input

# 7
# 5 3 7 2 4 6 8

# Output

# YES
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()

if not values or values[0] == "N":
    print("YES")
else:
    root = Node(int(values[0]))
    queue = [root]
    index = 0
    value_index = 1

    while index < len(queue) and value_index < len(values):
        node = queue[index]
        index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.left = Node(int(values[value_index]))
            queue.append(node.left)
        value_index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.right = Node(int(values[value_index]))
            queue.append(node.right)
        value_index += 1

    stack = [(root, None, None)]
    valid = True

    while stack:
        node, low, high = stack.pop()

        if low is not None and node.value <= low:
            valid = False
            break

        if high is not None and node.value >= high:
            valid = False
            break

        if node.right:
            stack.append((node.right, node.value, high))

        if node.left:
            stack.append((node.left, low, node.value))

    if valid:
        print("YES")
    else:
        print("NO")



# 4. Lowest Common Ancestor of BST
# Input

# 7
# 6 2 8 0 4 7 9
# 2 8

# Output

# 6
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()
p, q = map(int, input().split())

root = Node(int(values[0]))
queue = [root]
index = 0
value_index = 1

while index < len(queue) and value_index < len(values):
    node = queue[index]
    index += 1

    if value_index < len(values) and values[value_index] != "N":
        node.left = Node(int(values[value_index]))
        queue.append(node.left)
    value_index += 1

    if value_index < len(values) and values[value_index] != "N":
        node.right = Node(int(values[value_index]))
        queue.append(node.right)
    value_index += 1

current = root

while current:
    if p < current.value and q < current.value:
        current = current.left
    elif p > current.value and q > current.value:
        current = current.right
    else:
        print(current.value)
        break


# 5. Diameter of Binary Tree
# Input

# 5
# 1 2 3 4 5

# Output

# 3

# Path can be:

# 4 -> 2 -> 1 -> 3
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()

if not values or values[0] == "N":
    print(0)
else:
    root = Node(int(values[0]))
    queue = [root]
    index = 0
    value_index = 1

    while index < len(queue) and value_index < len(values):
        node = queue[index]
        index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.left = Node(int(values[value_index]))
            queue.append(node.left)
        value_index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.right = Node(int(values[value_index]))
            queue.append(node.right)
        value_index += 1

    stack = [(root, False)]
    height = {}
    diameter = 0

    while stack:
        node, visited = stack.pop()

        if visited:
            left_height = height.get(node.left, 0)
            right_height = height.get(node.right, 0)

            height[node] = 1 + max(left_height, right_height)
            diameter = max(diameter, left_height + right_height)
        else:
            stack.append((node, True))

            if node.right:
                stack.append((node.right, False))

            if node.left:
                stack.append((node.left, False))

    print(diameter)


# 6. Invert Binary Tree
# Input

# 7
# 4 2 7 1 3 6 9

# Output

# 4 7 2 9 6 3 1
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()

if not values or values[0] == "N":
    print()
else:
    root = Node(int(values[0]))
    queue = [root]
    index = 0
    value_index = 1

    while index < len(queue) and value_index < len(values):
        node = queue[index]
        index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.left = Node(int(values[value_index]))
            queue.append(node.left)
        value_index += 1

        if value_index < len(values) and values[value_index] != "N":
            node.right = Node(int(values[value_index]))
            queue.append(node.right)
        value_index += 1

    queue = [root]
    index = 0

    while index < len(queue):
        node = queue[index]
        index += 1

        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    result = []
    queue = [root]
    index = 0

    while index < len(queue):
        node = queue[index]
        index += 1

        if node:
            result.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("N")

    while result and result[-1] == "N":
        result.pop()

    print(" ".join(result))


# 7. Kth Smallest Element in BST
# Input

# 5
# 3 1 4 N 2
# 1

# Output

# 1
# Python 3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = int(input())
values = input().split()
k = int(input())

root = Node(int(values[0]))
queue = [root]
index = 0
value_index = 1

while index < len(queue) and value_index < len(values):
    node = queue[index]
    index += 1

    if value_index < len(values) and values[value_index] != "N":
        node.left = Node(int(values[value_index]))
        queue.append(node.left)
    value_index += 1

    if value_index < len(values) and values[value_index] != "N":
        node.right = Node(int(values[value_index]))
        queue.append(node.right)
    value_index += 1

stack = []
current = root
count = 0

while current or stack:
    while current:
        stack.append(current)
        current = current.left

    current = stack.pop()
    count += 1

    if count == k:
        print(current.value)
        break

    current = current.right


# 8. Word Ladder
# Input

# hit cog
# 6
# hot dot dog lot log cog

# Output

# 5

# Transformation:

# hit -> hot -> dot -> dog -> cog
# Python 3
begin_word, end_word = input().split()
n = int(input())
words = input().split()

word_set = set(words)

if end_word not in word_set:
    print(0)
else:
    queue = [(begin_word, 1)]
    index = 0
    visited = {begin_word}
    answer = 0

    while index < len(queue):
        word, steps = queue[index]
        index += 1

        if word == end_word:
            answer = steps
            break

        position = 0

        while position < len(word):
            code = ord('a')

            while code <= ord('z'):
                character = chr(code)

                if character != word[position]:
                    new_word = word[:position] + character + word[position + 1:]

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))

                code += 1

            position += 1

    print(answer)


# 9. Graph Valid Tree
# Input

# 5 4
# 0 1
# 0 2
# 0 3
# 1 4

# Output

# YES
# Python 3
n, m = map(int, input().split())

graph = [[] for i in range(n)]

edge = 0
while edge < m:
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    edge += 1

if m != n - 1:
    print("NO")
else:
    visited = [False] * n
    stack = [0]
    visited[0] = True
    count = 0

    while stack:
        node = stack.pop()
        count += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    if count == n:
        print("YES")
    else:
        print("NO")


# 10. Network Delay Time — Dijkstra
# Input

# 4 3 2
# 2 1 1
# 2 3 1
# 3 4 1

# Output

# 2
# Python 3 — Manual Min Heap

# Because you asked for no imports, this implementation does not use heapq.

def push(heap, item):
    heap.append(item)
    index = len(heap) - 1

    while index > 0:
        parent = (index - 1) // 2

        if heap[parent][0] <= heap[index][0]:
            break

        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent

def pop(heap):
    smallest = heap[0]
    last = heap.pop()

    if heap:
        heap[0] = last
        index = 0

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest_index = index

            if left < len(heap) and heap[left][0] < heap[smallest_index][0]:
                smallest_index = left

            if right < len(heap) and heap[right][0] < heap[smallest_index][0]:
                smallest_index = right

            if smallest_index == index:
                break

            heap[index], heap[smallest_index] = heap[smallest_index], heap[index]
            index = smallest_index

    return smallest

n, m, k = map(int, input().split())

graph = [[] for i in range(n + 1)]

edge = 0
while edge < m:
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    edge += 1

infinity = 10 ** 30
distance = [infinity] * (n + 1)
distance[k] = 0

heap = []
push(heap, (0, k))

while heap:
    current_distance, node = pop(heap)

    if current_distance != distance[node]:
        continue

    for neighbor, weight in graph[node]:
        new_distance = current_distance + weight

        if new_distance < distance[neighbor]:
            distance[neighbor] = new_distance
            push(heap, (new_distance, neighbor))

answer = 0

node = 1
while node <= n:
    if distance[node] == infinity:
        answer = -1
        break

    answer = max(answer, distance[node])
    node += 1

print(answer)