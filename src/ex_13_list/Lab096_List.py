"""
list: it is a collection of items that are ordered and changeable data types(mutable).
    It allows duplicates and supports modification.
    It allows us to store elements of different data types in one container
    ex: Grocery list - [milk, butter, bread]
    ex: 10th marks list
"""
my_list = [1, 2, 3, 4, 5] # same data type - int
my_list2 = [1, "Partha", 99.99, True]
print("My list1:",my_list)
print("Type: ", type(my_list))
print("Length: ",len(my_list2))
print("First element",my_list[0])


print("My list 2:",my_list2)
print("Type: ",type(my_list2))
print("Length: ",len(my_list2))
print("second element:",my_list2[1])
# print("sixth element:",my_list2[7]) index Error: List index out of range
