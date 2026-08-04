letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

letter = letter.replace("<|Name|>", "Abhinash")
letter = letter.replace("<|Date|>", "13 March 2026")

print(letter)


print(letter.replace("<|Name|>", "Abhinash").replace("<|Date|>", "13 March 2026"))     #In shots we can do this