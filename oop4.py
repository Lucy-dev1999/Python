class Fruit:
    def __init__(self, name, color, taste, size):
        self.fruitname = name
        self.fruitcolor = color
        self.fruittaste = taste
        self.fruitsize = size

banana = Fruit("banana", "yellow", "sweet", "small")
apple = Fruit("apple", "red", "sweet", "small")
orange = Fruit("orange", "green", "sweet", "big")

###################################################

class Animal:
    def __init__(self, name, size, breed, color, age):
        self.name = name
        self.size = size
        self.breed = breed
        self.color = color
        self.age = age 

    def details(self):
        print(f"name:{self.name}\n size:{self.size}\n breed:{self.breed}\n color:{self.color}\n age:{self.age}\n")
#How to achieve inheritance: meaning here the dog will be able to take one the properties of the class animal.
#This class Dog has 2 methods: the sound and the details.
class Dog(Animal):
    def sound(self):
        print("dog woofs")

dog = Dog("max", "small", "german shepherd", "brown", "2years")
dog.details()

        




