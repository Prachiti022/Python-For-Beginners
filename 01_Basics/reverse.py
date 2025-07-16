num = int(input("Enter a number: "))
org = num

rvs = 0
while num > 0:
    digit = num % 10
    rvs = rvs * 10 + digit
    num = num // 10

print("Original Number: ", org)
print("Reverse Number: ", rvs)
