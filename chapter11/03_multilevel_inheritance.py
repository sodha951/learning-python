class Employee:
    a = 1

class Programmer(Employee):
    b = 2
    
class Manager(Programmer):
    c = 3
    
# o = Employee()
# print(o.b)

o = Programmer()
print(o.a,o.b)
b = Manager()
print(b.a,b.b,b.c)