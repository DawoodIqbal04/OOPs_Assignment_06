
class Student:
    # Constructor Function
    def __init__(self, name, marks):
        self.name = name # Instance Attributes
        self.marks = marks # Instance Attributes
        self.attendance = '95%' # Instance Attributes

    # Instance Method
    def display_info(self):
        return print(f'Student {self.name} with marks: {self.marks} has attendance of {self.attendance}')
    
Dawood = Student('Dawood', 99) # Creating Class Instance
Dawood.display_info() # Display Info of Student

Suleman = Student('Suleman', 78)
Suleman.attendance = '89%' # Modifying Instance Attributes
Suleman.display_info()