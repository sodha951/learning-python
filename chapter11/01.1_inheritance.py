class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}. ")
        
class Programmer:
    company = "ITC Infotech"
    
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}. ")
        
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language. ")
        
a = Employee()

b = Programmer()
print(a.company, b.company)


class Employee:
    a = 1
    
class Programmer(Employee):
    b = 2
    
class Coder(Programmer):
    c = 3
    
o = Employee()
print(o.a)

o = Programmer()
print(o.a, o.b)

o = Coder()
print(o.a,o.b,o.c)