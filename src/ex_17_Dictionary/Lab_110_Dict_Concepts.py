keys= ["name", "role", "Experience", "gender"]
values = ["Aman", "IAS", 5]
my_dict = dict(zip(keys, values))
print(my_dict)

#Merge Two dictionaries
dict1 ={"a": 1, "b": 2,"d": 4}
dict2= {"c": 3, "f": 6, "e": 5}
print(dict1)
print(dict2)

merged_dict = dict1|dict2
print(merged_dict)
print(merged_dict.keys())
print(merged_dict.values())
print(merged_dict.get("c"))