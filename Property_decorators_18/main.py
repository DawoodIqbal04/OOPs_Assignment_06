
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        
    @property
    def price(self):
        print(f'price of {self.name} is {self.__price}')
        
    @price.setter
    def price(self, new_price):
        self.__price = new_price
        
    @price.deleter
    def price(self):
        print(f'Deleting Price of Product {self.name}')
        del self.__price
        
        
AirJordans = Product('Nike Air Jordan', 10000)

AirJordans.price

AirJordans.price = 12000

AirJordans.price

del AirJordans.price

AirJordans.price