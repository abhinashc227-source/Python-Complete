a = 31  
t = type(a) # class <int>
print(t)

b = "31.2"     # So the value is floating but this give the output string because whenever we write "" in double the anything will convert in string 
c = float(b)   # In this we have convert the string value into float but we cannot convert the string value into float means like name i we convert any value that value have to sensible
p = type(c)
print(p)

a = int(input("Enter the number 1 "))  # So the number is merging because we let the value into the string so for sum we have to convert the value into the int function so we can get the value in right way . When ever we have to conert the value into any data types so we have to declare the datatype into the outer cell example a = int(input("Enter the number"))
b = int(input("Enter the number 2 "))
print("Number a is : ",a)
print("Number b is : ",b)
print("Sum is : ",a+b)