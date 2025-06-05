def add_contacts():
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name}:{number}\n")
    print("Contact added.")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            data = file.read()
            print(data if data else "No contacts found.")
    except FileNotFoundError:
        print("No file found.")

def edit_contact():
    try:
        name = input("Enter name to edit: ")
        lines = []
        updated = False
        with open("contacts", "r") as file:
            lines = file.readlines()
        with open("contacts", "w") as file:
            for line in lines:
                n, p = line.strip().split(",")
                if n == name:
                    new_phone = input("Enter new phone: ")
                    file.write(f"{name},{new_phone}\n")
                    updated = True
                else:
                    file.write(line)
        if updated:
            print("Contact updated.")
        else:
            print("Contact not found.")
    except Exception as e:
        print("Error:", e)
    

def delete_contact():
    try:
        name = input("Enter name to delete: ")
        lines = []
        found = False
        with open("contacts", "r") as file:
            lines = file.readlines()
        with open("contacts", "w") as file:
            for line in lines:
                n, p = line.strip().split(",")
                if n != name:
                    file.write(line)
                else:
                    found = True
        if found:
            print("Contact deleted.")
        else:
            print("Contact not found.")
    except Exception as e:
        print("Error:", e)

def find_contact():
    try:
        name = input("Enter name to search: ")
        found = False
        with open("contacts", "r") as file:
            for line in file:
                n, p = line.strip().split(",")
                if n == name:
                    print(f"{name} : {p}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except Exception as e:
        print("Error:", e)