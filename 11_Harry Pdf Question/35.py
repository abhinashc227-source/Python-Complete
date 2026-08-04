#35 Write a program using functions to find greatest of three numbers. 
def greatest_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>a and b>=c:
        return b
    else:
        return c
three_number = greatest_number(15,25,35)
print(f"The greatest is {three_number}")