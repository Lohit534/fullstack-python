# 1. Grid of Stars with Dashes
r=13
c=3
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j!=c-1:
            print("-",end="")
    print()

# 2. Hollow Square/Rectangle Pattern
r=5
c=5
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
        if j!=c-1:
            print(" ",end="")
    print()

# 3. Rhombus / Left-Leaning Parallelogram
r=3
c=6
r1=c-1
for i in range(c):
    for j in range(r1-i):
        print("-",end="")
    for k in range(r):
        print("*",end="")
    print()

# 4. Rhombus / Right-Leaning Parallelogram
r=3
c=6
r1=c-1
for i in range(c):
    for j in range(i):
        print("-",end="")
    for k in range(r):
        print("*",end="")
    print()

# 5. Solid Pyramid Pattern
r=5
n=r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()

# 6. Inverted Solid Pyramid Pattern
r=5
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(2*r-1-(2*i)):
        print("*",end="")
    print()

# 7. Solid Diamond Pattern
r=5
n=r-1
for i in range(r-1):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()

# 8. Solid Hourglass Pattern
r=5
n=r-1
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()
for i in range(1,r):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()

# 9. Hollow Pyramid Pattern
r=5
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# 10. Inverted Hollow Pyramid Pattern
r=5
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# 11. Hollow Diamond Pattern
r=5
for i in range(r-1):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# 12. Right-Angled Number Triangle
r=6
for i in range(r):
    for j in range(1,i+2):
        print(j,end="")
    print()

# 13. Inverted Right-Angled Number Triangle (Right-Aligned)
r=6
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    print()

# 14. Palindromic Number Pyramid Triangle
r=6
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    for j in range(2,i+2):
        print(j,end="")
    print()