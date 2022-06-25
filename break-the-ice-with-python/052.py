# Define a custom exception class which takes a string message as attribute.

class MyError(Exception):

    def __init__(self, message):
        self.msg = message


error = MyError("This is a custom error")

try:
    raise error

except MyError as err:
    print(error.msg)
