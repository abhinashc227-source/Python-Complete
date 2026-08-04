age = int(input("Enter your age :"))

#If statement no 1
if(age%2==0):
    print("age is even")
# End of statement no 1 

#If statement no 2 
if(age>=18):
    print("You are adult now")
    print("You can go college now")

elif(age<0):
    print("You are enterning invalid age ")

elif(age==0):
    print("Age should be greater than 0")

else:
    print("You are teanagers now")

# End of statment no 2