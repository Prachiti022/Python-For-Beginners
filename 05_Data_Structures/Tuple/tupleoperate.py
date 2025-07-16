# Creating Tuples
tup1 = ('apple', 'banana', 'cherry', 10, 20)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = ()                   # Empty tuple
tup5 = (50,)                # Single-element tuple

# Accessing Tuples
print(tup1[0])
print(tup2[1:4])

# Concatenation (Updating indirectly)
tup6 = tup1 + tup2
print(tup6)

# Deleting a Tuple
del tup1

# Convert Tuple to List (Multiple Methods)
tup_to_list1 = list(tup2)
tup_to_list2 = [i for i in tup3]
tup_to_list3 = [*tup3]
tup_to_list4 = list(map(lambda x: x, tup3))

print(tup_to_list1)
print(tup_to_list2)
print(tup_to_list3)
print(tup_to_list4)

# Convert List to Tuple
list_to_tup = tuple(tup_to_list1)
print(list_to_tup)
