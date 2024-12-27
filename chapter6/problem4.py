# Problem4 : Write a program to find whether a given username contains less than 10 characters or not.

characters = input("Enter your characters: ")

if (len(characters) > 10):
    print("Username contains more than 10 characters.")
elif(len(characters) <= 10 ):
    print("Username contains 10 characters or less than 10 characters.")
