# Create a program to sum of three number from the user input
# if user doesn't enter values, use default values as 100, 200, 300

# logic building:
#step1: I/O and O/P
# i/o - int
# o/p - int
# step 2: rough logic
# return n1+n2+n3
# step 3: write logic

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def sum_of_three(n1=100,n2=200, n3=300):
    return n1 + n2 + n3

result = sum_of_three(num1, num2, num3)
print(result)
# step 4: edge cases
result1 = sum_of_three()
print("Default values:", result1)
result2 = sum_of_three(9,8)
print(result2)
# step 4: edge cases