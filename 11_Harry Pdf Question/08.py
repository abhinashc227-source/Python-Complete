#8. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 
name = input("Enter the name:")
date = input("Enter the date:")
print(f'''Dear {name}, 
          You are selected! 
          {date}''')