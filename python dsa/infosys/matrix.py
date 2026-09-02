# 1. Number of Islands
# Sample

# Input

# 4 5
# 1 1 0 0 0
# 1 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 1

# Output

# 3
# Code
rows, columns = map(int, input().split())

grid = []

for row in range(rows):
    grid.append(list(map(int, input().split())))

islands = 0

for row in range(rows):
    for column in range(columns):
        if grid[row][column] == 1:
            islands += 1

            stack = [[row, column]]
            grid[row][column] = 0

            while stack:
                current_row, current_column = stack.pop()

                if current_row > 0 and grid[current_row - 1][current_column] == 1:
                    grid[current_row - 1][current_column] = 0
                    stack.append([current_row - 1, current_column])

                if current_row + 1 < rows and grid[current_row + 1][current_column] == 1:
                    grid[current_row + 1][current_column] = 0
                    stack.append([current_row + 1, current_column])

                if current_column > 0 and grid[current_row][current_column - 1] == 1:
                    grid[current_row][current_column - 1] = 0
                    stack.append([current_row, current_column - 1])

                if current_column + 1 < columns and grid[current_row][current_column + 1] == 1:
                    grid[current_row][current_column + 1] = 0
                    stack.append([current_row, current_column + 1])

print(islands)

# 2. Search a 2D Matrix


# Sample

# Input

# 3 4
# 1 3 5 7
# 10 11 16 20
# 23 30 34 60
# 16

# Output

# YES
# Code
rows, columns = map(int, input().split())

matrix = []

for row in range(rows):
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


# 3. Longest Increasing Path in a Matrix


# Sample

# Input

# 3 3
# 9 9 4
# 6 6 8
# 2 1 1

# Output

# 4
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

for index in range(len(cells)):
    value = cells[index][0]
    row = cells[index][1]
    column = cells[index][2]

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


# 4. Spiral Matrix
# Sample

# Input

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output

# 1 2 3 6 9 8 7 4 5
# Code
rows, columns = map(int, input().split())

matrix = []

for row in range(rows):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = rows - 1
left = 0
right = columns - 1

answer = []

while top <= bottom and left <= right:
    for column in range(left, right + 1):
        answer.append(matrix[top][column])

    top += 1

    for row in range(top, bottom + 1):
        answer.append(matrix[row][right])

    right -= 1

    if top <= bottom:
        for column in range(right, left - 1, -1):
            answer.append(matrix[bottom][column])

        bottom -= 1

    if left <= right:
        for row in range(bottom, top - 1, -1):
            answer.append(matrix[row][left])

        left += 1

print(*answer)


# 5. Rotate Image
# Sample

# Input

# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output

# 7 4 1
# 8 5 2
# 9 6 3
# Code
n = int(input())

matrix = []

for row in range(n):
    matrix.append(list(map(int, input().split())))

for row in range(n):
    for column in range(row + 1, n):
        matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

for row in range(n):
    left = 0
    right = n - 1

    while left < right:
        matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
        left += 1
        right -= 1

for row in range(n):
    print(*matrix[row])


# 6. Set Matrix Zeroes


# Sample

# Input

# 3 3
# 1 1 1
# 1 0 1
# 1 1 1

# Output

# 1 0 1
# 0 0 0
# 1 0 1
# Code
rows, columns = map(int, input().split())

matrix = []

for row in range(rows):
    matrix.append(list(map(int, input().split())))

first_row_zero = False
first_column_zero = False

for column in range(columns):
    if matrix[0][column] == 0:
        first_row_zero = True
        break

for row in range(rows):
    if matrix[row][0] == 0:
        first_column_zero = True
        break

for row in range(1, rows):
    for column in range(1, columns):
        if matrix[row][column] == 0:
            matrix[row][0] = 0
            matrix[0][column] = 0

for row in range(1, rows):
    for column in range(1, columns):
        if matrix[row][0] == 0 or matrix[0][column] == 0:
            matrix[row][column] = 0

if first_row_zero:
    for column in range(columns):
        matrix[0][column] = 0

if first_column_zero:
    for row in range(rows):
        matrix[row][0] = 0

for row in range(rows):
    print(*matrix[row])


# 7. Max Area of Island

# Input

# 4 5
# 0 0 1 0 0
# 1 1 1 0 1
# 0 1 0 0 1
# 0 0 0 1 1

# Output

# 5
# Code
rows, columns = map(int, input().split())

grid = []

for row in range(rows):
    grid.append(list(map(int, input().split())))

maximum_area = 0

for row in range(rows):
    for column in range(columns):
        if grid[row][column] == 1:
            stack = [[row, column]]
            grid[row][column] = 0
            area = 0

            while stack:
                current_row, current_column = stack.pop()
                area += 1

                if current_row > 0 and grid[current_row - 1][current_column] == 1:
                    grid[current_row - 1][current_column] = 0
                    stack.append([current_row - 1, current_column])

                if current_row + 1 < rows and grid[current_row + 1][current_column] == 1:
                    grid[current_row + 1][current_column] = 0
                    stack.append([current_row + 1, current_column])

                if current_column > 0 and grid[current_row][current_column - 1] == 1:
                    grid[current_row][current_column - 1] = 0
                    stack.append([current_row, current_column - 1])

                if current_column + 1 < columns and grid[current_row][current_column + 1] == 1:
                    grid[current_row][current_column + 1] = 0
                    stack.append([current_row, current_column + 1])

            maximum_area = max(maximum_area, area)

print(maximum_area)