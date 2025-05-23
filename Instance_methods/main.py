
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.bredd = breed
        
    def sound(self, sound):
        print(f'{self.name} with breed of {self.bredd} creates a sound of {sound}')
        
mano = Cat('Mano', 'GermanLily')
mano.sound('Meow')