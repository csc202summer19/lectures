# NOTE: This does not create an object; it just defines a class:
class Point:
    """ A point in the Cartesian plane """
    def __init__(self, x, y):
        self.x = x # Initialize the integer x-coordinate
        self.y = y # Initialize the integer y-coordinate

    def __eq__(self, other):
        return (type(other) == Point
                and self.x == other.x
                and self.y == other.y)

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)


# This actually creates two distinct objects:
p1 = Point(1, 2)
p2 = Point(9, 4)

# This does not instantiate a new object:
p3 = p1


# This implements the translation operation described in the point ADT:
def translate(pt, dx, dy):
    """ Translate a point. """
    return Point(pt.x + dx, pt.y + dy)
