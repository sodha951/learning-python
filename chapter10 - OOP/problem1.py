# Problem1 : Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft",
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = Programmer("Alpesh",1200000,387330)
print(p.name,p.salary,p.pin)
s = Programmer("Divy",123000,38731)
print(s.name,s.salary,s.pin)