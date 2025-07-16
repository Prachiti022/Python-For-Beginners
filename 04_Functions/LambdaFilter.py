from functools import reduce

# Lambda Function
uppercase = lambda text: text.upper()
print(uppercase("hello"))

# Map Function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers))
print("Squares:", squared)

# Reduce Function
total_sum = reduce(lambda x, y: x + y, numbers)
print("Sum:", total_sum)

# Filter Function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)
