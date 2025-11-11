"""
Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 !=side3 → isosceles
o/p = result in string - iso, eq, scalene

"""

def check_triangle_type(side1, side2, side3):

    # check if the sides can form a triangle
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return "Not a valid triangle"

    # check if all sides are equal - it's an equilateral triangle
    if side1 == side2 == side3:
        return "It's an Equilateral triangle"

    # check if any two side are equal - It's an Isosceles triangle
    elif side1 ==side2 or side2 == side3 or side3 == side1 :
        return "It's an Isosceles triangle"

    # check if none of the sides are equal - It's a Scalene triangle
    else:
        return "It's a Scalene triangle"

# input the sides of the triangle
print ("Enter side1 side2 side3 of a triangle: ")
side1= int(input("Side1: "))
side2= int(input("Side2: "))
side3= int(input("Side3: "))

# Validate and print the triangle type
result = check_triangle_type(side1, side2, side3)
print(result)