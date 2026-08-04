#34  Write a program to print multiplication table of n using for loops in reversed order
n= int(input("Enter the table do you want: "))
for i in range(10,1,-1):
    print(f"{n}*{i}={n*i}")