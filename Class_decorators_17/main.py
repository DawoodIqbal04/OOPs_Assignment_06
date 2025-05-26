
class add_greeting:
    def __init__(self, cls):
        self.cls = cls
        
    def __call__(self, *args, **kwds):
        print(f'Hello From Decorator In {self.cls.__name__}')
        return self.cls(*args, **kwds)
        
@add_greeting
class Person:
    pass

person1 = Person()