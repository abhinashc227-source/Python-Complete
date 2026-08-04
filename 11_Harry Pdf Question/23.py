#23 Write a program to find whether a given username contains less than 10 
#characters or not. 
str = input("Enter the username: ")
if str>="10":
    print(f"The user contains more than 10 characters {str}")
else:
    print(f"The user contain less than 10 character {str}")