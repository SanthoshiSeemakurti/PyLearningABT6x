squares = set()

for x in range (5):
    x = x**2
    squares.add(x)
    print(x)
print(squares)

fset = frozenset([1,2,3,4,4])
print (fset)
print(type(fset))
