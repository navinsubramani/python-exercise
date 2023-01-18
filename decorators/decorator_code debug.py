
def code_debug(func):
    '''Definition of the that prints the input and output of any function to the console'''
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)
        
        print('Input Arguments:')
        a = [print(i) for i in args]
        b = [print(key, i) for key, i in kargs.items()]

        print('Output Value:')        
        print(result)

        return result
    return wrapper

@code_debug
def sum_of_two_numbers(a, b):
    '''Dummy function'''
    return a+b

@code_debug
def multiply_two_numbers(a, b):
    '''Dummy function'''
    return a*b

sum_of_two_numbers(2, 4)
multiply_two_numbers(3, b=3)