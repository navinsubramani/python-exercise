# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7
# Then, the output should be:

# 0
# 7
# 14

from ast import Pass
from unittest import result


class range_divby7():

    def __init__(self, start, last):
        self.start = start
        self.last = last
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current == self.last:
                StopIteration
            elif self.current % 7:
                self.current += 1

            else:
                result = self.current
                self.current += 1
                return result


for i in range_divby7(10, 100):
    print(i)
