class Point:
    """Test"""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def reflect_x(self):
        return self.x, -1 * self.y

    def slope_from_origin(self):
        return float(self.y)/self.x
