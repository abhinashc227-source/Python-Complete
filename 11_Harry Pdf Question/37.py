# 37 Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * 
def star_print(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*",end="")
        print()
star_print(3)

