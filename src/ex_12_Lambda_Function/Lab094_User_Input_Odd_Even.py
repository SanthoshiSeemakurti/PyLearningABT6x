# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
num = int(input("Enter a number: "))
check_Even_Odd = lambda num : "Even" if num % 2 ==0 else "odd"
result = check_Even_Odd(num)
print (result)
