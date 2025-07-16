words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

num = input("Enter a number: ")

for digit in num:
    print(words[int(digit)], end=" ")
