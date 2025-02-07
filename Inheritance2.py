class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def Sound(self):
        print(f'{self.name} Woofs')
    def legs(self):
        return print("4")

class Hen(Animal):
    def Sound(self):
        print(f'{self.name} Quacks')
    def legs(self):
        print("2")

D = Dog('Snoopy')
D.Sound()
D.legs()

H = Hen('Lucy')
H.Sound()
H.legs()