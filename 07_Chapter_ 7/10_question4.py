#  Write a program to find whether a given number is prime or not. 

number = int(input("Enter the number : "))

for i in range(2,number):
    if(i%2)==0:
     print("number is even")
     break
    else:
       print("number is not prime")

        