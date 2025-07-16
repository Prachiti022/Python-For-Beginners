# Creating a dictionary
student = {"name": "John", "age": 20, "course": "Python"}

# Accessing values
print("Name:", student["name"])

# Modifying values
student["age"] = 21
print("Updated dictionary:", student)

# Adding new key-value pair
student["grade"] = "A"
print("Dictionary after adding:", student)

# Removing a key-value pair
del student["course"]
print("Dictionary after deletion:", student)

# Iterating over dictionary
for key, value in student.items():
    print(key, ":", value)
