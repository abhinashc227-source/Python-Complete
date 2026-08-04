file = open("data.txt","r")
print(file.read())
file.close()

# Shortcut or better way

with open("data.txt","r") as file:
    print(file.read())