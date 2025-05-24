
class Engine:
    
    def start_engine(self):
        print('Engine is started!')
        
class Car:
    car_engine = Engine()
    
    def start_car(self):
        self.car_engine.start_engine()
        
ToyotaVigo = Car()
ToyotaVigo.start_car()