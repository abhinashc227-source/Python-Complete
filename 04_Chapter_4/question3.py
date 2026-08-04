 #Check that a tuple type cannot be changed in python.

change = (5, 6, "Rohan ")
a = type(change)
print(a)

change[2] = 10

print(change)