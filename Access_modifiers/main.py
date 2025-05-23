
class Employee:
    def __init__(self, name, salary, ssn): # Parametrized Constructor
        self.name = name # Public Var
        self._salary = salary # Protected Var
        self.__ssn = ssn # Private Var
        
    def salary_getter(self): # Getter Func For Salary
        print(f'Your Salary is {self._salary}')
        
    def ssn_getter(self): # Getter Func For ssn
        print(f'This is your ssn: {self.__ssn}')
        
JavedAhmad = Employee('JavedAhmad', 35000, 'emp2345') # Class Instance
print(JavedAhmad.name) # Prints The Name As It Is Public Var and Accessable Outside The Class
JavedAhmad.salary_getter() # Call This Method Wich Print Salary
JavedAhmad.ssn_getter() # Call This Method Wich Print ssn