"""
User defined function:
1. Non-return function
2. non-retuning function with parameter
3. no return type with default parameter function
4. multiple parameter function

"""
import math

# built in functions:
result  = max(9,99)
print(result)

# 1.Non-returning function:
def greet():
    print("Hi")
greet()

#2.no return type with argument function:

def greet1(name):
    print( "Hello", name)

greet1("Sara")

# 3.no return type and with default arguments

def say_hello_default_arg(name= "Santu"):
    print("Hello", name.upper())
say_hello_default_arg()
say_hello_default_arg("Myra")


# multiple arguments:

def multiple_arg(name2= "Ram", name1= "sita"):
    print("Multiple Arg:",name1, name2)
multiple_arg(name1="lakshmi", name2="narayana")
multiple_arg(name1="janaki")
multiple_arg(name1= "Krishna")
multiple_arg()

#4.Argument + return type

def sum_of_two(a,b):
    return a+b
result =sum_of_two(2,3)
print(result)

def sum_of_two_with_default(num1=100,num2=200):
  print("I'll add two numbers!")
  return num1+num2

result = sum_of_two_with_default(5,6)
print(result)
result1 = sum_of_two_with_default()
print(result1)
