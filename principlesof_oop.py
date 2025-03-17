#Properties/Principles of OOP.
"""Encapsulation: The bundling of data and methods within a single unit is called encapsulation.
This is achieved through the use of classes and objects.

Abstraction: The process of hiding the internal details of a class 
and showing only the necessary functionality to the user is called abstraction. 
This is achieved through the use of abstract classes and interfaces.

Inheritance: The ability of a class to acquire properties and methods from 
another class is called inheritance. This is achieved through the use of the
"extends" keyword in Java and the "class" keyword in Python.

Polymorphism: The ability of an object to take on multiple forms is called polymorphism. 
This is achieved through the use of method overriding and method overloading in Java and Python."""

#Abstraction: Something that is not clear.Helps in naming and identification of classes.Helps in defining objects without going into much details.
#Encapsolation: Ability to hide or control acess of some of the internal functionality of it's data.
#Polymorphism: An object taking on more than one form.
#Inheritance: Sub-classes can take on characteristics of the base/main class.

#Benefits of oop.
# 



class Animal():
    name ="" 
    color ="" 
    weight =""
    owner ="" 
#A method is a function within a class.
#The statements in a method are called behaviours.
    def eat(self): 
        print("Meat")   
#The statements in a method are called behaviours.
    def sound(self):
        print("I bark")   

horse = Animal()
horse.sound()
horse.eat()




