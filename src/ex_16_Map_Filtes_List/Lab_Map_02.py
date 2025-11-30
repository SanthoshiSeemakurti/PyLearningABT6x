names = ["ram","sham", "radha","sara", "veena"]

def upper_case(string):
    return string.upper()

upper_names= list(map(upper_case, names))
print(upper_names)