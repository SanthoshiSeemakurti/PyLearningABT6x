# print non-empty strings in a given list

names = ["QA", "", "Test", "Data", ""]

def non_empty(x):
    if x != "":
        return True
    return None

no_empty = list(filter(non_empty, names))       # removes non-empty strings
print(no_empty)