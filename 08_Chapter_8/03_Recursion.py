# The concept of Recursion with the help of Factorial
# Factorial concept
# Factorial(1) = 1
# Factorial(2) = 2*1
# Factorial(3) = 3*2*1
# Factorial(4) = 4*3*2*1
# Factorial(5) = 5*4*3*2*1
#             .
#              .
# Factorial(n) = n*(n-1)*.........3*2*1
# Factorial(n) n*factorial(n-1)

def fac(n):
    if(n==0 or n==1):
        return 1 
    else:
        return n*fac(n-1)
    
n = int(input("Enter the number : "))
    
print("Factorial of this number is :",fac(n))