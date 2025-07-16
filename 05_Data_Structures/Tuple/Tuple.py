#DATA STRUCTURE: TUPLE
t1 = (2, 4, 2)                          #representation
print(t1)

t2 = ("a", 'b', (1, 2))                 #multidimensional tuples
print(t2)

t3 = t1 + t2                            #concatenation
print(t3)

print(t3[2])                            #indexing

print(t3[2:5])                          #slicing

t1 = (1, 2, 5, 6, (7, 8, 9))            #nesting tuples

#t1[2] = 3                              #immutability

print(t1)                   
print(t1[4][1])                         #multi-dimensional accessing

del t3                                  #deleting

l = ["hii"]                             #conversion of list to tuple
t = tuple(l)
print(type(t))

s = "hii"                               #conversion of string to tuple
t = tuple(s)
print(type(t))

l = list(t)                             #conversion of tuple to list
print(l)

t = ("a", "b", "c", "d", "a", "a")      #METHODS
print(t.index("b"))                         #index
print(t.count("a"))                         #count

for i in enumerate(t):                      #enum
    print(i)

print(max(t))                               #max
print(min(t))                               #min

temp = sorted(t)                            #sorted
print(t)

t = (1, 2, 3, 4, 5, False)
print(sum(t))                               #sum

#tuple is faster than list
import timeit
print(timeit.timeit("x=(1, 2, 3, 4, 5)", number=1000000))
print(timeit.timeit("x=[1, 2, 3, 4, 5]", number=1000000))

samp = "hi", "hii"      #tuple
print(type(samp))
samp = ("hi")           #string
print(type(samp))
samp = ("hi", "hii")    #tuple
print(type(samp))
samp = ("hi",)          #tuple
print(type(samp))