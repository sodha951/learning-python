#Override the __len__() method on vector of problem 5 to display the dimension of the vector.



class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        return result

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __len__(self):
        return 3

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)  
print(v1 * v2)  
print(len(v1))  