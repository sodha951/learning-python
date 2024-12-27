# # Problem2: Write a python program using function to convert celsius to fahrenheit.

def cel_to_fah(c):
    return (c * 9/5) + 32

c = int(input("Enter temperature in C: "))
d = (cel_to_fah(c))
print(F"{round(d,2)} °F")