# 1. Course Schedule
# Sample

# Input

# 2 1
# 1 0

# Output

# YES
# Code
n, m = map(int, input().split())

graph = [[] for course in range(n)]
indegree = [0] * n

for edge in range(m):
    course, prerequisite = map(int, input().split())
    graph[prerequisite].append(course)
    indegree[course] += 1

queue = []

for course in range(n):
    if indegree[course] == 0:
        queue.append(course)

front = 0
completed = 0

while front < len(queue):
    current = queue[front]
    front += 1
    completed += 1

    for index in range(len(graph[current])):
        next_course = graph[current][index]
        indegree[next_course] -= 1

        if indegree[next_course] == 0:
            queue.append(next_course)

if completed == n:
    print("YES")
else:
    print("NO")


# 2. Course Schedule II
# Sample

# Input

# 4 4
# 1 0
# 2 0
# 3 1
# 3 2

# Output

# 0 1 2 3

# Another valid order can also exist.

# Code
n, m = map(int, input().split())

graph = [[] for course in range(n)]
indegree = [0] * n

for edge in range(m):
    course, prerequisite = map(int, input().split())
    graph[prerequisite].append(course)
    indegree[course] += 1

queue = []

for course in range(n):
    if indegree[course] == 0:
        queue.append(course)

front = 0
order = []

while front < len(queue):
    current = queue[front]
    front += 1

    order.append(current)

    for index in range(len(graph[current])):
        next_course = graph[current][index]
        indegree[next_course] -= 1

        if indegree[next_course] == 0:
            queue.append(next_course)

if len(order) == n:
    print(*order)
else:
    print(-1)


# 3. Number of Connected Components


# Sample

# Input

# 5 3
# 0 1
# 1 2
# 3 4

# Output

# 2
# Code
n, m = map(int, input().split())

graph = [[] for vertex in range(n)]

for edge in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
components = 0

for vertex in range(n):
    if not visited[vertex]:
        components += 1

        stack = [vertex]
        visited[vertex] = True

        while stack:
            current = stack.pop()

            for index in range(len(graph[current])):
                neighbor = graph[current][index]

                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

print(components)