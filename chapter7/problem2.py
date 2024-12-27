# problem2 : Write a program to greet all the person names stored in a list "l" which starts with S.

l = ["Alpesh","Harry","Sachin","Parth","Rahul","Sagar"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
    
