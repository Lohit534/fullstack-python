# 1. Generate multiplication table
n=int(input())
if 2<=n<=20:
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


# 2. Print reverse of a string
n=int(input())
for i in range(n):
    i=input()
    print(i[::-1])

# 3. Check whether a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    if n == 1:
        return 2
    count = 1
    num = 3
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 2

T = int(input())
for _ in range(T):
    N = int(input())
    print(nth_prime(N))

# 4. Find the Nth term of the Fibonacci Series
def fibonacci_series(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for _ in range(2, n):
            c = a + b
            print(c)
            a, b = b, c
try:
    num_terms = int(input())
    fibonacci_series(num_terms)
except ValueError:
    print("Invalid input. Please enter an integer.")

