# pop - Removes and returns the item at the index (default last object)

squares = [1,4,9,16,25,36,49,64]
print(squares)
print(squares.pop()) # only pop / removed item is printed
print(squares)
print(squares.pop(2)) # only pop / removed item with is printed
print(squares)

squares.clear()
print(squares)

# index (element, start, end)
    # element Required. Any type (string, number, list, etc.). The element to search for
    # start	Optional. A number representing where to start the search
    # end	Optional. A number representing where to end the search
# index() - returns the index of the first occurrence of the element
numbers=[10,20,30,40,50,60,70,80,90,10,10,20,30,40,30]
print(numbers.index(20, 6,12))
print(numbers.index(50))

print("no. of 10's: ",numbers.count(10))
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

print("Max value:",max(numbers))
print("min value: ",min(numbers))
print("Sum: ",sum(numbers))

# slicing
print(numbers[1:4]) # print from index of 1 to 3
print(numbers[-1]) # refers last element

print("apple" in numbers)
print(20 in numbers)

# list creation and comprehension - its shortcut to create a loops
# range (1,5) #-> will return list
l =list(range(1,5))
print(l)


matrix =[[]]