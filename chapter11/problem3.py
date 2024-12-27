# Problem3 : Create a class "Employee" and add salary and increament property to it. Write a method 'salaryAfterincrement' method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 234
    increment = 20
    
    @property
    def salaryAfterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterincrement.setter
    def salaryAfterincrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100
        
e = Employee()
print(e.salaryAfterincrement)
e.salaryAfterincrement = 280.8
print(e.increment)