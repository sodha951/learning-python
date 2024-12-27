# Problem7 : Write a program to find out whether a given post is talking about "Alpesh" or not.

post = input("Enter the post: ")

if("Alpesh".lower() in post.lower()):
    print("This post is talking about Alpesh.")
else:
    print("This post is not talking about alpesh.")
    
    