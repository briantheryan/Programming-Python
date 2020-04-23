"""
Exercises 11.1.12
1)
"""
import math


class Point:
    """Test"""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def to_string(self):
        return "({0}, {1})".format(self.x * -1, self.y)

    def reflect_x(self):
        return((self.x * -1) + self.y


p1 = Point(1, 7)
p2 = Point(5, 12)

print(distance(p1, p2))
print(p1.to_string())


    """def distance(self):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    """







