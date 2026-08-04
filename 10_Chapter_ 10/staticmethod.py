class Students:
    college_name = "ABC college"   # Class Attributes
    name = "anonymous"             # Class Attributes
    #default constructors means jb hum constructor define nhi karte hai toh apne aap python constructor initialize kar deta hai 
    def __init__(self):
        pass

    #Parameterized constructors
    def __init__(self,name,grade,marks):
        self.name = name     # Object Attributes> # Class Attributes
        self.grade = grade
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello World")

s1 = Students("Abhinash kumar",'A++',97)
print(s1.name,s1.grade,s1.marks,s1.college_name)
print(f"My name is {s1.name} and my grade are {s1.grade} and marks are {s1.marks} my college name {s1.college_name}")
s1.hello()