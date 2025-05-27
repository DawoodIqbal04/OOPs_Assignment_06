
class MultiPlier:
    def __init__(self):
        self.factor = 12
        
    def __call__(self):
        self.input = int(input('Choose a number: '))
        self.answer = self.factor / self.input
        print(f'{self.input} / {self.factor} = {self.answer}')
        
        
obj = MultiPlier()
obj()