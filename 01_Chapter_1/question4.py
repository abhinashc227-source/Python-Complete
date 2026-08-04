import os

path = r"C:\Users\Abhinash kumar\OneDrive\Documents"

contents = os.listdir(path)

for item in contents:
    print(item)