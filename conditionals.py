#Syntax
"""if condition:      # here colon is given to enter inside the if block
      statements....
   else:               # no need ot write conditions in else coz its only true or false statements
      statements
statements #this statements doesnt come under if else condition due to indentation
      """

"""#nested if else 
if conditions:
   statements
    if conditions:    #this is if else inside if statements
       statements
    else:
        statements
else:
     if conditions:  #this is if else  inside else 
        statements
     else:   
        statements              
     statements  this statement doesnt belong to above else and belong to parent if else statements

#we also can use nested  if else both at a time both in if and else 
#we can also use lot of if conditions at a time but its not efficient way to write code
 """


"""#if elif else conditions
if conditions:
   statements
elif conditions:
   statements:
elif conditions:
   statements: 
else:
    statements    

"""


"""a= 5
b= 3
c= int(input())      #we use input() function only to take string inputs from users and we convert them to int or float or any datatype we needed
if a<=c:             
    print("true")
else:
    print("flase")"""


ch=input("enter a charecter")
print(ch[2])  #prints character at the given index no.

n=input("enter char")[2]  #we can also write above code like this at input only
print(n)

m=eval(input("enter expr"))  #eval is a inbuilt function to evaluate expression directly from input
print(m)






"""l=[23,43,7,67,75,9,2]
print(type(l))
print(55 in l)    # in keyword tells weather the given element is present or not
print(55  not in l)  #not in tells same
if 10 in l:
    print("there")
else:
    print("not there")"""

"""Quiz1"""
#print ("enter the age")
#age=int(input())
"""if age>18:
    print("allowed to drive")
elif age==18:
    print("meet me personally")
else:
    print("not allowed")"""

"""Quiz2"""
"""if age>100 or age<7:
    print("the entered age doesnt exixt")
elif age>18:
    print("allowed to drive")
elif age==18:
    print("meet me personally")
else:
    print("not allowed")"""

"""#Exersice2

a= int(input("enter a"))
b= int(input("enter b"))
print("what operation do u want to perform +,-,*,/,%,**")
i=(input())
p="+"
s="-"
m="*"
d="/"
M="%"
p="**"

if i==m and a!=45 and b!=3:
    c=a*b
    print(c)
elif a==45 and b==3:
    print("555")
elif i==p and a!=56 and b!=9:
    c=a+b
    print(c)
elif a==56 and b==9:
    print("77")
elif i==d and a!=56 and b!=6:
    c=a/b
    print(c)
elif a==56 and b==6:
    print("4")
else:
    print("get out from here")"""



#short hand if Else
a=int(input("enter a"))
b=int(input("enter b"))
if a>b:print(" true its greater")
else:print("lesser i think")

print("its greater") if a>b else print("lesser")  #above and this if else statements do same work but in one line


#   1. question

"""Write a Python program to get the difference between a given number and 17, if the number
 is greater than 17 return double the absolute difference."""

def difference(s):      # created a function named difference
    if s <= 17:     #if statement inside the function checks wheather n is less than or equal to 17
        return 17 - s       # returens the subtracterd value from 17
    else:                     # else statement is used here if input value is greater than 17
        return (s - 17) * 2        # returns the double of the absolute difference


print(difference(14))              # prints the value as 2 because input value is less than 17
print(difference(20))            # prints the value as 6 because input value is greater than 17
                                 # so that 20-17=3 and   3*2 =6


"""Write a Python program to create two strings from a given string. Create the first string
using those character which occurs only once and create the second string which consists of
multi-time occurring characters in the said string."""

from collections import Counter   #imported a counter from collections to use in followin function
def genStrings(input):             # created or declared a function named "genStrings"
     str_char_ctr = Counter(input)
     single = [ key for (key,count) in str_char_ctr.items() if count==1]
#created a forloop to check wheather for all characters the charecter is equal 1 or not

     multiple = [ key for (key,count) in str_char_ctr.items() if count>1]
#created a for loop to check wheather for charecters the character is repeated morethan ones

     single.sort()      # this sorts them according to  the alpabetical order of single variables
     multiple.sort()    # this sorts them according to  the alpabetical order of multiple variables
     return single,multiple     # return statement used to return vlaues of single and multiple


input = "oggyanndcockroaches"
v1, v2 = genStrings(input)
                 # the given inmput is passed to function by calling it and stored in v1,v2
print(''.join(v1))    # prints the value by joining all the values of v1
print(''.join(v2))     # prints the value by joining all the values of v2
