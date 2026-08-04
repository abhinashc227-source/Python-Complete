#19 Create an empty dictionary. Allow 4 friends to enter their favorite language as 
#value and use key as their names. Assume that the names are unique. 
d= {}
name1 = {
    "rahan": input("Enter the favourite language: ")
}
d.update(name1)
name4 = {
    "rahan": input("Enter the favourite language: ")
}
d.update(name4)
name2 = {
    "Abhinash": input("Enter the favourite language: ")
}
d.update(name2)
name3 = {
    "Ritik": input("Enter the favourite language: ")
}
d.update(name3)

print(d)