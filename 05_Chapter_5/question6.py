#  Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

s1 = {}

name = input("Enter the friend name :")
lang = input("Enter the language name : ")
s1.update({name:lang})
name = input("Enter the friend name :")
lang = input("Enter the language name : ")
s1.update({name:lang})
name = input("Enter the friend name :")
lang = input("Enter the language name : ")
s1.update({name:lang})
name = input("Enter the friend name :")
lang = input("Enter the language name : ")
s1.update({name:lang})

print((s1))