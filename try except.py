#Try Except Exception Handling
#we use this if we are getting error but we want the next line to  run
a =6
b =5
try:
    print(int(a,b))  #it trys this line if this does'nt work then it defines this error and prints it and runs next line of code
except Exception as e:  #here e refers to the type of error and defines error,here  Exception is a keyword a
    print(e)
print("important to run this")
