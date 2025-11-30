"""
frequency of characters in a String
#write a program to count the frequency of characters in a given String
"""

string = "santhoshi"
srting =input("Enter the input string e.g: santhoshi: ")
#{s: 2, a: 1, n: 1, t:1, h:2, o:1 i:1}
char_count ={}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)