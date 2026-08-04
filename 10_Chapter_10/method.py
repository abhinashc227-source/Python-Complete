class Student:
    def __init__(self,name,grade,marks):
        self.name = name     # Object Attributes> # Class Attributes
        self.grade = grade
        self.marks = marks

    def hello(self):
        print("Hello",self.name)

s1 = Student("Abhinash Kumar","A++",97)
print(s1.name,s1.grade)
s1.hello()

