#28 Write a program to find whether a given number is prime or not. 
num = int(input("Enter the number: "))
for i in range(num):
    if i ==2 or i == 3 or i==5 or i==7:
        print(f"Prime number {i}")
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
        print(f"Prime number {i}")
    else:
        print(f"Not a Prime number")