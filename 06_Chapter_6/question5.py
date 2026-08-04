#  Write a program which finds out whether a given name is present in a list or not.
a1 = "Abhi"
a2 = "Abhinash"
a3 = "Rahul"
a4 = "Rekha"

name = input("Enter the name : ")

if((a1 in name )or(a2 in name)or(a3 in name)or(a4 in name)):
    print("Present")

else:
    print("Absent")