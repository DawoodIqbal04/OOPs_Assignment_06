
def log_function_call(func):
    def wrapper():
        print('Function Is Bieng Called')
        
    return wrapper
                
@log_function_call
def hello():
    pass
    
hello()