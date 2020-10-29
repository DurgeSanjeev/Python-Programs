#Lists are mutable can be changed any time.and we can store any type of data like string,int float...
college=["students","faculty","buildings","hostels","food",87]  #lists are initilised with the help of square braces"[]"
print(college)
print(college[0])
print(college[1])
print(college[5])
numbers=[48,85,28,49,52,42]
print(numbers)
print(numbers[0])
print(numbers.sort()) #to sort inbuilt sort() function is there, this also changes the original list
print(numbers)
numbers.reverse()          #to reverse list inbuilt function reverse() is there,changes original list
print(numbers)
print(numbers[0:6])
print(numbers[ ::-2])
print(max(numbers))
numbers.append(99)   #appends given no. to the end of list ,changes original list.with hepl of append(no. to insert)
print(numbers)
numbers.insert(0,625)  #inserts the wanted no. at given index no. with help of insert(index no.,no. to insert)
print(numbers)
numbers.remove(625)            #remove given no. if there with help of remove(no. to be removed)
print(numbers)
numbers.pop()                 #removes the last no. inserted
print(numbers)
numbers[2]=55
print(numbers)
print(len(numbers))
print(range(4))               #range function returns the list
digit=[2,4,6,9,13,34]
print(numbers+digit)           #like integers we can also concatinate the lists
print(9 in digit)
print(9 not in digit)
print(sum(numbers))    #prints sum of lists
names=["lisa","alice","hayley"]
names.sort()                      #sorts according to alphabetical order
print(names)
print(len(names))
print(len(numbers))
print(max(numbers))
print(min(digit))
print(max(names))
print(min(names))
print(sum(digit)/len(digit))      #gives  average

"""exer=list()
while True:
    inp=input("no.")
    if inp == '0' :
        break
    v = float(inp)
    exer.append(inp)

avg = int(sum(exer)/len(exer))
print(avg)"""

x= "you are the best"
s=x.split()                  #this splits the string into the list  and divide them according to space given between the string
print(s)

line="may:be:you:deserve:better"
r=line.split()
print(r)
r=line.split(":")                 #we have to mention based on what the string has to be splitted in braces
print(r)



l=list()
#print(dir(l))



