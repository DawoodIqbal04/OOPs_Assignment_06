
class Person:
    def __init__(self, name): # Constructor 
        self.name = name # Instance Var
        
class Teacher(Person): # Inherits From Class Person
    def __init__(self, name, subject):
        super().__init__(name) # Super Class Constructor Called Here
        self.subject = subject # Instance Var of Class Teacher
        print(f'Miss {self.name}`s Subject is {self.subject}')
        
Lina = Teacher('Lina', 'Maths') # Instance Created Here