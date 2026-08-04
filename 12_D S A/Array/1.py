# Making array 
# 1 way to make the array 
import array

arr = array.array('i',[1,2,3,4,5,6])

# 1st way to print with the range method
for i in range(0,6):
    print(arr[i],end=",")
print("\n")

#2nd way to print with the making the new variable
for x in arr:
    print(x,end="-")
print("\n")


# 2nd way to make the array 

import array as arr

val = arr.array('i', [1,2,3,4,5])
for y in val:
    print(y,end=".")
print("\n")

# 3rd way to make the array this is a most efficient way 

from array import*

num = array('i',[1,2,3,4])

for z in num:
    print(z,end="/")
