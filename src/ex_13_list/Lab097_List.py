my_list = [1, 2, 3, 4, 5]
my_list[0] = "Myra "
my_list[1] = "is "
my_list[2] = "my "
my_list[3] = "Universe."
my_list[4] = True

for i in my_list:
    print(i)


# range() is a function that creates a list and returns that
#indexing
for i in range(0,4):
    print(f"Element at index {i}: ",i)

# append() add an object to the end of the list.
my_list.append(2025)
print(my_list)

#extend() - appends a new list
my_list.extend(["Junnu" , "is", "my ", "super", "star"])
print(my_list)

# insert() a object can be inserted at a particular index/position in the list
my_list.insert(1,"Kada ")
print(my_list)

# changing the item at a particular position
my_list[5] = "Forever"
print(my_list)

# remove() deletes a particular element from the list
my_list.remove(2025)
print(my_list)

#delete is a keyword, deletes an element by index or whole list
del my_list[1]
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)
