#  Write a program to find out whether a given post is talking about “Harry” or not. 
a = "harry"

post = input("Enter the post :").lower()

if(a in post):
    print("Post talking about the harry")

else:
    print("Not talking about the harry")