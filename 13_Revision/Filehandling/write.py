file = open("data.txt","w")
file.write("Hello World")
print(file)
file.close()

# Better way to write
with open("data.txt","w") as file:
    file.write("Hello GIRLS")
    