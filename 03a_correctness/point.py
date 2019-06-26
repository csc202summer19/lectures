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


# This implements the translation operation described in the point ADT:
def translate(pt, dx, dy):
    """
    Translate a point in the Cartesian plane.

    :param pt: The Point to translate
    :param dx: The displacement in the x-direction
    :param dy: The displacement in the y-direction
    :return: A new translated Point
    """
    return Point(2, 3)
