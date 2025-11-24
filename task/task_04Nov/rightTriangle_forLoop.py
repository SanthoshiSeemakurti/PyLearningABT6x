"""
Right angle Triangle star pattern
*
**
***
****
*****

"""

for i in range(1,6):
    print("*"*i)


"""inverted triangle
 for i in range (6,-1,-1):
    print("*"*i)
"""

for i in range(1,6):
    for j in range(1,i+1):
        while i>j:
            print("*"*i)