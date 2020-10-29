#Functions
""" Syntax of user defined function
def function name():  this is function defination
    statements...      #indentation is important
function name()     #this is function calling"""

def f(a,b):                            #function defenation
    """this is to compare the variables"""
    #a=int(input("enter a"))
    #b=int(input("enter b"))
    if a>b:
        print("greater")
    else:
        print("less")
f(4,6)                                  #function calling by taking input form calling
#print(f())                             #because of no. return value we get  none
print(f.__doc__)   #this is known as docstring which tells about a function and print the output that we gave in inverted commas just below the function entry