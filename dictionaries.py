#dictionaries
#are key value pairs key is same as word these are unordered, mutable and indexed
d1={"men":"women","love":"hate","sleep":"die","coding":{"single":"commited","alone":"extrovert"}}  #here terms before colon and after are related
print(type(d1))  # we can write a dictionary inside a dictionary
print(d1)
print(d1["men"])
print(d1["coding"])
print(d1["coding"]["single"])  #we get ooutput as sub dictionary by using another square bracket inside it
d1["fat"]="showoff"  #we can add new elements again
print(d1)
del d1["fat"]  # deletion of elements
print(d1)
print(d1.keys())  #here before colon values are known as keys and after colon values are known as values
print(d1.items())
print(d1.values())

#Exercise1
#making a dictionary of some words and taking input from user to search for word

"""oxford={"frontend development":"developing the user interface with the help of HTML,CSS,JavaScript,JQuery","backend development":"server side programming using NodeJS,PHP,MySql,python","fullstack development":"doing server side and GUI programming","datastructures":" programming and storing and using the data in efficient way","algorithms":"writing a code with certain logic in it doing specific task"}
print(oxford)
print("enter a word to search")
s=input()
print(s)
print(oxford[s])"""

#print(oxford["frontend development"])


"""d= dict()
#print(input(" enter the values"))
d["monkey"] = 2
d["rats"] = 3
d["monkey"] = d["monkey"] + 2          #we can add the value or change as we wanted
d["horse"] =5
print(d)"""

"""d= dict()
n= input("file name:" )
fhand= open(n)
#n= {"men":"women","love":"hate","sleep":"die","coding":{"single":"commited","alone":"extrovert","men"}}
#n= {"men","love","sleep","coding","gay"}
for names in n:
    if names not in d :
        d[names]=1
    else:
        d[names]=d[names] +1
print(d)"""

"""d= dict()
text = input(' ')
print(text)
a = text.split()
#print(a)
print('Words:', a)
for word in a:
    d[word] =  d.get(word,0) +1
print(d)"""

"""m={"piedpiper":1,"hoolie":2,"google":5}
for key in m:                                #here the  random variable only loops through the keys not the values
    print(key,m[key])

n={"richard hendrics":1,"gilfoil":2,"dinesh":3,"buchmann":4,"jared":5}
print(list(n))                          #this turns dictionary to the list as the values gets dissappear
print(n.keys())                         #this keys() method returns the keys of dictionary
print(n.values())                       #this values() metthod returns the values in dictionary
print(n.items())

for a,b in n.items():                   #we can use both iteration variables atsame time
    print(a,b)"""

print("enter filename")
fn=input()
handle= open(fn)
d=dict()
for line in handle:
    w = line.split()
    #print(w)
    for word in w:
        d[word]=d.get(word,0)+ 1
print(d)
bigcount=None
bigword=None
for bc,bw in d.items():
    if bigcount is None or bc > bigcount:
        bigcount =bc
        bigword = bw
print(bigword,bigcount)
