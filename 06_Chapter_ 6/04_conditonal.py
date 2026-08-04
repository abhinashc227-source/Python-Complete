# # WAP to check i a number entered by the user is odd or even 

number = int(input("Enter the number : "))

if(number%2==0):
     print("The number is even ")

else:
    print("The number is odd")

#WAP to find the greatest of 3 numbers entered by the user 

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))

if(num1>=num2 and num1>=num3 ):
   print(num1 , " is greater")

elif(num2>num1 and num2>=num3):
   print(num2, "is greater number")

else:
   print(num3 , "is greater ")


# WAP to check if a number is a multiple of 7 or not

multiple = int(input("Enter the number "))

number = multiple%7

if(number == 0):
    print(multiple , "is multiple of 7")

else:
    print("Invalid number")