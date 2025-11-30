dict1 ={"a":1, "b":2, "c":3, "d":4}
dict2 ={"a":1,"c":3}

print (dict1.keys())
print (dict1.values())
print(dict2.keys())
print(dict2.values())
missing_keys=set(dict1.keys()-dict2.keys())
print(missing_keys)