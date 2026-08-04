#22 A spam comment is defined as a text containing following keywords: 
#“Make a lot of money”, “buy now”, “subscribe this”, “subscribe this”. Write a program 
#to detect these spams. 
message = input("Enter the message: ")

if ("Make a lot of money" in message or
    "buy now" in message or
    "subscribe this" in message):
    print("Message is spam")
else:
    print("Message is not spam")