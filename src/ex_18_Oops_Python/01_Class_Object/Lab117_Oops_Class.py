# CAB -> ( class, Attribute, Behaviour)
"""
Function:
A function is a standalone block of reusable code that performs a specific task.
It can be called independently by its name, and
it typically takes input arguments and may return a value.
Functions are not tied to any particular object or class and
operate on data that is explicitly passed to them.

Method:
A method is a function that is associated with an object or a class.
It is defined within a class or a similar data structure and operates on the data (attributes) of the object it belongs to.
Methods are called using the object's name followed by a dot and the method's name (e.g., object.method()).
They implicitly have access to the object's data and can modify its state.
"""


class Person:
    # Attributes
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    mobile_no = None
    address = None

    # Behaviour (methods)

    def method_talk(self):  # self - this , self will be the frist argument in every behavior.
        print("I'm Talking to you.")

    def method_see(self, name):  # Arg with no return type
        print("I see you")
        print("see", name)

    def method_hear(self, name):  # Arg with return type
        print("I'm hearing")
        return None

    def method_walk(self):  # no arg with return
        return "I'm walking"


def function_outside():  # (function)
    print("block of code outside the class is called Function")


# create an object of the class
# objectRef = className() -> object
# geeta : object reference
# Person() : object


geeta = Person()
ara = Person()
print(geeta.name)
ara.method_see("Abhi")
function_outside()
