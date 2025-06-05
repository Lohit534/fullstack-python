class Student:
    name=""
    rollno=0
    def display(self,na,roll):
        self.name=na
        self.rollno=roll
        print(f"name is:{self.name}, and rollnum is:{self.rollno}")
a=Student()
a.display("Lohit",34)