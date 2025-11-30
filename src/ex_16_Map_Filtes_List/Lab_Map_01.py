#  map(): applies a function to each item in a list (any iterable) and returns a map object (iterator).
# n=map(function, iterable)
numbers= [1,2,3,4]

def sq(x):
    return x ** 2

sq_all_numbers = list(map(sq, numbers))
print(sq_all_numbers)
