#29 Write a program to find the sum of first n natural numbers using while loop. 
number = int(input("Enter the number: "))

i = 1
total = 0

while i <= number:
    total = total + i
    i += 1

print("Sum =", total)
# with the for loop 
number = int(input("Enter the number: "))

total = 0

for i in range(1, number + 1):
    total = total + i

print("Sum =", total)