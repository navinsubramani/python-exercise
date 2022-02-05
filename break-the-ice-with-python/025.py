# Define a class, which have a class parameter and have a same instance parameter.

class test():
    value1 = 0

    def __init__(self, value):
        self.value1 = value


a = test(5)
print(a.value1)
print(test.value1)
