list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

print(len(list1))
print(max(list1))
print(min(list1))

tuple1 = (100, 200, 300)
converted_list = list(tuple1)
print(converted_list)

list1.append(60)
print(list1)

print(list1.count(30))

list1.extend(list2)
print(list1)

print(list1.index(40))

list1.insert(2, 25)
print(list1)

popped_item = list1.pop()
print(popped_item)
print(list1)

list1.remove(30)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)
