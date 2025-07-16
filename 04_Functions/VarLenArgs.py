def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

add_numbers(10, 20, 30, 40)

display_info(Name="Prachiti", Age=20, Course="Computer Engineering")
