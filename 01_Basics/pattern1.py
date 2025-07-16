rows = 4
width = 7

for i in range(rows, 0, -1):
    pattern = ""
    for j in range(1, 2 * i, 2):
        pattern += str(1 if j % 4 == 1 else 0)
    print(pattern.center(width))
