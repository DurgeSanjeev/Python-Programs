#classes
class employee:
    no_of_emps=0
    raise_amount=2.3
    def __init__(self,firstname,lastname,id,salary):         #this is called as constructur which helps to create the instance variables,here the init() fun is called automatically and it refres to self
        self.firstname=firstname                    # instance variable stores the data that is unique
        self.lastname=lastname
        self.id=id                                 #here for all variables we are creating we have to self which actully substutes the object at the interpretation
        self.salary=salary
        self.gmail=firstname+"."+lastname+"@gmail.com"
        employee.no_of_emps+=1

    def fullname(self):                                           #these are regular methodes
        return "{} {}".format(self.firstname,self.lastname)
    def apply_raise(self):        #in regular method creation we call the instamnce variable self so
        self.salary= int(int(self.salary) * int(self.raise_amount))
        #self.salary = int(self.salary + employee.raise_amount)

    @classmethod         #this tells that this is class method  the classmethod is called decorator denoted with symbol "@"
    def set_raise_amt(cls,amount):           #in here we call cls like we call self in regular method
        cls.raise_amount=amount
 #   @classmethod
  #  def form_str(cls,emp_str1):
   #     firstname, lastname, salary = emp_str1.split("-")
    #    return cls(firstname,lastname,salary)




print(employee.no_of_emps)
emp1=employee('mohd','farhan','11065','40000')        #emp1 is instance or object in the class in employee
emp2=employee("sanchay","swaraj","11066","30000")  #as we created the init() function here we can directly assign values to the class variables
print(emp1)             #this prints the as it is object of employee and the address in specefic address
print(emp1)

"""emp1.firstname="mohd"     #these are called instance variables which belongs to the object given
emp1.lastname="farhan"
emp1.id="11065"
emp1.salary="40000"
emp1.gmail="farhan.mustafa@gmail.com"

emp2.firstname="sanchay"
emp2.lastname="swaraj"
emp2.id="11066"
emp2.salary="30000"
emp2.gmail="sanchay.swaraj@gmail.com"""

print(emp1.id)           #printing the id of emp1
print(emp2.id)

print(emp1.gmail)
print(emp2.gmail)

print("{} {}".format(emp1.firstname,emp1.lastname))     #a way to create method outside of the class
#print(emp2.fullname())      #we can directly call the method we crated in the class by giving the object name
#print(emp2.fullname)
print(employee.fullname(emp2))   #here another way to print fullname by using the class name but class dont give it self automatically
                                  #so it doesnt know to call what instance or object to call so we have to give it

#class variables are the variables that are shared between all the instances in the class

employee.set_raise_amt(2.5)    #this is class method bcoz we are using this whole class methodes gets updated
employee.raise_amount=3.5     #this is normal method it also updated the whole class as we called it
emp1.raise_amount=5      # this effects only the emp1 instance as we called it
emp2.set_raise_amt(4.7)    #we can also use classmethodes to update the single instances

print(emp1.raise_amount)      #here we can see the raise amount we have given in the class which we give as class variable
print(employee.raise_amount)     #here the raise_amount checks weather the instance conatins the  attribute
print(emp2.raise_amount)
print(emp1.salary)
emp1.apply_raise()      #we applied the raise methid to the emp1 object
print(emp1.salary)         #we can see raise in salery in emp1

print(employee.no_of_emps)         #this tells the no. of objects or instance are created in the class employee

emp_str1= "akshay-kumar-20000"
emp_str2="nupun-kothari-23000"
emp_str3="alok-kumar-24000"

firstname,lastname,salary=emp_str1.split("-")
print(salary)
new_emp1=employee(firstname,lastname,id)

new_emp=employee.form_str(emp_str1)
