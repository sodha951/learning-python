#Problem6: Create an empty dictionary.Allow 4 friends to enter their favorite language as value and use key as their names.Assume that the names are unique.

d = {}
d.update({"Alpesh":"Python"})  
d.update({"Parth":"C++"})
d.update({"Aayushi":"C"})
d.update({"Tembo":"JAVA"})
print(d)

dict = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
dict.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
dict.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
dict.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
dict.update({name: lang})

print(dict)