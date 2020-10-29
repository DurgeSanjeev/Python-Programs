"""Operators
1)arthematic operators : +,-,*,/(division givies quotient),%(modules operator gives reminder ),//(divides and gives integer),**(power)
2)assignment operators : =,+=,-=,*=,/=,%=)
3)Unary operators : =
4)Relational operators : >,<,<=,>=,==,!=
5)Logical operators : and,or,not
6)Bitwise operators : ~(compliment),&(bitwise and),|(bitwise OR),^(bitwise XOR),<<(left shift),>>(right shift)
7)Identity operators : is, isnot
8)Membership operators : in, not in     #cheks weather they are there ir not in some 0place or like list
"""

a=7
b=3
c=4
print(a,b)
print(a*b)
print(a/b)
print(a%b)

a,b=b,a #simple mwthod of swapping 2 elements
print(a,b)

print(-a)
print(~12) #we get -13 because 12 complement in binary is equal to -13  in bianry with the help of 2's complement concept
print(~45)

print(12&13) #we convert 12 and 13 to binary any use "and" truth table and solve we get 12 in binary format
print(12|13)
print(12^13)
print(10<<2) #convert 10 into binary and shift the bianry by 2 lefthand side and calculate it we get 40
print(10>>2)

i=0
i+=1   #which is equal to i=i+1
print(i)
j=9
print(i is j)  #checks weather they are equal or not
print(i is not j)


#when we speak about IDLE we have to import the module by keyword "import"

x=math.sqrt(23)
print(x)