#DATA STRUCTURE: SETS
s = {}
print(type(s))
s = {()}
print(type(s))
s = ({})
print(type(s))

a = {1, 2, 3, 4}         #set representation
b = set([3, 4, 5, 6])
c = set({1:"ps"})        # only utilize key of dict
print("Set A: ", a)
print("Set B: ", b)
print("Set C: ", c)

a.add(5)                #adding single element using add()
print(a)

a.update([6, 7])        #adding multiple elements using update()
print(a)

a.remove(6)           #remove element
#a.remove(10)         #error if element dont exist

a.discard(100)        #No error if element doesnt exist

#set operations
print(a)                                                     
print(b)
print("Union: ", a|b)                                       #comman values once
print("Union: ", a.union(b))                                
print("Intersection: ", a&b)                                #only comman values
print("Intersection: ", a.intersection(b))
print("Difference a-b : ", a-b)                             #values in A not in B
print("Difference b-a : ", b.difference(a))
print("Symmetric Difference: ", a^b)                        #uncomman elements
print("Symmetric Difference: ", a.symmetric_difference(b))

print("A is subset of B: ", a.issubset(b))                  # b is in a
print("A is superset of B: ", a.issuperset(b))              # a contains b

c = a.copy()         #copy() creates new set in memory
print(c)

c.clear()            #clear() delete all elements
print(c)

s1 = set("hello")                                 #set from string and list(duplicates removed)
s2 = set(["apple", "banana", "apple", "cherry"])
print(s1)
print(s2)

s = {1, 2, 3, 4, 5, 6}           #membership in set
print(3 in s)
print(10 in s)
print(3 not in s)
print(10 not in s)

for item in s:                  #looping through set
    print("Item: ", item)

square = {x**2 for x in range(6)}         #set comprehension
print(square)

print(s)                    #popping random element
e = s.pop()
print(e)
print(s)