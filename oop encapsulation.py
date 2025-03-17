class House():
    def __init__(self, color, type, size):
        self.color = color
        #Any property of a class that starts with an underscore is a private property.
        self._type = type
        self.size = size
    
    def house_cleaning(self):
        print(f"type {self._type} needs to be cleaned twice a week")
house1 = House("green", "bangalow", 'medium')  
print(house1._type)  

#Direct inheritance
#Indirect inheritance

    
