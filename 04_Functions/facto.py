def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))




