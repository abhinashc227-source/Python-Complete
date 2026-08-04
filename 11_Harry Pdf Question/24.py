# 24 Write a program which finds out whether a given name is present in a list or not. 
li = ["Abhinash", "Rahul","Ayushi"]
name = input("Enter the name: ")
if name in li:
    print(f"Name is given in list {li}")
else:
    print(f"Name is not given in list {li}")