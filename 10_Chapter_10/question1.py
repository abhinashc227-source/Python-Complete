# Create student class that takes name and marks of 3 subject as arguments in constructor. Then create a method to print the average.

class Students:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    def avg(self):
        # return sum(self.marks) / 3
        print(sum(self.marks)/3)


s1 = Students("Abhinash", 95, 90, 85)
print(s1.name, s1.avg())

s2 = Students("Sumit", 80, 70, 90)
print(s2.name, s2.avg())

s3 = Students("Rahul", 60, 75, 80)
print(s3.name, s3.avg())