#Problem3 : Write a program to detect double space in a string.

name = "Alpesh is a good  boy and"

print(name.find("  "))

#Problem4: Replace the double space from problem3 with single spaces.

NAME = "Alpesh is a good  boy and"

print(name.replace("  ", " "))
print(name)

# Strings are immutable which means that you cannot change them by running functions on them.