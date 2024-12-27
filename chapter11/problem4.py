# Problem4 : Write a class 'Complex' to represent comple numbers, along with overload operators "*" and "+" which adds and multiplies them.

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
        
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        return Complex(self.r * c2.r - self.i * c2.i, self.r * c2.i + self.i * c2.r)
    
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1+c2)
print(c1*c2)