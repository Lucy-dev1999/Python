#Object Oriented Programming.
#Class, oject, properties(attributes, characteristics,features).
#Methods,constructors.
#Principles of oop(abstraction, encupsolation, inheritance, polymorphism).
#Overriding and overloaded.
#OOP is a paradigm that advocates for writing software based on real world objects.

#Ojects are gotten from classes or they are classified.
#We don't identifiy classes in plural hence the are singular.
#A class is a blueprint of an object while an object is an instance of a class.
#A classes defines the features, attributes, characteristics of the objects.

#The only recursive function is lambda.
#"is a" is the phrase we use to identify the class of a particular object.
#An object should fulfill the properties of the class.

students = ["Ainembabazi Lucia Rachel", "Yafi Lutalo", "Asiraf Lumu", "Nakabaale Ashima"]
student1 = {"Name": "Yafi Lutalo", "Gender": "Male", "School": "Refactory"}

print(students)
print(student1)


class laptop():
    pass 
class food():
#These are properties/characteristics etc.
    name = ""
    price = 0
    quantity = 0
    taste = ""
    value =""

#Creating objects out of the class food.
matooke = food() 
matooke.name = "Matooke"
matooke.price = 25000
matooke.quantity = 5
matooke.taste = "sweet"
matooke.value = "cabohydrates"

print(matooke.name)
print(matooke.price)
print(matooke.quantity)


