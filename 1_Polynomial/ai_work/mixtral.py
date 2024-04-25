'''mixtral unittest'''

"""Polynomial 0.61"""
class Mono:
    """Mono"""
    def __init__(self, coefficient:int, degree: int, nexts = None) -> None:
        self.coefficient = coefficient
        self.degree = degree if coefficient!=0 else 0
        self.next = nexts
    def __str__(self) -> str:
        x = 'x**'+str(self.degree)
        coef = self.coefficient
        if self.degree == 1:
            x = 'x'
        elif self.degree == 0:
            x = ''
        if self.coefficient == 1:
            coef = ''
        if self.coefficient == 0:
            return 'Mono: 0'
        if self.coefficient == 1 and self.degree==0:
            coef = 1
        return f"Mono: {coef}{x}"
import unittest

class TestMono(unittest.TestCase):
    def test_initialization(self):
        m = Mono(2, 3)
        self.assertEqual(m.coefficient, 2)
        self.assertEqual(m.degree, 3)

    def test_zero_coefficient(self):
        m = Mono(0, 5)
        self.assertEqual(m.coefficient, 0)
        self.assertEqual(m.degree, 0)

    def test_next_attribute(self):
        m1 = Mono(2, 3)
        m2 = Mono(3, 2)
        m1.next = m2
        self.assertEqual(m1.next.coefficient, 3)
        self.assertEqual(m1.next.degree, 2)

    def test_str_method(self):
        m = Mono(2, 3)
        self.assertEqual(str(m), 'Mono: 2x**3')

        m2 = Mono(0, 5)
        self.assertEqual(str(m2), 'Mono: 0')

        m3 = Mono(1, 1)
        self.assertEqual(str(m3), 'Mono: x')

        m4 = Mono(1, 0)
        self.assertEqual(str(m4), 'Mono: 1')

        m5 = Mono(-2, 3)
        self.assertEqual(str(m5), 'Mono: -2x**3')

if __name__ == '__main__':
    unittest.main()