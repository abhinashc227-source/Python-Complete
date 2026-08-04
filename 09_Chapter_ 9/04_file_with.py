# f = open(r'Chapter 9/file.txt')
# data = f.read()
# print(data)
# f.close()

# We can write this statement in very small code with the help of with statement

with open('Chapter 9/file.txt') as f:
    text =  f.read()
print(text)
