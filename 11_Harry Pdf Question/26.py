#26Write a program to print multiplication table of a given number using for loop. 
table = int(input("Enter the table: "))
i = 1
while(i<=10):
    print(f"{table}*{i}={table*i}")
    i+=1

for num in range(1,11):
    print(f"{table}*{num}={table*num}")