sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
prct = total / 5

print("Total Marks:", total)
print("Percentage:", prct, "%")

if prct >= 90:
    print("Grade: A+")
elif prct >= 80:
    print("Grade: A")
elif prct >= 70:
    print("Grade: B")
elif prct >= 60:
    print("Grade: C")
elif prct >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
