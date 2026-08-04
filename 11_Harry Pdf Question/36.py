#36 Write a recursive function to calculate the sum of first n natural numbers. 
def natural_number(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+i
    return sum
num = natural_number(5)
print(num)