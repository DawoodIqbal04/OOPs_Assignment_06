
class Logger: 
    def __init__(self): # Constructor Method
        print('Welcome Back!')
        
    def __del__(self): # Destructor Method
        print('Class is destructed')
        
        
logger = Logger() # Instance Created Here
del logger # Destructed