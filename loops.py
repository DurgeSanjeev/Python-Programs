#loops
#for loop
"""syntax
variable= [......]
for i in variable name:  #here i is a variable indicates a elements of variable ones at a time as its value starts
   statements  #indentation is important

for i in variable/list/:     #we can give whole variable here directly
   statements


"""
"""l1=[["pendrive",1],["harddrive",2],["antivirus",1],["ram",8],["rom",2]]
 print(l1)    #this prints in form of list
print(l1[0]) #prints separetly
#for item in l1:
 #   print(item)
for keys,quantity in l1:
    print(keys,quantity)"""

"""d1={"videos":"youtube","music":"spotify","travell":"uber","serach engine":"Google"}
for items in d1:
    print(items)
for keys in d1:
    print(keys)"""
"""d2=dict(l1)  # here we have typecasted the list into dictionary
print(d2)
for items in d2:
    print(items)
for keys in d2:
    print(keys)"""

"""Quiz"""
"""list=["while","3",12,34,2,4,6,7,8,56,67,87,444,12,"do while"]
for item in list:
    if int(item).isnumeric() and item>6:
        print(item)"""
#while loop
"""syntax
initilise value for variable
while(conditions):
ststements
i++ or i=i+1  #this is here to stop the while loop which increments the value dof i
"""
"""i=0   #this is initilisation 
   while(i<10):
        print(i,end=" ") #indentation is very important which tells that statements are of that block8
        i = i + 1     #increments the value so that it will run rext time"""

#Exercise
a=16
i=0
while(i<5):
    print("guess the no.")
    b=int(input())
    if b==a:
        print("you won")
        break
    elif b<a:
        print("its greater than  the no. u entered ,u have",5-i-1, "chances left")
    elif b>a:
        print("its less than the no. u entered ,u have",5-i-1,"chances left")
    else:
        print("game over")
    #if i ==5:
     #56   print("u lost game over")

    i=i+1

# else:
    #    print("game over")


"""i=1
while i<=5:
    print("hyy",i)
    i=i+1
"""


