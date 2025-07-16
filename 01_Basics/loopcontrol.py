print("Using 'continue':")
for num in range(1, 6):
    if num % 2 == 0:
        continue  
    print(num, end=" ")
print("\n")
#--------------------------------------------------------------------
print("Using 'pass':")
for num in range(1, 6):
    if num == 3:
        pass  
    print(num, end=" ")
print("\n")
#--------------------------------------------------------------------
print("Using 'break':")
for num in range(1, 6):
    if num == 3:
        break  
    print(num, end=" ")
print("\n")
#--------------------------------------------------------------------
