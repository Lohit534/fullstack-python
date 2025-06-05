import project as bank

FILENAME = "accounts.txt"

def main():
    while True:
        try:
            print("\n--- Bank Account Management ---")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Account")
            print("5. Exit")
            choice = input("Choose option (1–5): ")

            if choice == "1":
                name = input("Enter name: ")
                acc_no = input("Enter account number: ")
                acc_type = input("Enter account type (savings/current): ").lower()
                balance = float(input("Enter opening balance: "))

                if acc_type == "savings":
                    acc = bank.SavingsAccount(name, acc_no, balance)
                elif acc_type == "current":
                    acc = bank.CurrentAccount(name, acc_no, balance)
                else:
                    print("Invalid account type.")
                    continue

                with open(FILENAME, "a") as file:
                    file.write(f"{acc.name},{acc.acc_no},{acc.get_balance()},{acc_type}\n")

                print("Account created.")

            elif choice == "2":
                acc_no = input("Enter account number: ")
                found = False
                accounts = []

                with open(FILENAME, "r") as file:
                    for line in file:
                        name, ano, bal, typ = line.strip().split(",")
                        if ano == acc_no:
                            found = True
                            amt = float(input("Enter amount to deposit: "))
                            acc = bank.SavingsAccount(name, ano, float(bal)) if typ == "savings" else bank.CurrentAccount(name, ano, float(bal))
                            
                            acc.deposit(amt)
                            accounts.append(f"{acc.name},{acc.acc_no},{acc.get_balance()},{typ}\n")
                        else:
                            accounts.append(line)

                if not found:
                    print("Account not found.")
                else:
                    with open(FILENAME, "w") as file:
                        file.writelines(accounts)

            elif choice == "3":
                acc_no = input("Enter account number: ")
                found = False
                accounts = []

                with open(FILENAME, "r") as file:
                    for line in file:
                        name, ano, bal, typ = line.strip().split(",")
                        if ano == acc_no:
                            found = True
                            amt = float(input("Enter amount to withdraw: "))
                            acc = bank.SavingsAccount(name, ano, float(bal)) if typ == "savings" else bank.CurrentAccount(name, ano, float(bal))
                            
                            acc.withdraw(amt)
                            accounts.append(f"{acc.name},{acc.acc_no},{acc.get_balance()},{typ}\n")
                        else:
                            accounts.append(line)

                if not found:
                    print("Account not found.")
                else:
                    with open(FILENAME, "w") as file:
                        file.writelines(accounts)

            elif choice == "4":
                acc_no = input("Enter account number: ")
                found = False

                with open(FILENAME, "r") as file:
                    for line in file:
                        name, ano, bal, typ = line.strip().split(",")
                        if ano == acc_no:
                            found = True
                            acc = bank.SavingsAccount(name, ano, float(bal)) if typ == "savings" else bank.CurrentAccount(name, ano, float(bal))
                            acc.display()
                            break

                if not found:
                    print("Account not found.")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()