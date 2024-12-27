# Problem4 : Add a static method in problem 2, to greet the user with hello.



import math

class Calculator:
    
    def __init__(self, n):
        self.n = n
        
    def square(self):
        return self.n ** 2
    
    def cube(self):
        return self.n ** 3
    
    def squareroot(self):
        return math.sqrt(self.n)
    
    @staticmethod
    def greet():
        return "Hello world!"
    
cal = Calculator(16)
print(cal.square())
print(cal.cube())
print(cal.squareroot())
print(cal.greet())
