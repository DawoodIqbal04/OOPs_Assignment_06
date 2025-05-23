
from abc import ABC, abstractmethod # Importing ABC and abstractmethod

class Shape(ABC): # Abstract Base Class
    @abstractmethod # Abstract Method
    def area(self):
        pass

class Rectangle(Shape): # Inherits From Shape Class
    def __init__(self, width, height): # Constructor
        self.width = width
        self.height = height
        
    def area(self): # Method From Base Class
        return self.width * self.height
    
triangle = Rectangle(43, 23) # Created Instance
print(triangle.area()) # Calls The Abstract Method