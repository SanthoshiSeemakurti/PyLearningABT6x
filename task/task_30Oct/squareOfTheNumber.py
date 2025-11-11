"""
Q - Create a function which will take a positive number from the user and perform square of the number?

i/o = 3
o/p = 9

"""


def square(n):
    return n ** 2

try:
    n = int(input("Enter a number to find its square: "))
    result= square(n)
    print(f"The square of the {n} is: ", result)
except :
    print("Entered non numeric value, please enter a numeric value: ")