import contacts1 as cf
#contacts = {}
try:
    print("\tContacts App")
    file=open("contacts.txt","a")
    while True:
        print("\n\nChoices :")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = int(input("Enter choice : "))
        file.write(f"{choice}")
        if choice == 1:
            cf.add_contacts()
        elif choice == 2:
            cf.view_contacts()
        elif choice == 3:
            cf.delete_contact()
        elif choice == 4:
            cf.find_contact()
        elif choice == 5:
            cf.edit_contact()
        else:
            print("Ok bye thank you!!!")
            break
except Exception as e:
    print(f"Error found:{e}")
finally:
    file.close()
    print("program excuted successfully")