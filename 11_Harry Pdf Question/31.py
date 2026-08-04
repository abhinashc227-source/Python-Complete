#31 Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 
# n= 3 
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

l = 3
for i in range(1,l+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*l-2*i+1):
        print("*",end="")
    print()