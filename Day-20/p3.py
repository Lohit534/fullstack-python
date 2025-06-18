user_list = [{'name': 'Ram', 'id': 1}, {'name': 'Jas', 'id': 2}]

n = int(input()) 

for i in range(n):
    user_dict = {} 
    user_dict["name"] = input()
    user_dict["id"] = int(input())
    user_list.append(user_dict) 
print(user_list)

search = input()
filter_list = []
for i in user_list:
    if search.lower() in i["name"].lower():
        filter_list.append(i)

print(filter_list)
