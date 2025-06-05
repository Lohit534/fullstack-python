class Human:
    eyes=2
    ears=2
    print(f"they have {eyes} eyes and {ears} ears")
class male(Human):
    hands=2
    legs=2
    print(f"they are {hands} hands and {legs} legs")
class female:
    hands=2
    legs=2
class gender(male,female):
    def add(self):
        print(f"both have hands={self.hands} and legs={self.legs}")
x=male()
y=gender()
y.add()