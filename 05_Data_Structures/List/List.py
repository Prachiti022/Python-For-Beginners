# DATA STRUCTURE : LIST

l = ["Hello", 2, True, 3.6, ["abc", False]]     #representation
print(l)

print(l[1])                                     #accessing

print(l[4][1])                                  #multidimensional accessing

l[3] = 2                                        #mutabality and duplicating
print(l)

#METHODS
l.append(123)               #append
print(l)

l.extend(["pqr","stv",23])  #extend
print(l)

l.insert(2, "second")       #insert
print(l)

l.remove(True)              #remove
print(l)

l.pop()                     #pop
print(l)

print(l.count(2))           #count

l.reverse()                 #reverse
print(l)

l = [1, 5, 3, 2, 7, 0, 4]
l.sort()                    #sort() -> within same list
print(l)

sorted(l)                   #sorted() -> creates a copy of list and then sorts it
print(l)

lc = l.copy()               #copy
print(lc)

print(l.index(2))           #index

l.clear()                   #clear
print(l)

l1 = ["a", "v", "t", "b", "z"]        #Deep Copy
l2 = l1                               #Both list points same address
l2.append("hiii")
print("OG list: ", l1)
print("New List: ", l2)
print(id(l1))
print(id(l2))

l1 = ["a", "v", "t", "b", "z"]        #Swallow Copy
l2 = l1.copy()                        #Creates new location created and then copied
l2.append("hiii")
print("OG list: ", l1)
print("New List: ", l2)
print(id(l1))
print(id(l2))

l3 = []                     # 2's table using for loop and list
for i in range(2, 21, 2):
    l3.append(i)
print(l3)

l1 = [2*i for i in range(1, 11)]                #List Comprehension
print(l1)
l2 = [2*i for i in range(1, 11) if(i%2==0)]
print(l2)

print(" ")
print(" ")

l3 = [2*i if(i%2==0) else 3*i for i in range(1, 11) ]    #
print(l3)

del l2        #deleting