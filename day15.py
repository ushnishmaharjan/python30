class Test():
    a=100

class Test2():
    b=1000

class Child( Test,Test2):
    c=10000


#Employee management system

class Person:

    def setPerson(self,name,age):
        self.name = name
        self.age = age

    
    def display_person(self):
        return f"name = {self.name}, age = {self.age}"

class Job:

    def setJob(self,jobTitle):
        self.jobTitle = jobTitle

    def setSalary(self,salary):
        self.salary = salary

    def display_job(self):
        return f"job title = {self.jobTitle} , salary = {self.salary}"

class Employee(Person,Job):
    
    def isHighEarner(self):
        if self.salary > 45000:
            return "High earner"
        else:
            return "Low earner"

    def display_employee(self):
        return f"{self.display_person()} , {self.display_job()} , {self.isHighEarner()}"
    

employee = Employee()
employee.setPerson("hari",12)
employee.setJob("pyython")
employee.setSalary(20000)

print(employee.display_employee());





