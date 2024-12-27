# Problem7 : Write a python function which converts inches to cms.

def inch_cms(inch):
    return inch * 2.54

n = int(input("Enterr value in inches: "))
print(f"The corresponding value in cms is {inch_cms(n)}")