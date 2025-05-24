
class A:
    def show(self):
        print('This Is Class A')
        
class B(A):
    def show(self):
        print('This Is Class B')
        
class C(A):
    def show(self):
        print('This Is Class C')
        
class D(B, C):
    pass

d = D()
print(D.mro())
d.show()
