#13 Write a program to accept marks of 6 students and display them in a sorted manner. 
li = []
accept_marks1 = int(input("Enter the marks:"))
li.append(accept_marks1)
accept_marks2 = int(input("Enter the marks:"))
li.append(accept_marks2)
accept_marks3 = int(input("Enter the marks:"))
li.append(accept_marks3)
accept_marks4 = int(input("Enter the marks:"))
li.append(accept_marks4)
accept_marks5 = int(input("Enter the marks:"))
li.append(accept_marks5)
accept_marks6 = int(input("Enter the marks:"))
li.append(accept_marks6)

new_li = li.sort()
print(li)