list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

# Using set intersection
common_items = list(set(list1) & set(list2))
print("Common items:", common_items)

# Using list comprehension
common_items2 = [item
                 for item in list1
                     if item in list2]
print("Common items (list comprehension):", common_items2)
