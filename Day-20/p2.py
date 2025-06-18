n = int(input())
name_list = []

for _ in range(n):
    name = input()
    name_list.append(name)


print(name_list)
keyword = input()
fil_list = []
for name in name_list:
    if keyword.lower() in name.lower():
        fil_list.append(name)

print(fil_list)