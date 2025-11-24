""" set is used for mathematical operations -> union and intersection.
union (OR) (a|b) : prints all the unique elements from both the sets
intersection (AND) (a&b) :prints common elements from both the sets.
Difference (a-b): prints only the elements present in "a" but not in "b"
symmetric difference(a ^ b):  prints all the elements present in "a" and "b" but not the common elements
"""

a = {1,2,8,9,10}
b = {1,3,2,9,10}
#union
print("union: ", a.union(b))
print("Union: ", a|b)

#intersection
print("Intersection: ", a.intersection(b))
print("Intersection: ", a&b)

#difference
print("Difference: ", a-b)
print("Difference: ", a.difference(b))
print("Difference: ", b-a)

# symmetric difference
print(a ^ b)
print("______________")

set1= {1,2,3,4,5}
set2= {4,5,6,7,8}

print("Union: ", set1.union(set2)) #{1,2,3,4,5,6,7,8}
print("intersection: ", set1.intersection(set2)) #{4,5}
print("Difference: ", set1.difference(set2)) # {1,2,3}
print("symmetric Difference: ", set1.symmetric_difference(set2)) # {1,2,3,6,7,8}



