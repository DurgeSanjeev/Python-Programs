str1="Guido Van Russo"
"""print(str1)
print(str1[0])               #here string is like array starting with 0,1,2,.... here it prints "G"o here after colon no. is excluded
print(str1[0:5])
print(len(str1))             #len() is inbuilt function to tell length os string
print(str1[0:15])            #prints everything
print(str1[0:44])            #also prints everything
print(str1[1])               #prints "u"
print(str1[7])               #prints according
print(str1[0:4])             #this prints as strating from 0=G and ends before 4=
#print(str1[23])       #error
print(str1[0:])              #also prints till end from given point
print(str1[:15])             #prints from strating till given end point
print(str1[:])               #prints from starting till end
print(str1[0:15:2])          #after second colon we write the difference ,skips 1 character between
print(str1[0:15:])           #by default difference is 1
print(str1[::])              #prints all
print(str1[::6049588])   """    #prints till possible
print(str1[-4])              #starts counting from back of string  from -1 not from 0
print(str1[-5:-2])           #starts from  -5 and goes to right side till -3 as we know after colon the no.is excluded
print(str1[::-1])            #reverses whole string
print(str1[::-2])            #after reversing the original string then from starting it starts skipping
print(str1.isalnum())       # isalnum() is a function checks weather all characters are alphanumeric (alphabets or numbers) //stringname.isalnu() is syntax
print(str1.isalpha())       #isalpha() is a boolian function which handles string where it is true if and only if string contains only alphabets
                               # there should be no spaces,nuumbers,symbols // stringname.alpha() is syntax
print(str1.capitalize())
print(str1.endswith("g"))
print(str1.encode())
print(str1.find("Van"))
print(str1.expandtabs())
print(str1.index("Van"))
print(str1.format())
print(str1.isdigit())

print(str1.count("s"))
#print(str1.replace("Van","nun"))