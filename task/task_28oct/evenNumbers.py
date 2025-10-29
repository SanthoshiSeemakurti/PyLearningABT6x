"""
Print even numbers between 1 and 20 use continue, break, pass
"""

# while loop
i=1     # initiation
print("Even number between 1 to 20 (while loop):")
while i <=20:       # condition
        if i%2 == 0:
            print(i)
        i = i + 1       # update


# for loop

print("Even numbers between 1 to 20 (for loop)")
for n in range (1,21,1):
    if n % 2 != 0:
        continue        # skip odd numbers
    print(n)

