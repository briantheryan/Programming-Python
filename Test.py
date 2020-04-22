"""
Exercises 11.1.12
"""


class Point:
    """Test"""
    import math
    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def distance(self):
        """Compute the distance between points."""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    """def distance(p1, p2):
        return math.sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2)
"""


p = Point(5, 12)
print(p.x)
print(p.distance())