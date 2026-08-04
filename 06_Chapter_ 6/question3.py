# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 
a1 = "Make a lot of money"
a2 = "buy now"
a3 = "suscribe this"
a4 = "click this"

message = input("Enter the comment")

if((a1 in message)or(a2 in message)or(a3 in message)):
    print("This message is a scam ")

else:
    print("This message  is not a scam")
