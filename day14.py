class Parent:
    a = 100
    b = 1000

    def __init__(self, a, b):
        print("this is cons from parent")

    def add(self):
        return self.a + self.b


class Child(Parent):

    def __init__(self, a, b):
        print("this is cons from child")
        super().__init__(a, b)

    def result(self):
        return self.add()


class GrandChild(Child):
    def summary(self):
        return"this is summary data"

#obj=GrandChild(10, 20)
#print(obj.add())


class Person():
    
    name="hari"
    age=12

    def __init__(self,lang="eng"):
        self.lang=lang

    def display_info(self):
        return f'{self.name} is {self.age} years old '
    
    def display_info_np(self):
        return f'Mero name {self.name} ho , age {self.age} years ho '


class Student(Person):
    student_id="S001"

    def display_student(self):
        return f'{self.display_info()} and student id is {self.student_id}'
    
    def display_student_np(self):
        return f'{self.display_info_np()} , mero  student id  {self.student_id} ho'

class GraduateStudent(Student):
    thesis_topic="data structure with python"

    def display_graduate(self):
        if self.lang=="nep":
            return f'{self.display_student_np()} ra thesis topic {self.thesis_topic} ho.' 
        return f'{self.display_student()} and thesis topic is {self.thesis_topic}' 
    

obj=GraduateStudent("nep")
print(obj.display_graduate())

