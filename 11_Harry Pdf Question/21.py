#21 Write a program to find out whether a student has passed or failed if it requires a 
#total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#take marks as an input from the user. 
marks1 = int(input("Enter the marks1: "))
marks2 = int(input("Enter the marks2: "))
marks3 = int(input("Enter the marks3: "))
total_marks = ((marks1+marks2+marks3)/300)*100
if (total_marks>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print(f"Student is passed with {total_marks}% ")
else:
    print(f"Student is failed by {total_marks}%")
