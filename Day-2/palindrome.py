def is_palindrome(n):
    return str(n) == str(n)[::-1]
def sum_palindromes(n):
    sum_of_palindromes = 0
    for i in range(n + 1):
        if is_palindrome(i):
            sum_of_palindromes += i
    return sum_of_palindromes
while True:
    try:
        num = int(input())
        if num == 0:
            break
        print(sum_palindromes(num))
    except ValueError:
        break

'''
num = 121
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''