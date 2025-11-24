import math

# def give_me_power(num):
#     return math.pow(num, 2)
#
# op =  give_me_power(10)
# print(op)

# num = int(input("Enter the number"))
# op2 = lambda num: math.pow(num, 2)
# print(op2(num))

# user input values
n = int(input("Enter a number: "))
exponential_value = int(input("Enter exponential value: "))

#caluclation 1
nExpo  = lambda n, exponential_value : n ** exponential_value
result = nExpo(n, exponential_value)
print("Result: ", result)

#caluclation 2
nExpo1= lambda num,exponential_value : math.pow(num,exponential_value)
result1 = nExpo1(n,exponential_value)
print("Result1: ", result1)


nExpo2 = lambda: math.pow(int(input("Enter the Number: ")),int(input("Enter the power value: ")))
result2 = nExpo2()
print("Result2: ", result2)


