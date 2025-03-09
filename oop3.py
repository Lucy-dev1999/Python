#How you declare a class under encapsulation.
#This is a dynamic method.
class Animal():
#"init" is a constractor and always defined by two undersores on each side.
#"init" is used to initialise/give values to an object of the class.
#Self (the first parameter)is used to identify the properties of the class.
#The other parameters are the properties of the class.
    def __init__(self,name, size, color,sound ):
        self.animalname = name
        self.animalsize = size
        self.animalcolor = color
        self.animalsound = sound
cow = Animal("cow","medium","red","moowing")
cat = Animal("cat","small","black and white","meowing")
dog = Animal("dog","big","brown","barking")




        