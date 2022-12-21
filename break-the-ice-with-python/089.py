# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person(object):
    def __init__(self):
        self.gender = "unknown"
    
    def getGender(self):
        return self.gender


class Male (Person):
    def __init__(self):
        self.gender = "Male"

class Female (Person):
    def __init__(self):
        self.gender = "Female"

aMale = Male()
aFemale = Female()

print(aMale.getGender())
print(aFemale.getGender())