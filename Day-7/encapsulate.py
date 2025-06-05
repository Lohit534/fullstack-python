class bank:
    def check_balance1(self):
        self.__balance=100
        self.name="lohit"
        print(f"{self.__balance},{self.name}")
class Bank:
    def check_balance2(self,bal,name):
        self.__balance=bal
        self.name=name
        print(f"{self.__balance},{self.name}")

b=bank()
b.check_balance1()
c=Bank()
c.check_balance2(1000,"abhi")
b.self.__balance()
'''It refers to the **bundling of data and methods** that operate on that data within a single unit or class, and **restricting access** to some of the object’s components.

It is a way to **hide the internal details** of how an object works and only expose what’s necessary. This helps **protect the data from accidental modification** and improves **security and maintainability**.

---

### 🔐 **What Are Private Variables?**

In Python, we can make an attribute "private" by **prefixing it with two underscores (`__`)**. This means it can't be accessed directly from outside the class.
'''