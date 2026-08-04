#17 Write a program to create a dictionary of Hindi words with values as their English 
#translation. Provide user with an option to look it up! 
dic = {"jao":"Go",
       "niche":"Down",
       "Ghar":"Home",
       "Uppar":"Up"}
print("Welcome to the gyan pathsala")

meaning = input("Enter the hindi word:")
print("Meaning:",dic.get(meaning,"word not found"))