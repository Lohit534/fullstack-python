def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile

def view_contacts(contacts):
    print("\n")
    for i in contacts:
        print(f"{i} : {contacts[i]}")

def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)

def find_contact(contacts):
    query = input("Enter name to search : ")
    found = False
    for key in contacts:
        if query in key:
            print(f"{key} => {contacts[key]}")
            found = True
    if not found:
        print("Query not Found!!!")

def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " , name_to_edit)