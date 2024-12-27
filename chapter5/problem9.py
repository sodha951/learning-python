# Problem9 : Can you change the values inside a list which is contained in set s?

s = {8, 7 , 12, "Alpesh", [1,2]}

s.add((3,4))
print(s)

# No, you cannot include a list as an element of a set in Python. This is because sets require their elements to be immutable (i.e., they cannot be changed after they are created), and lists are mutable (i.e., their elements can be changed).