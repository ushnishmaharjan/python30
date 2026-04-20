class Test():
    a=100

class Test2():
    b=1000

class Child( Test,Test2):
    c=10000


class Person():
    def setperson(self,name,age):
    
        self.name=name
        self.age=age

    def displayperson(self,):
        return f'Name: {self.name}, Age:{self.age}'
    
#obj=Person()
#obj.setperson('hari', 23)
#print(obj.displayperson())


class Job():
    def setjob(self,Jobtitle,salary):
        self.Jobtitle=Jobtitle





