shopping_list_wife = ["bread", "milk", "aata"]
shopping_list_wife [2]= "veggies"  # list can be changed
print(shopping_list_wife)

# real of tuples
# as the tuples are immutable, but need to be changed,
   # tuple needs to be converted to list, do the changes and convert back to tuple
my_tuple = ("api.com", "sdet.com")
print(my_tuple)

# converting tuples to list
my_api_list = list(my_tuple)
print(my_api_list)

# changing the list items
my_api_list.append("ind.com")
print (my_api_list)

# converting back to tuples that cant be modified
my_api_tuple= tuple(my_api_list)
print(my_api_tuple)

# creating an empty tuple
t= tuple()
print(t)

# creating an empty list
l= list()
print(l)

#converting list to tuple
t1 = tuple(["Rada", "rani", "Baby"])
print(t1)
# different tuples can be combined
hero1 = ("Batman", "Superman" )
hero2 = ("Wonder Women", "Princess Jasmine")
new_tuple =(hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print (new_tuple[1])
print(new_tuple[0][1])

