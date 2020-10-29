#variables in python

v1="hyy";        #we need not to give semicolon in end while initializing variables.
print(v1);       #we dont give inverted commas while printing the value from somewhere.
v2=5
print(id(v2))   #id is a function which prints address of the variable
print(v2)
v3=54.76
print(v3)        # By default python gives the  datatype required as value is intialised
print(type(v1))  # type is a keyword used to know the datatype given to variable declared
print(type(v2))
print(type(v3))
print(v2+v3)     #here the values are added as the datatypes are int and float
#print(v1+v2)     #here gives error because  datatypes are int and string that cannot be added
v4=" python"
print(id(v4))
print(v1+v4)     #we can add two strings or characters because both datatypes are same
v5=" 3.8.2"
print(v4+v5)     #here v5 is taken as a character bcoz we written in inverted commas although it is a integer
v6="43"
v7="7"
print(v5+v6)     #as both are int but both are taken as strings so they get concatinated
print(int(v7) + int(v6));     """we have changed the datatype by method typecasting by writing name of datatype in 
front of variable name while printing. we can typecast to any datatype"""
print(5*"python\t")  #python gets printed 5 times with tab space
print( 2 * int(v7) + int(v6))
print(5* str(int(v7) + int(v6)));

a=23
b=a
print(b)
print(id(a))  #here in python we if the data inside different vaiables are same then the adresses are same for both
              #what happenes is both variables points to the same value or same memory block
print(id(b))
c=23
print(id(c))  #infuture also if we creat  variable with same value then it also points the same memoryb block as this c also has same address
a=10
print(id(a))  #id of a is changed as new value is assigned
print(b)
print(id(b))  #but as we assignes b=a above but address and value of b is not changed because its over in past

"""QUIZ OF THE DAY
print("enter 2 no.'s to add")
a= input()
b= input()
print(a,b)
c = int(a) + int(b)
print( "answer is ",c)
#print("answer is",int(a)+int(b))"""



