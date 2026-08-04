#  Write a recursive function to calculate the sum of first n natural numbers.

def rec(n):
    if n == 0:
        return 0
    else:
        return n + rec(n - 1)

num = int(input("Enter the natural number: "))
print("Sum is:", rec(num))
