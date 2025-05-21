
class MathUtils:

    @staticmethod
    def sum(a, b): # Static Method That Havenot Access of Class Vars Neither Instance Vars
        first_digit = a # Static variables
        second_digit = b # Static Variables
        return print(first_digit + second_digit) # Reurn Sum of Vars
    
maths = MathUtils() # Instance Created
maths.sum(4, 5) # Called Sum Static Method