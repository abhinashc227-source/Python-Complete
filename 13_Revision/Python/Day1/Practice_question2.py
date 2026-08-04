# Create a program that takes a user's name and age as 
# input and prints a greeting message

name = input("Enter the name :")

age = int(input("Enter your age :"))

if name.isalpha() and age>0:
    print("Good Morning")

else:
    print(" Not Valid input")