"""v1=[0,1,2,3,4,5]

for i in v1:
    if i==4:
        continue  #here continue will stop control there and will take control to starting again
    print(i)"""

"""v1=[0,1,2,3,4,5]

for i in v1:
    if i==3:
        break  # here break will take control direct to the end of loop or whatever 
    print(i)"""

#pass
#its a keyword used to pass the block if we do not know what statements to write inside that block
v1=[0,1,2,3,4,5,6]
for i in v1:
    if i >= 3:
       print(i)
    else:
        pass  #we used because we may write statements inside this block later on



