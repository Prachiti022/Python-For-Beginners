# Given dictionary
data = {'a': 50, 'b': 200, 'c': 150, 'd': 300, 'e': 100}

# Finding the highest 3 values
highest_values = sorted(data.values(), reverse=True)[:3]

print("Highest 3 values:", highest_values)
