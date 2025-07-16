num = int(input("Enter a number: "))

org = num

rvs = 0
while num > 0:
    digit = num % 10
    rvs = rvs * 10 + digit
    num = num // 10

if org == rvs:
    print(f"{org} is a palindrome.")
else:
    print(f"{org} is not a palindrome.")
