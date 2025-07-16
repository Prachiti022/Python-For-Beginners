def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

text = input("Enter a string: ")
count_case(text)
