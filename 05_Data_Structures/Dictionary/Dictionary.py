#DATA STRUCTURE: DICTIONARY
d = {}
print(type(d))

d = {1:"one", "two":1 ,"one":"one"}                                 #representation(no duplicate keys)
print(d)

samp = dict([(1,'prachiti'), (2,'uma')])                            #conversion of tuple to dictionary
print(samp)

d = {"name":{185:"Prachiti"},                                                   #nested dictionary
     "subject":{"programming":"python", "maths":{"geometry":"trigonometry"}}}

print(d["name"])                                        #accessing dict
print(d["name"][185])

print(d["subject"]["programming"])                      #accessing nested dict
print(d["subject"]["maths"]["geometry"])

d["percentage"] = 99                                    #adding element (new as doesnt exist)
d["name"] = {156:"uma"}                                 #adding element (replacing existing)
print(d)                               

d["marks"] = 10, 20, 30                                 #adding set of values
print(d)

d = {"A":1,"B":2,"C":3,"D":4}       #METHODS 
print(d.get("A"))                       #get                   
print(d.get("B"))                               
print(d.get("E","not found!!"))

print(len(d))           #len

print(d.keys())         #keys
print(d.values())       #values
print(d.items())        #items

d.pop("D")              #pop
print(d)
del d["C"]              #del particular item
print(d)
d.clear()               #clear
print(d)
del d                   #del entire dict

d1 = {"A":1, "B":2}
d2 = {"C":3, "D":4}
d1.update(d2)           #update
print(d1)

d1 = {}        #dictionary copying (switching key and values)
d = {"A":1, "B":2, "C":3, "D":4}
print(d)
for key,value in d.items():         
    d1[value] = key
print(d1)

print(" ")
print(" ")

print(d)
d2 = {k:v for(k,v) in d.items() if v>2}          #dict comprehension
print(d2)

d2 = {k:v for(k,v) in d.items() if v%2==0}
print(d2)

d2 = {k:("even" if(v%2==0) else "odd") for k,v in d.items()}
print(d2)