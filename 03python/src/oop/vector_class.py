""" Vector class
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception

If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.

"""

import math
class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    
    def __str__(self):
        if len(self.coordinates) != 0:
            lst = ','.join([str(x) for x in self.coordinates])
            return f"({lst})"
        return ''
    
    def add(self, other):
        if len(self.coordinates) == len(other.coordinates):
            return Vector([self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates))])
        else:
            raise Exception
    
    def subtract(self, other):
        if len(self.coordinates) == len(other.coordinates):
            return Vector([self.coordinates[i] - other.coordinates[i] for i in range(len(self.coordinates))])
        else:
            raise Exception
    
    def dot(self, other):
        if len(self.coordinates) == len(other.coordinates):
            return sum([self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates))])
        else:
            raise Exception
    
    def norm(self):
        return math.sqrt(sum(x**2 for x in self.coordinates))
    
    def equals(self, other):
        return self.__dict__ == other.__dict__