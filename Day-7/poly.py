class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()  # Polymorphism in action
#Polymorphism is an essential concept in Object-Oriented Programming that means "many forms". It allows objects of different classes to respond to the same method in different ways.