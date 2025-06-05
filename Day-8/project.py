from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance 

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display(self):
        pass

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        try:
            if amount > 0:
                self.set_balance(self.get_balance() + amount)
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        except:
            print("Error in deposit.")
        finally:
            pass

    def withdraw(self, amount):
        try:
            if 0 < amount <= self.get_balance():
                self.set_balance(self.get_balance() - amount)
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        except:
            print("Error in withdrawal.")
        finally:
            pass

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.acc_no}")
        print(f"Balance: {self.get_balance()}")
        print("Account Type: Savings")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        try:
            if amount > 0:
                self.set_balance(self.get_balance() + amount)
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        except:
            print("Error in deposit.")
        finally:
            pass

    def withdraw(self, amount):
        try:
            if amount <= self.get_balance():
                self.set_balance(self.get_balance() - amount)
                print("Withdrawal successful.")
            else:
                print("Overdraft not allowed.")
        except:
            print("Error in withdrawal.")
        finally:
            pass

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.acc_no}")
        print(f"Balance: {self.get_balance()}")
        print("Account Type: Current")