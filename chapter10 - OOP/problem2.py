# Problem2 : Write a class “Calculator” capable of finding square, cube and square root of a number.

# import math

# class Calculator:
    
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         return self.n ** 2
    
#     def cube(self):
#         return self.n ** 3
    
#     def squareroot(self):
#         return math.sqrt(self.n)
        
# a = Calculator(64)
# print(a.square())
# print(a.cube())
# print(a.squareroot())


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
    
cal = Calculator(16)
print(cal.square())
print(cal.cube())
print(cal.squareroot())