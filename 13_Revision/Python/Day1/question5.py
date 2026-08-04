# WAP to ask the user to enter names of their 3 favorite movies and store them in a list 

list = [] 
movies1 = input("Enter the movie 1 : ")
movies2 = input("Enter the movie 2 : ")
movies3 = input("Enter the movie 3 : ")

# list = [movies1,movies2,movies3]

# print(list.sort())
# print(list)

list.append(movies1)
list.append(movies2)
list.append(movies3)

list.sort()

print(list)


