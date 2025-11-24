"""
set is unique elements,
it is unordered collection of data types
it is mutable in nature.
it is unindexed
{}
it is used for testing, removing duplicates and mathematical set operations like union (OR) and intersection (AND).
"""
# list -> [], tuple -> (), set -> {}

list_of_unique_items ={1,2,2,7,9,7,8,9,10}
print(list_of_unique_items)

list1 =[44.5,67.8,78.9,67.8,78.9]
print(list1)
set1 =set(list1)
print(set1)
t = ("Test", "grape", "grape","Test", "apple", "apple", "jangle","dollar")
print(t)
print(set(t))
mixed={1, "QA", "Zoo", "two", "two" ,3.5, 6.7, 3.5}
print(mixed)
for  item in mixed:
    print(item)

empty = set()
print(type(empty))

empty.add(10)
print(empty)
(empty.add(20))
print(empty)
empty.remove(20)
print(empty)
empty.discard(10)
print(empty)

empty.discard(30)  # dose nothing, no Error, even there is no such element present in the set
print(empty)
# empty.remove(30)    # Raises error, when there is such element present in the set
print(empty)