#30 Write a program to calculate the factorial of a given number using for loop. 
n = int(input("Enter the number: "))
i = 2
factorial = 1
while i<=n+1:
    factorial = factorial*(i-1)
    i+=1
print(factorial)

n = int(input("Enter the number: "))

i = 1
factorial = 1

while i <= n:
    factorial *= i
    i += 1

print(factorial)

# Through the for loop 
n = int(input("Enter the number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)