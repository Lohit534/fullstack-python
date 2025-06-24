n=int(input())
#hallow rectangle
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#rev z pattern
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print(" " * i + "*")

#Box-x pattern


for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print("*", end="") 
        elif j == 0 or j == n-1:
            print("*", end="")  
        elif j == i or j == n - i - 1:
            print("*", end="")  
        else:
            print(" ", end="")  
    print()

#Z pattern
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()