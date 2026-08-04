age = int(input("Enter your age :"))

if(age>=18):
    print("You are adult now")
    print("You can go college now")

elif(age<0):
    print("You are enterning invalid age ")

elif(age==0):
    print("Age should be greater than 0")

else:
    print("You are teanagers now")