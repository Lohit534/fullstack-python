class Movie:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print(f"{self.name},{self.price}")
class a_movie:
    def change_name(self,new_name,new_price):
        self.name=new_name
        self.price=new_price
        print(f"after changing movie name and price\n{self.name},{self.price}")
a=Movie("salaar",100)
b=a_movie()
b.change_name("hit3",200)
