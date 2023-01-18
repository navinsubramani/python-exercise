'''Importing statistics to calculate the median'''
import statistics
import time

def time_profile(func):
    '''Definition of the decorator'''
    def wrapper(*args, **kargs):
        start = time.perf_counter_ns()
        result = func(*args, *kargs)
        end = time.perf_counter_ns()

        time_delay = (end-start)/1000000
        print(f'Time delay is {time_delay} ms')
        return result
    return wrapper

@time_profile
def algorithm(n_list: list):
    '''Finds the median for a given function
    '''
    return statistics.median(n_list)


print(algorithm(range(10000000)))