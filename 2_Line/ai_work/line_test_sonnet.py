import unittest
from line import Line
from point import Point

class TestIntersect(unittest.TestCase):
    def setUp(self):
        self.line1 = Line(Point(0, 0), Point(1, 1))
        self.line2 = Line(Point(0, 1), Point(1, 0))
        self.line3 = Line(Point(0, 0), Point(2, 2))
        self.line4 = Line(Point(1, 1), Point(3, 3))
        self.line5 = Line(Point(0, 0), Point(0, 1))
        self.line6 = Line(Point(0, 0), Point(0, 1))
        self.line7 = Line(Point(1, 1), Point(2, 2))
        self.line8 = Line(Point(1, 0), Point(1, 2))
        self.line9 = Line(Point(2, 0), Point(2, 2))
        self.line10 = Line(Point(-1, -1), Point(1, 1))
        self.line11 = Line(Point(0, 0), Point(1, 0))
        self.line12 = Line(Point(1, 2), Point(3, 4))
        self.line13 = Line(Point(1, 2), Point(3, 6))

    def tearDown(self):
        pass

    def test_intersect_lines(self):
        self.assertEqual(self.line1.intersect(self.line2), Point(0.5, 0.5))

    def test_no_intersection(self):
        self.assertIsNone(self.line1.intersect(self.line3))

    def test_same_lines(self):
        self.assertEqual(self.line5.intersect(self.line6), self.line5)

    def test_parallel_lines(self):
        self.assertIsNone(self.line3.intersect(self.line4))

    def test_collinear_lines(self):
        self.assertEqual(self.line3.intersect(self.line7), self.line3)

    def test_vertical_lines(self):
        self.assertIsNone(self.line8.intersect(self.line9))

    def test_negative_slope(self):
        self.assertEqual(self.line1.intersect(self.line10), Point(0.5, 0.5))

    def test_zero_length_line(self):
        self.assertIsNone(self.line5.intersect(self.line11))

    def test_different_slopes(self):
        self.assertEqual(self.line12.intersect(self.line13), Point(2, 3))

    def test_large_coordinates(self):
        line14 = Line(Point(1000, 2000), Point(3000, 4000))
        line15 = Line(Point(2000, 1000), Point(4000, 5000))
        self.assertEqual(line14.intersect(line15), Point(2000, 3000))

if __name__ == '__main__':
    unittest.main()
