file = open("data.txt","a")
file.write("\nHello World")
print(file)
file.close()

## Better way
with open("data.txt","a") as file:
    file.write("Hello Bachoo")
    