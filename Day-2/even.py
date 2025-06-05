start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Even numbers in the range:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)