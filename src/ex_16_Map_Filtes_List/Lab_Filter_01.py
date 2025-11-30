# Filter (): it filters elements of an iterable using a condition (returns only those that match true)
# filter(function, iterable)
from operator import truediv

# print the even numbers
l = [1,2,3,4,5,6,7,8,9]

def even(num):
    return num % 2 == 0

even_numbers = list(filter(even, l))
print(even_numbers)



# select student with greater than 50.
list_students = [50,51,78,88]

def keep(num):
    if num >55:
        return True

all_students = list(filter(keep, list_students))
print (all_students)