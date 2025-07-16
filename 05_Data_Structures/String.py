
# DATA STRUCTURE : STRING

s = "mitochondria"          #representation

print(s[7])                 #accessing
print(id(s))

# s[2] = "a"                #immutability

s = "photosynthesis"        #reassignment possible 

print(id(s))                #addressing

print(s[0:5])               #slicing
print(s[5:])
print(s[5:-3])

print(s)
print(s.partition("syn"))   #partitioning

s = "{}{}{}".format("Hello","Good","Morning")                 #string formatting
print(s)
s = "{},{},{}".format("Hello","Good","Morning")
print(s)

s = "{2} {0} {1}".format("Hello","Good","Morning")            #positional formatting
print(s)
s = "{b} {a} {c}".format(a="Hello",b="Good",c="Morning")      #keyword formatting
print(s)

s = "Prachiti"                          #METHODS
print(len(s))
print(s.capitalize())
print(s.casefold(), s.lower())
print(s.count("i"))
print(s.find("i"))
print(s.rindex("i"))
print(s.replace("iti", "i"))
print(s.split("c"))
print(s.strip())
print(s.swapcase())
print(s.title())
print(s.join("1234567"))