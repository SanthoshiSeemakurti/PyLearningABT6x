"""
Given a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1,
"""

num = int(input("Enter a number to find its factorial: "))
if num < 0:
    print("No factorial for negative numbers! Enter a number greater than 0")
elif num == 0 :
    print("Factorial of 0 is: 1" )
else:
    fact = 1
    i = 1   # initiation
    while i <= num:     # condition
        fact = fact * i
        i += 1        # decrement
    print(f"Factorial of {num} is: {fact}")


