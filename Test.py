"""
Exercises 11.1.12
"""
import math

class Point:
    """Test"""
    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def distance(self):
        """Compute the distance between points."""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def distance1(p1, p2):
    return math.sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2)


p1 = Point(1,7)
p2 = Point(5, 12)

print(distance1(p1,p2))