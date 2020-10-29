"""l=6                           #global variable
def fun1(n,m):
    global l                  #global keyword is used to access the variable declared globally and in that we can also manupulate them
    l=7                       #local variable
    l=l+3
    print(l)
    print(n,m,"bye")


fun1("helllo","HIII")
print(l)"""


"""def fun2():
    k=2
    print(k)
    def fun3():
        global k            #here this global variable will directly go outside of all above functions or anything above
        k=4
    print(k)
    fun3()
    print(k)
fun2()
print(k)"""


"""def fun4(str1):
    
    print("i am" + str1)
fun4(" 12sanju")"""

"""def factorial1(n):           #functiom to get factorial of no. using iterations
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    #print(fac)
    return fac
num = int(input("enter the no."))
print(factorial1(num))"""

"""def factorial2(n):                      #factorial using recursion
    if n==1:
        return 1
    else :
        return n * factorial2(n-1)
num = int(input("enter the no."))
print(factorial2(num))"""


def fibonaci(n):                             #fibonaci series using recursion
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
num = int(input("enter the no."))
print(fibonaci(num))




