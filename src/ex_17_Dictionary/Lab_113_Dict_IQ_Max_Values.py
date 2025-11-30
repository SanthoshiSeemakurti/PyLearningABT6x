# Function that returns max value from the dictionary.
#{"a": 10, "b": 30, "c": 40}

def max_value_dict(dictionary):
    return max(dictionary.values())

def mxa_key_dict(dictionary):
    return max(dictionary.keys())

my_dict = {"a": 10, "b": 30, "c": 40}

print(max_value_dict(my_dict))
print(mxa_key_dict(my_dict))


