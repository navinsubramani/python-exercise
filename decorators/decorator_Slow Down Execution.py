'''Import the time module to use the sleep function'''
import time

def slow_down(func):
    '''Code definition for slowing down the execution using time sleep'''
    def wrapper(*args, **kargs):
        time.sleep(1)
        return func(*args, **kargs)
    return wrapper

@slow_down
def add(a, b):
    '''Dummy Code'''
    return a+b

print(add(1,1))