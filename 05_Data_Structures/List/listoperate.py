# Creating lists
list1 = ['Java', 'Python', 'Perl']
list2 = [10, 20, 30, 40, 50]

# Accessing list elements
print("Accessing elements:")
print("list2[1] =", list2[1])                       # Access single element
print("list2[1:3] =", list2[1:3])                   # Access slice

# Updating list elements
list2[0] = 60                                       # Updating first item
list2[3:4] = [70, 80]                               # Updating multiple elements
print("Updated list2:", list2)

# Adding elements
list1.append('C++')                                 # Append a single item
list1.extend(['Ruby', 'JavaScript'])                # Extend with multiple items
print("Extended list1:", list1)

# Concatenation
list3 = list1 + ['Swift', 'Go']
print("Concatenated list3:", list3)

# Repetition
list4 = ['A', 'B'] * 2
print("Repeated list4:", list4)

# Insert at specific position
list2.insert(1, 30)
print("List after insertion:", list2)

# Deleting elements
del list2[2]                                        # Using del
print("List after deleting index 2:", list2)


list2.remove(50)                                    # Using remove
print("List after removing 40:", list2)

# Deleting entire list
del list1
# print(list1)                                      # error since list1 not present
