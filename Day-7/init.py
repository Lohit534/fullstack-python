class vechile:
    name="suzuki"
    price=200
    print(f"{name},{price}")
class Bike(vechile):
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print(f"{self.name},{self.price}")
x=Bike("honda",8726)

        