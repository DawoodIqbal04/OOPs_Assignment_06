
class Temprature_convertor:
    @staticmethod
    def celsius_to_fahrenheit(C):
        F = (9/5) * C + 32
        print(f'{C} Celsius to Fahrenheit is equals to {F}')
        
temp = Temprature_convertor()
temp.celsius_to_fahrenheit(44)
temp.celsius_to_fahrenheit(79.5)