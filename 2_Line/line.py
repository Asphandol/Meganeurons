"""intersectioin"""
class Point:
    """point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:
    "Line"
    def __init__(self, p1, p2):
        if p1.x == p2.x and p1.y == p2.y:
            raise ValueError("Cannot create a line from equal points")
        self.p1 = p1
        self.p2 = p2

    def intersect(self, other_line):
        """intersection"""
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = other_line.p1.x, other_line.p1.y
        x4, y4 = other_line.p2.x, other_line.p2.y

        k1 = (y2-y1)/(x2-x1) if x2-x1 else 0
        b1 = y1 - k1*x1

        k2 = (y4-y3)/(x4-x3) if x4-x3 else 0
        b2 = y3 - k2*x3

        if k1 == k2:
            return self if not b1==b2 else None
        return Point(x:=((b2 - b1) / (k1 - k2)), k1 * x + b1)
