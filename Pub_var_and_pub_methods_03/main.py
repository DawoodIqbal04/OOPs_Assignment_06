
class Car:
    brand = 'Honda' # Public Class Variable

    def __init__(self, model):
        self.model = model # Public Instance Variable

    def start(self): # Method for Calling Public Variables
        print(f'Your {self.brand} {self.model} is starting.....')

car1 = Car('Civic')
car1.start() # Calls the Start Method