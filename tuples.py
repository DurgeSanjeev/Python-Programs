#tuple this is same as lists but immutable values cannot be changed
values=(23,33,45,6,51,9,6) #tuples are initialised with paranthasis
print(values)
print(values.count(6))


"""t= tuple()
print(dir(t))   #to see directory of tuple see what are methodes work"""

"""(x,y) = (4,6)
print(y)
(a,b) = ("samsung","iphone")
print(a)"""

"""print((3,5,8)>(2,9,6))     #tules are comparable as they only check first one if true it says as true or ifit is false then moves to next one
d={"d":1,"b":2,"c":3}
print(d.items())
print(sorted(d.items()))   #sorts by checking the key of that dict

l=list()
for k,v in d.items():
    l.append((v,k))5554
print(l)
print(sorted(l,reverse= True))
print(l)"""


fhand = open('sili')
#print(fhand.read())
d=dict()
for line in fhand:
    words = line.split()
    # print(words)
    for word in words:
        d[word]= d.get(word,0)+ 1.
print(d)

l=list()
for key,value in d.items():
    newtup = (value,key)
    l.append(newtup)
print(l)

l= sorted(l,reverse=True)

print(l)

for value,key in l[:5]:
    print(value,key)







