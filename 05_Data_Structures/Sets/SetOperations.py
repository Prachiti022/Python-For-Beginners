# Creating two sets
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}

# Union of sets
all_items = fruits.union(companies)
print("Union:", all_items)

# Intersection of sets
common_items = fruits.intersection(companies)
print("Intersection:", common_items)

# Difference of sets
unique_fruits = fruits.difference(companies)
print("Difference:", unique_fruits)

# Symmetric Difference of sets
unique_items = fruits.symmetric_difference(companies)
print("Symmetric Difference:", unique_items)
