tup = (1, 2, 3, 4, 5, 2, 3, 6, 2, 4, 4, 7)

seen = set()
repeated = set()

for item in tup:
    if item in seen:
        repeated.add(item)
    seen.add(item)

print("Repeated items:", list(repeated))
