# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Answer

# print("swiss".count("s"))
# print("swiss".count("w"))
# print("swiss".count("i"))

s= set()

def first_non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            s.add(char)
            return char
    return None

word = input("Enter a word to find the first non repeating character: ")
print(first_non_repeating_char(word))
print(first_non_repeating_char("tomorrow"))
print("set: ", s)