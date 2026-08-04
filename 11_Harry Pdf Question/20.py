#20 Write a program to find the greatest of four numbers entered by the user. 
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))
if(a>=b  and a>=c and a>=d):
    print(f"The greatest number is {a}")
elif(b>a and b>=c and b>=d ):
    print(f"The greatest number is {b}")
elif(c>a and c>b and a>=c and c>=d):
    print(f"The greatest number is {c}")
else:
    print(f"The greatest number is {d}")
