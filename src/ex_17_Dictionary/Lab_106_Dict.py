"""
Dictionary:
key value pair
a Dictionary is unordered, mutable, and indexed collection of key-value pairs in python.
{}
mostly used in API automation (dictionary is similar to json)

"""

my_dict = {
    "name" : "Zara",
    "age" : 27,
    "role" : "AI_Engineer",
    "exp" : 4
}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["role"])
print(my_dict["exp"])
print(my_dict.get("role"))
print(my_dict.get("age"))

del my_dict["age"]
print(my_dict)

for key , value in my_dict.items():
    print (key, value)

print("age" in my_dict)
print("role" in my_dict)