#DATA STRUCTURE: FROZEN SET
a = frozenset([1, 2, 3])           #set representation and creating
b = frozenset([3, 4, 5])
print(a, b)
print(type(a))

#set operations
print("Union: ", a|b)                                       #comman values once                               
print("Intersection: ", a&b)                                #only comman values
print("Difference a-b : ", a-b)                             #values in A not in B
print("Symmetric Difference: ", a^b)                        #uncomman elements

print("A is subset of B: ", a.issubset(b))                  # b is in a
print("A is superset of B: ", a.issuperset(b))              # a contains b

print('y' in frozenset("python"))               #membership

for ch in frozenset("freeze"):                  #looping through set
    print(ch, end='')
print()

#conversion: List to frozenset
l = [1, 2, 3, 4]          
s = set(l)                   #conversion of list to set
f = frozenset(s)                #conversion of set to frozenset
print("L: ", l)
print("S: ", s)
print("F: ", f)
f = frozenset(l)             #direct conversion possible

#frozenset as dict key
f1 = frozenset([1, 2])
f2 = frozenset([3, 4])
fd ={f1:"first", f2:"second"}
print(fd)

s = {f1, f2}                    #set of a frozensets (set of sets not possible)
print(s)
