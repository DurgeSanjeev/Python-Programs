#sets
s={23,34,1,65,4,32,66,34,84} #we initilise with the help of flower braces
print(s)                   #while we print we wont get output as same as we gave but in some random form
                           # we also saw 34 is printed at ones only

#print(s[2:])             #as there is no index or numbering for sets its just a collection of values , this doesnt support duplicate values

print(s)
print(type(s))
s.add(5)
print(s)
d= s.intersection({23,34,21,4,8})
print(d)
s.add('hy')
print(s)
print(len(s))
