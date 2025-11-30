string =input("Enter a string: ")
# a,e,i,o,u
# no. of vowels in the input string

vowels = "aeiou"
vowels_count = 0
result = list ()

for char in string:
    if char in vowels:
        vowels_count += 1
        result.append(char)
print (vowels_count)
print(result)