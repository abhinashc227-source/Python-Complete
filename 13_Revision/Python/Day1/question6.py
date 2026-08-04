# Store the following word meanings in a python dictionary 
# table : "a piece of furniture","list of facts & figures"
# cat : "a small animal"

variable = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"

}
print(variable)

# WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# WAP to enter marks of 3 subjects from the user and store them in dictionary.

student_marks = {}

subject1 = input("Enter the subject : ")
marks1 = input("Enter the marks : ")
student_marks[subject1] = marks1

subject2 = input("Enter the subject : ")
marks2 = input("Enter the marks : ")
student_marks[subject2] = marks2

subject3 = input("Enter the subject : ")
marks3 = input("Enter the marks : ")
student_marks[subject3] = marks3

print(student_marks)