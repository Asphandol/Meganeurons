import unittest
from line import *

class TestLine(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(3, 3)
        self.line1 = Line(self.p1, self.p2)

        self.p3 = Point(1, 0)
        self.p4 = Point(2, 1)
        self.line2 = Line(self.p3, self.p4)

        self.line3 = Line(Point(0, 1), Point(1, 0))
        self.line4 = Line(Point(1, -1), Point(-1, 1))

    def test_intersect_parallel_lines(self):
        self.assertIsNone(self.line1.intersect(self.line2))

    def test_intersect_lines_with_same_slope(self):
        self.assertEqual(self.line1, self.line1.intersect(self.line1))

    def test_creating_a_line_with_identical_points_raises_ValueError(self):
        p1 = Point(3, 3)
        with self.assertRaises(ValueError):
            Line(p1, p1)

    def test_intersecting_lines(self):
        self.assertEqual(self.line1.intersect(self.line3), Point(0.5, 0.5))
        self.assertEqual(self.line4.intersect(self.line1), Point(0, 0))



# if __name__ == '__main__':
#     unittest.main()
