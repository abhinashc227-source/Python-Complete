#1 Typecode
import array as arr
val = arr.array('i',[1,2,3,4,5])
print(val.typecode)
print("/n")

# Reverse the array 
val.reverse()
for i in range(0,len(val)):
    print(val[i],end=",")
print("/n")

# Insert the array : In insert the add a new value and other value to the other side.
val.insert(2,100)
for i in range(0,len(val)):
    print(val[i],end=",")
print("/n")

# Append the array 
val.append(500)
for i in range(0,len(val)):
    print(val[i],end=",")
print("/n")
# REPLACE THE VALUE
val[2] = 200
for i in range(0,len(val)):
    print(val[i],end=",")
