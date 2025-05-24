class Employ:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, Employ):
        self.employ = Employ
    
        
emp1 = Employ('Dawood')

dep = Department(emp1)
print(dep.employ.name)