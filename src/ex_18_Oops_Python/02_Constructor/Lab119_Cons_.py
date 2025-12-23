"""
constractor : it is a special method that is called automatically when an object is created from a class.
It's main role is to initialize (__init__) the object by setting up by its attributes.

"""

print("outside the class")


class mobilePhone:
    brand = None
    model = None

    def __init__(self):
        print("inside default constructor")

    def talk(self):
        print("inside talk")


iphone = mobilePhone()
iphone.talk()
print("outside the class2")
