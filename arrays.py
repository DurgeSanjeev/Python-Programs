from array import *
v=array("i",[2,3,5,-96,7,8])
print(v.buffer_info())  #this buffer_info function gives address and length of array
print(v.typecode)  #tells type of array
v.reverse()  #this fun reverses the array but this fun doesnt return any value so its written seperate
print(v)
for i in range(len(v)):  #the length is decided at the runtime dynamically as len is given
    print(v[i])

