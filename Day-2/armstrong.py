def is_armstrong(num):
    s_num = str(num)
    n = len(s_num)
    sum_of_powers = sum(int(digit) ** n for digit in s_num)
    return num == sum_of_powers
T = int(input())
for _ in range(T):
    N = int(input())
    if is_armstrong(N):
        print("Yes")
    else:
        print("No")

'''num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")'''
