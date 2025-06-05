file=open("./demo.txt","r")
data=file.read()
list_data=data.split("\n")
age_dict={

}
for item in list_data:
    spli_item=item.split(" ")
    age_dict[spli_item[0]]=int(spli_item[1])
print(age_dict)